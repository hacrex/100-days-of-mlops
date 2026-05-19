"""
Day 67 - Prometheus + Grafana Monitoring
Flask ML API instrumented with Prometheus metrics.
"""

import logging
import os
import time

import joblib
import numpy as np
from flask import Flask, jsonify, request
from prometheus_client import Counter, Gauge, Histogram, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# --- Prometheus Metrics ---

REQUEST_COUNT = Counter(
    "ml_api_requests_total",
    "Total number of requests",
    ["method", "endpoint", "http_status"],
)

REQUEST_LATENCY = Histogram(
    "ml_api_request_duration_seconds",
    "Request latency in seconds",
    ["endpoint"],
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5],
)

PREDICTION_CONFIDENCE = Gauge(
    "ml_model_prediction_confidence",
    "Average prediction confidence of the last request",
)

PREDICTION_CLASS_COUNT = Counter(
    "ml_predictions_by_class_total",
    "Prediction counts by class label",
    ["predicted_class"],
)

# --- Model loading ---
MODEL_PATH = os.getenv("MODEL_PATH", "models/iris_pipeline.joblib")
model = None

try:
    model = joblib.load(MODEL_PATH)
    logger.info(f"Model loaded from {MODEL_PATH}")
except FileNotFoundError:
    logger.warning(f"Model not found at {MODEL_PATH} — predictions will fail")


# --- Endpoints ---

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
    start = time.time()

    if model is None:
        REQUEST_COUNT.labels(method="POST", endpoint="/predict", http_status="503").inc()
        return jsonify({"error": "Model not loaded"}), 503

    data = request.get_json(silent=True)
    if not data or "features" not in data:
        REQUEST_COUNT.labels(method="POST", endpoint="/predict", http_status="400").inc()
        return jsonify({"error": "Missing 'features' in request body"}), 400

    try:
        features = np.array(data["features"], dtype=float)
        if features.ndim == 1:
            features = features.reshape(1, -1)
    except (ValueError, TypeError) as exc:
        REQUEST_COUNT.labels(method="POST", endpoint="/predict", http_status="400").inc()
        return jsonify({"error": f"Invalid features: {exc}"}), 400

    predictions = model.predict(features).tolist()
    probabilities = model.predict_proba(features).tolist()
    latency = time.time() - start

    # Record metrics
    REQUEST_LATENCY.labels(endpoint="/predict").observe(latency)
    REQUEST_COUNT.labels(method="POST", endpoint="/predict", http_status="200").inc()

    avg_confidence = float(np.mean([max(p) for p in probabilities]))
    PREDICTION_CONFIDENCE.set(avg_confidence)

    for pred in predictions:
        PREDICTION_CLASS_COUNT.labels(predicted_class=str(pred)).inc()

    return jsonify({
        "predictions": predictions,
        "probabilities": probabilities,
        "latency_ms": round(latency * 1000, 2),
    })


# Expose /metrics endpoint via Prometheus WSGI middleware
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    "/metrics": make_wsgi_app()
})

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("0.0.0.0", 8080, app.wsgi_app)
