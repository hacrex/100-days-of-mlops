# Capstone: End-to-End ML System

## Overview

A complete production ML system covering the full lifecycle: data ingestion → feature engineering → training → model registry → serving → monitoring.

## Architecture

```
Raw Data (S3/GCS)
    ↓ DVC
Processed Data
    ↓ Feature Pipeline
Feature Store (Feast)
    ↓ Training Pipeline
MLflow Model Registry
    ↓ CI/CD (GitHub Actions)
Docker Image
    ↓ Kubernetes Deployment
REST API (FastAPI)
    ↓ Prometheus + Grafana
Monitoring Dashboard
```

## Components

| Component | Technology | Day Reference |
|-----------|-----------|---------------|
| Data versioning | DVC | Day 10 |
| Feature store | Feast | Day 41 |
| Experiment tracking | MLflow | Day 20 |
| Model training | scikit-learn | Day 31 |
| Model serving | FastAPI | Day 58 |
| Containerization | Docker | Day 50 |
| Orchestration | Kubernetes | Day 92 |
| Monitoring | Prometheus + Grafana | Day 67 |
| CI/CD | GitHub Actions | Day 76 |

## Project Structure

```
end-to-end-ml-system/
├── data/
│   └── raw/
├── src/
│   ├── data/
│   │   ├── ingest.py
│   │   └── preprocess.py
│   ├── features/
│   │   ├── feature_repo/
│   │   └── pipeline.py
│   ├── training/
│   │   ├── train.py
│   │   └── evaluate.py
│   └── serving/
│       ├── app.py
│       └── schemas.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── .github/
│   └── workflows/
│       └── ml-pipeline.yml
├── docker-compose.yml
├── Dockerfile
├── Makefile
└── requirements.txt
```

## Getting Started

```bash
# 1. Set up environment
make install

# 2. Ingest and version data
make data

# 3. Build features
make features

# 4. Train and register model
make train

# 5. Serve the model
make serve

# 6. Run the full pipeline
make pipeline
```

## Status

⏳ In progress
