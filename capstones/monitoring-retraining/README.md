# Capstone: Monitoring & Auto-Retraining

## Overview

A system that continuously monitors a deployed ML model for data drift and prediction drift, and automatically triggers retraining when drift exceeds a threshold.

## Architecture

```
Production Traffic
    ↓
ML API (Flask + Prometheus)
    ↓ logs predictions + features
Feature Log Store (Parquet/S3)
    ↓ scheduled drift check (every 6h)
Drift Detector (Evidently AI)
    ↓ if drift detected
Argo Events trigger
    ↓
Retraining Pipeline (Argo Workflows)
    ↓ if accuracy >= threshold
Model Registry (MLflow)
    ↓
Rolling Deployment (Kubernetes)
```

## Components

| Component | Technology | Day Reference |
|-----------|-----------|---------------|
| Drift detection | Evidently AI | Day 75 |
| Metrics | Prometheus + Grafana | Day 67 |
| Event triggering | Argo Events | Day 87 |
| Retraining pipeline | Argo Workflows | Day 85 |
| Model registry | MLflow | Day 20 |
| Deployment | Kubernetes | Day 92 |

## Drift Detection Logic

```python
# Checks run every 6 hours
# If PSI > 0.2 for any feature → trigger retraining
# If prediction distribution shift > 0.1 → trigger retraining
# If accuracy on labeled sample < 0.85 → trigger retraining
```

## Project Structure

```
monitoring-retraining/
├── src/
│   ├── serving/
│   │   └── app.py              # ML API with prediction logging
│   ├── monitoring/
│   │   ├── drift_detector.py   # Evidently-based drift detection
│   │   └── metrics.py          # Prometheus metrics
│   └── retraining/
│       └── pipeline.py         # Retraining pipeline
├── workflows/
│   ├── drift-check.yaml        # Argo CronWorkflow
│   └── retrain.yaml            # Retraining workflow
├── configs/
│   ├── drift_thresholds.yaml
│   └── prometheus.yml
└── docker-compose.yml
```

## Status

⏳ In progress
