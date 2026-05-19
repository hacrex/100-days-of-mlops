<<<<<<< HEAD
# Day 100 — Implementation Notes

## What I Built

A complete observability stack for an ML API combining Prometheus metrics, Jaeger distributed tracing, and ELK structured logging — all instrumented via OpenTelemetry.

## The Three Pillars

### 1. Metrics (Prometheus + Grafana)

What: Numeric measurements over time
When to use: Alerting, dashboards, SLOs
Example: `request_rate`, `p99_latency`, `prediction_confidence`

### 2. Traces (Jaeger + OpenTelemetry)

What: End-to-end request flows across services
When to use: Debugging latency, understanding request paths
Example: A trace showing: Flask handler → feature lookup → model inference → response

### 3. Logs (ELK Stack)

What: Timestamped text records of events
When to use: Debugging specific errors, audit trails
Example: `{"level": "ERROR", "trace_id": "abc123", "message": "Model prediction failed"}`

## Correlating the Three Pillars

The key is injecting the trace ID into logs:

```python
import logging
from opentelemetry import trace

class TraceIdFilter(logging.Filter):
    def filter(self, record):
        span = trace.get_current_span()
        if span.is_recording():
            ctx = span.get_span_context()
            record.trace_id = format(ctx.trace_id, "032x")
            record.span_id = format(ctx.span_id, "016x")
        else:
            record.trace_id = "0" * 32
            record.span_id = "0" * 16
        return True

# Now logs include trace_id — you can jump from a log to the trace in Jaeger
```

## ML Drift Monitoring with Evidently

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def check_drift(reference_data, current_data):
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference_data, current_data=current_data)
    result = report.as_dict()

    drift_detected = result["metrics"][0]["result"]["dataset_drift"]
    drift_share = result["metrics"][0]["result"]["share_of_drifted_columns"]

    # Update Prometheus gauge
    FEATURE_DRIFT_SCORE.labels(feature_name="overall").set(drift_share)

    return drift_detected, drift_share
```

## Docker Compose Stack

```yaml
version: "3.8"
services:
  prometheus:
    image: prom/prometheus:v2.51.0
    ports: ["9090:9090"]
    volumes:
      - ./configs/prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:10.4.0
    ports: ["3000:3000"]
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

  jaeger:
    image: jaegertracing/all-in-one:1.56
    ports:
      - "6831:6831/udp"   # Thrift compact
      - "16686:16686"     # UI

  elasticsearch:
    image: elasticsearch:8.13.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports: ["9200:9200"]

  kibana:
    image: kibana:8.13.0
    ports: ["5601:5601"]
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
```

## 100-Day Reflection

Starting from `python3 -m venv .venv` and ending with a full observability stack — the journey covers the complete MLOps lifecycle. The key insight: MLOps is DevOps applied to ML, with extra concerns around data versioning, experiment tracking, model validation, and ML-specific monitoring.

The most impactful skills:
1. **DVC** — Data versioning is as important as code versioning
2. **MLflow** — Experiment tracking prevents "which config was that again?"
3. **Docker** — Reproducibility across environments
4. **Kubernetes** — The platform everything runs on
5. **Observability** — You can't improve what you can't measure
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
