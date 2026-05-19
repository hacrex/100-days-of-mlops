# Capstone: ML Observability Stack

## Overview

A production-grade observability stack for ML systems combining metrics, distributed tracing, and structured logging — all deployed on Kubernetes with Helm.

## Stack

| Pillar | Tool | Port |
|--------|------|------|
| Metrics | Prometheus | 9090 |
| Visualization | Grafana | 3000 |
| Tracing | Jaeger | 16686 |
| Log storage | Elasticsearch | 9200 |
| Log processing | Logstash | 5044 |
| Log visualization | Kibana | 5601 |
| Alerting | Alertmanager | 9093 |

## Architecture

```
ML API
├── /metrics endpoint → Prometheus scrapes → Grafana dashboards
├── OpenTelemetry SDK → Jaeger (traces)
└── Structured JSON logs → Logstash → Elasticsearch → Kibana

Prometheus → Alertmanager → PagerDuty/Slack
```

## Grafana Dashboards

1. **ML API Overview** — Request rate, latency, error rate
2. **Model Performance** — Prediction distribution, confidence, drift scores
3. **Infrastructure** — CPU, memory, pod count
4. **SLO Dashboard** — Availability, latency SLOs

## Alerting Rules

```yaml
# High error rate
- alert: HighErrorRate
  expr: rate(ml_api_requests_total{status=~"5.."}[5m]) > 0.01
  for: 5m
  labels:
    severity: critical

# High latency
- alert: HighLatency
  expr: histogram_quantile(0.99, rate(ml_api_request_duration_seconds_bucket[5m])) > 1.0
  for: 5m
  labels:
    severity: warning

# Feature drift detected
- alert: FeatureDrift
  expr: ml_feature_drift_score > 0.2
  for: 1h
  labels:
    severity: warning
```

## Project Structure

```
observability-stack/
├── helm/
│   ├── prometheus/
│   ├── grafana/
│   ├── jaeger/
│   └── elasticsearch/
├── configs/
│   ├── prometheus.yml
│   ├── alerting-rules.yml
│   ├── grafana-dashboards/
│   └── logstash.conf
├── src/
│   └── ml-api/
│       └── app.py              # Fully instrumented ML API
└── docker-compose.yml          # Local development stack
```

## Getting Started

```bash
# Local development
docker compose up -d

# Kubernetes deployment
helm install prometheus prometheus-community/kube-prometheus-stack
helm install jaeger jaegertracing/jaeger
helm install elasticsearch elastic/elasticsearch
helm install kibana elastic/kibana
```

## Status

⏳ In progress
