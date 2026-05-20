# Day 100 - Observability Capstone

## Objective

Build a complete observability stack for an ML system — combining metrics (Prometheus + Grafana), distributed tracing (Jaeger + OpenTelemetry), and structured logging (ELK stack) into a unified observability platform.

## Background

Observability is the ability to understand the internal state of a system from its external outputs. For ML systems, this means knowing not just "is the service up?" but "are predictions drifting?", "which requests are slow?", and "what happened during that incident at 2am?". The three pillars of observability are metrics, traces, and logs.

## Topics Covered

- The three pillars of observability: metrics, traces, logs
- OpenTelemetry for unified instrumentation
- Distributed tracing with Jaeger
- Structured logging with the ELK stack
- Correlating traces, metrics, and logs
- ML-specific observability: prediction drift, feature drift, model confidence
- Building a unified Grafana dashboard

## Tools Used

- `Prometheus` — Metrics collection
- `Grafana` — Visualization
- `OpenTelemetry` — Unified instrumentation SDK
- `Jaeger` — Distributed tracing
- `Elasticsearch` — Log storage
- `Logstash` — Log processing
- `Kibana` — Log visualization
- `Evidently AI` — ML-specific drift monitoring

## Prerequisites

- All 99 previous days completed
- Docker Compose installed

## Setup

```bash
cd days/day-100-observability-capstone
docker compose up -d
pip install -r requirements.txt
python src/app.py
```

Services:
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`
- Jaeger: `http://localhost:16686`
- Kibana: `http://localhost:5601`

## Architecture

```
ML API (Flask + OpenTelemetry)
    │
    ├── Metrics → Prometheus → Grafana
    ├── Traces  → Jaeger
    └── Logs    → Logstash → Elasticsearch → Kibana
```

## OpenTelemetry Instrumentation

```python
# src/telemetry.py
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

def setup_telemetry(app):
    # Configure Jaeger exporter
    jaeger_exporter = JaegerExporter(
        agent_host_name="localhost",
        agent_port=6831,
    )

    provider = TracerProvider()
    provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))
    trace.set_tracer_provider(provider)

    # Auto-instrument Flask and requests
    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()

    return trace.get_tracer(__name__)
```

## ML-Specific Metrics

```python
from prometheus_client import Histogram, Counter, Gauge

# Prediction distribution
PREDICTION_DISTRIBUTION = Counter(
    "ml_predictions_total",
    "Prediction counts by class",
    ["predicted_class"]
)

# Model confidence
CONFIDENCE_HISTOGRAM = Histogram(
    "ml_prediction_confidence",
    "Distribution of prediction confidence scores",
    buckets=[0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99, 1.0]
)

# Feature drift (updated by a background job)
FEATURE_DRIFT_SCORE = Gauge(
    "ml_feature_drift_score",
    "PSI drift score for each feature",
    ["feature_name"]
)
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- OpenTelemetry provides a single SDK for all three pillars — you instrument once and export to any backend
- Trace IDs can be injected into logs, enabling correlation between traces and logs
- ML-specific metrics (prediction distribution, confidence, drift) are as important as infrastructure metrics
- Grafana can query Prometheus, Jaeger, and Elasticsearch — a single pane of glass

## What I Built Over 100 Days

| Phase | Days | Skills |
|-------|------|--------|
| Environment | 1–10 | Python, venv, uv, DVC |
| Experiment Tracking | 11–30 | MLflow, W&B, Optuna |
| Training Pipelines | 31–49 | scikit-learn, Feast |
| Containerization | 50–66 | Docker, Flask, FastAPI |
| Monitoring | 67–75 | Prometheus, Grafana |
| CI/CD | 76–84 | GitHub Actions, ArgoCD |
| Orchestration | 85–91 | Argo Workflows, Kubeflow |
| Kubernetes | 92–100 | K8s, HPA, Observability |

## References

- [OpenTelemetry Python](https://opentelemetry-python.readthedocs.io)
- [Jaeger docs](https://www.jaegertracing.io/docs)
- [Evidently AI](https://docs.evidentlyai.com)
- [Grafana Unified Observability](https://grafana.com/solutions/observability)
