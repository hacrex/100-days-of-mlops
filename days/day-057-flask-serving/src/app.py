"""
Day 57 - Flask Model Serving
A production-ready Flask API for serving an ML model.
"""

import logging
import os
import time
from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, request

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# --- Model loading ---
MODEL_PATH = os.getenv("MODEL_PATH", "models/iris_pipeline.joblib")
model = None
model_load_time: float | None = None


def load_model() -> None:
    global model, model_load_time
    start = time.time()
    model_path = Path(MODEL_PATH)
    if not model_path.exists():
        logger.warning(f"Model file not found at {MODEL_PATH}")
        return
    model = joblib.load(model_path)
    model_load_time = time.time() - start
    logger.info(f"Model loaded in {model_load_time:.3f}s from {MODEL_PATH}")


load_model()

# --- Endpoints ---

@app.route("/health")
def health():
    """Liveness probe — always returns 200 if the process is running."""
    return jsonify({"status": "healthy", "timestamp": time.time()}), 200


@app.route("/ready")
def ready():
    """Readiness probe — returns 503 if the model isn't loaded yet."""
    if model is not None:
        return jsonify({
            "status": "ready",
            "model_load_time_s": model_load_time,
        }), 200
    return jsonify({"status": "not ready", "reason": "model not loaded"}), 503


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict endpoint.

    Request body:
        {"features": [f1, f2, f3, f4]}           # single sample
        {"features": [[f1, f2, f3, f4], ...]}     # batch

    Response:
        {"predictions": [...], "probabilities": [...], "latency_ms": ...}
    """
    start = time.time()

    if model is None:
        return jsonify({"error": "Model not loaded"}), 503

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    if "features" not in data:
        return jsonify({"error": "Missing 'features' key in request body"}), 400

    try:
        features = np.array(data["features"], dtype=float)
    except (ValueError, TypeError) as exc:
        return jsonify({"error": f"Invalid features format: {exc}"}), 400

    if features.ndim == 1:
        features = features.reshape(1, -1)

    if features.shape[1] != 4:
        return jsonify({
            "error": f"Expected 4 features per sample, got {features.shape[1]}"
        }), 400

    predictions = model.predict(features).tolist()
    probabilities = model.predict_proba(features).tolist()
    latency_ms = (time.time() - start) * 1000

    logger.info(
        f"Predicted {len(predictions)} sample(s) in {latency_ms:.1f}ms"
    )

    return jsonify({
        "predictions": predictions,
        "probabilities": probabilities,
        "latency_ms": round(latency_ms, 2),
    })


@app.route("/model/info")
def model_info():
    """Return metadata about the loaded model."""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 503
    return jsonify({
        "name": "iris-classifier",
        "version": "1.0.0",
        "model_type": type(model).__name__,
        "model_path": MODEL_PATH,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
