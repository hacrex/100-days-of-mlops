<<<<<<< HEAD
# Day 57 - Flask Model Serving

## Objective

Wrap a trained ML model in a Flask REST API so it can serve predictions over HTTP.

## Background

Once a model is trained, it needs to be accessible to other systems. A REST API is the most common way to expose ML models — it's language-agnostic, easy to test, and works with any client. Flask is a lightweight Python web framework that's great for building simple model serving APIs.

## Topics Covered

- Building a Flask REST API for model inference
- Request validation and error handling
- Health check and readiness endpoints
- Loading a model at startup (not per-request)
- Dockerizing the Flask app
- Testing the API with curl and Python requests

## Tools Used

- `Flask` — Lightweight Python web framework
- `joblib` — Model loading
- `scikit-learn` — The model being served
- `gunicorn` — Production WSGI server

## Prerequisites

- Days 1–50 completed
- A trained model saved with joblib

## Setup

```bash
cd days/day-057-flask-serving
pip install -r requirements.txt
python src/app.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/ready` | Readiness check (model loaded) |
| POST | `/predict` | Get predictions |
| GET | `/model/info` | Model metadata |

## Example Request

```bash
# Health check
curl http://localhost:8080/health

# Single prediction
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# Batch prediction
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]}'
```

## Flask App

```python
# src/app.py
import joblib
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load model at startup — not per request
model = joblib.load("models/model.joblib")
model_metadata = {"name": "iris-classifier", "version": "1.0.0"}

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/ready")
def ready():
    if model is not None:
        return jsonify({"status": "ready"}), 200
    return jsonify({"status": "not ready"}), 503

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "features" not in data:
        return jsonify({"error": "Missing 'features' in request body"}), 400

    features = np.array(data["features"])
    if features.ndim == 1:
        features = features.reshape(1, -1)

    predictions = model.predict(features).tolist()
    probabilities = model.predict_proba(features).tolist()

    return jsonify({
        "predictions": predictions,
        "probabilities": probabilities,
    })

@app.route("/model/info")
def model_info():
    return jsonify(model_metadata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Load the model once at startup, not inside the prediction function — loading is slow
- Always validate input before passing to the model — bad input causes cryptic errors
- Use `gunicorn` in production, not Flask's built-in server — it's single-threaded and not production-safe
- Return consistent error responses with appropriate HTTP status codes
- Health and readiness endpoints are essential for Kubernetes deployments

## Common Pitfalls

- Running Flask's dev server in production — it's single-threaded and not safe
- Loading the model inside the prediction handler — adds 100ms+ latency per request
- Not handling malformed input — the model will throw an exception and return a 500

## References

- [Flask documentation](https://flask.palletsprojects.com)
- [gunicorn docs](https://gunicorn.org)

## Next Steps

- Day 58: FastAPI Model Serving — async, type-safe alternative to Flask
=======
# Day 57 - Flask Serving

## Objective
Document hands-on implementation and learnings for this MLOps task.

## Topics Covered
- TODO

## Tools Used
- Python
- Docker
- Kubernetes
- MLflow

## Commands

```bash
# Add commands here
```

## Learnings
- TODO

## Screenshots
Add screenshots here.

## References
- Official Documentation
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
