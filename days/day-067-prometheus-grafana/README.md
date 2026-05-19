<<<<<<< HEAD
# Day 67 - Prometheus + Grafana Monitoring

## Objective

Instrument an ML serving API with Prometheus metrics and visualize them in Grafana dashboards.

## Background

Monitoring is non-negotiable for production ML systems. You need to know: Is the service up? How many requests per second? What's the p99 latency? Are predictions drifting? Prometheus collects these metrics; Grafana visualizes them.

## Topics Covered

- Prometheus architecture: scraping, time series, PromQL
- Instrumenting a Python app with `prometheus-client`
- The four metric types: Counter, Gauge, Histogram, Summary
- Writing a `prometheus.yml` scrape config
- Running Prometheus + Grafana with Docker Compose
- Building a Grafana dashboard for ML metrics

## Tools Used

- `Prometheus` — Metrics collection and storage
- `Grafana` — Metrics visualization
- `prometheus-client` — Python instrumentation library

## Prerequisites

- Days 1–57 completed
- Docker and Docker Compose installed

## Setup

```bash
cd days/day-067-prometheus-grafana
docker compose up -d
pip install -r requirements.txt
python src/app.py
```

Then open:
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (admin/admin)

## Docker Compose

```yaml
# docker-compose.yml
version: "3.8"
services:
  prometheus:
    image: prom/prometheus:v2.51.0
    ports:
      - "9090:9090"
    volumes:
      - ./configs/prometheus.yml:/etc/prometheus/prometheus.yml
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.retention.time=15d"

  grafana:
    image: grafana/grafana:10.4.0
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana

volumes:
  grafana-data:
```

## Prometheus Scrape Config

```yaml
# configs/prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "ml-api"
    static_configs:
      - targets: ["host.docker.internal:8080"]
```

## Python Instrumentation

```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Counters — only go up
REQUEST_COUNT = Counter(
    "ml_api_requests_total",
    "Total number of prediction requests",
    ["method", "endpoint", "status"]
)

# Histograms — track distributions (latency, request size)
REQUEST_LATENCY = Histogram(
    "ml_api_request_duration_seconds",
    "Request latency in seconds",
    ["endpoint"],
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
)

# Gauges — can go up and down
MODEL_CONFIDENCE = Gauge(
    "ml_model_prediction_confidence",
    "Average prediction confidence of the last batch"
)

# Usage
with REQUEST_LATENCY.labels(endpoint="/predict").time():
    result = model.predict(features)
    REQUEST_COUNT.labels(method="POST", endpoint="/predict", status="200").inc()
```

## Key PromQL Queries

```promql
# Request rate (per second, 5-minute window)
rate(ml_api_requests_total[5m])

# p99 latency
histogram_quantile(0.99, rate(ml_api_request_duration_seconds_bucket[5m]))

# Error rate
rate(ml_api_requests_total{status=~"5.."}[5m]) / rate(ml_api_requests_total[5m])

# Average confidence
avg(ml_model_prediction_confidence)
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Prometheus **pulls** metrics from targets (scraping) — your app exposes a `/metrics` endpoint
- Use `Histogram` for latency, not `Summary` — histograms can be aggregated across instances
- Label cardinality matters — don't use high-cardinality labels like user IDs
- Grafana dashboards can be exported as JSON and committed to git

## Common Pitfalls

- Using `Summary` instead of `Histogram` for latency — summaries can't be aggregated
- High-cardinality labels (e.g., `user_id`) — creates millions of time series and kills Prometheus
- Not setting retention time — Prometheus disk usage grows unbounded

## References

- [Prometheus docs](https://prometheus.io/docs)
- [prometheus-client Python](https://github.com/prometheus/client_python)
- [Grafana docs](https://grafana.com/docs)

## Next Steps

- Day 68: Custom Prometheus Metrics — advanced instrumentation patterns
=======
# Day 67 - Prometheus Grafana

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
