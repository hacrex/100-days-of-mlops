# Day 57 — Implementation Notes

## What I Did

Built a Flask REST API to serve an Iris classifier, added health/readiness endpoints, and tested it with curl.

## Full App Code

```python
# src/app.py
import logging
import os
import time

import joblib
import numpy as np
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load model at startup
MODEL_PATH = os.getenv("MODEL_PATH", "models/iris_model.joblib")
model = None
load_time = None

def load_model():
    global model, load_time
    start = time.time()
    model = joblib.load(MODEL_PATH)
    load_time = time.time() - start
    logger.info(f"Model loaded in {load_time:.3f}s from {MODEL_PATH}")

load_model()

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "timestamp": time.time()}), 200

@app.route("/ready")
def ready():
    if model is not None:
        return jsonify({"status": "ready", "model_load_time_s": load_time}), 200
    return jsonify({"status": "not ready", "reason": "model not loaded"}), 503

@app.route("/predict", methods=["POST"])
def predict():
    start = time.time()

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key"}), 400

    try:
        features = np.array(data["features"], dtype=float)
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid features: {e}"}), 400

    if features.ndim == 1:
        features = features.reshape(1, -1)

    if features.shape[1] != 4:
        return jsonify({"error": f"Expected 4 features, got {features.shape[1]}"}), 400

    predictions = model.predict(features).tolist()
    probabilities = model.predict_proba(features).tolist()
    latency_ms = (time.time() - start) * 1000

    logger.info(f"Predicted {len(predictions)} samples in {latency_ms:.1f}ms")

    return jsonify({
        "predictions": predictions,
        "probabilities": probabilities,
        "latency_ms": round(latency_ms, 2),
    })

@app.route("/model/info")
def model_info():
    return jsonify({
        "name": "iris-classifier",
        "version": "1.0.0",
        "model_type": type(model).__name__,
        "model_path": MODEL_PATH,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
```

## Gunicorn Configuration

```bash
# 4 workers, 2 threads each — good for CPU-bound ML inference
gunicorn \
  --workers 4 \
  --threads 2 \
  --timeout 60 \
  --bind 0.0.0.0:8080 \
  --access-logfile - \
  "src.app:app"
```

## Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY models/ ./models/
EXPOSE 8080
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8080", "src.app:app"]
```

## Performance Notes

- Model loading: ~50ms for a small sklearn model
- Prediction latency: ~1-2ms per request (single sample)
- Throughput with 4 gunicorn workers: ~2000 req/s for simple models

## Flask vs FastAPI

| Feature | Flask | FastAPI |
|---------|-------|---------|
| Async support | ❌ (sync only) | ✅ Native async |
| Input validation | Manual | ✅ Pydantic |
| Auto docs | ❌ | ✅ OpenAPI/Swagger |
| Performance | Good | Better (async) |
| Learning curve | Low | Low-Medium |
