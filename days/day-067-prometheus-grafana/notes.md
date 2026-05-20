# Day 67 — Implementation Notes

## What I Did

Instrumented a Flask ML API with Prometheus metrics, ran Prometheus + Grafana via Docker Compose, and built a dashboard showing request rate, latency, and model confidence.

## Metric Types Cheat Sheet

| Type | Use Case | Example |
|------|----------|---------|
| Counter | Things that only increase | Total requests, errors |
| Gauge | Things that go up and down | Active connections, queue size |
| Histogram | Distributions with buckets | Request latency, payload size |
| Summary | Distributions with quantiles | Same as histogram but can't aggregate |

## Instrumented Flask App

```python
from prometheus_client import Counter, Histogram, Gauge, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

REQUEST_COUNT = Counter(
    "ml_api_requests_total", "Total requests",
    ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "ml_api_request_duration_seconds", "Request latency",
    ["endpoint"]
)
PREDICTION_CONFIDENCE = Gauge(
    "ml_model_avg_confidence", "Average prediction confidence"
)

@app.route("/predict", methods=["POST"])
def predict():
    start = time.time()
    # ... prediction logic ...
    latency = time.time() - start

    REQUEST_LATENCY.labels(endpoint="/predict").observe(latency)
    REQUEST_COUNT.labels(method="POST", endpoint="/predict", http_status="200").inc()
    PREDICTION_CONFIDENCE.set(float(np.max(probabilities)))

    return jsonify(result)

# Expose /metrics endpoint
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    "/metrics": make_wsgi_app()
})
```

## Grafana Dashboard Panels

1. **Request Rate** — `rate(ml_api_requests_total[5m])`
2. **p50/p95/p99 Latency** — `histogram_quantile(0.99, rate(ml_api_request_duration_seconds_bucket[5m]))`
3. **Error Rate** — `rate(ml_api_requests_total{http_status=~"5.."}[5m])`
4. **Model Confidence** — `ml_model_avg_confidence`
5. **Requests by Status** — `sum by (http_status) (rate(ml_api_requests_total[5m]))`

## Prometheus Scrape Config

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: "ml-api"
    metrics_path: "/metrics"
    static_configs:
      - targets: ["host.docker.internal:8080"]
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
```

## Observations

- The `/metrics` endpoint returns text in Prometheus exposition format — easy to read manually
- Grafana's "Explore" tab is great for ad-hoc PromQL queries
- Setting up alerting rules in Prometheus is straightforward — just YAML
- The `histogram_quantile` function is the key to SLO monitoring
