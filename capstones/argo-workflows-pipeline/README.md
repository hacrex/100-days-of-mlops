# Capstone: Argo Workflows ML Pipeline

## Overview

A Kubernetes-native ML pipeline using Argo Workflows with DAG orchestration, artifact passing, and conditional deployment based on model quality gates.

## Pipeline DAG

```
prepare-data
    ↓
feature-engineering
    ↓
train-model
    ↓
evaluate-model
    ↓ (if accuracy >= 0.90)
register-model
    ↓
build-image
    ↓
deploy-to-staging
    ↓ (manual approval)
deploy-to-production
```

## Components

| Component | Technology | Day Reference |
|-----------|-----------|---------------|
| Pipeline orchestration | Argo Workflows | Day 85 |
| Container runtime | Kubernetes | Day 92 |
| Artifact storage | MinIO (S3-compatible) | — |
| Model registry | MLflow | Day 20 |
| Serving | Flask/FastAPI | Day 57/58 |

## Project Structure

```
argo-workflows-pipeline/
├── workflows/
│   ├── ml-pipeline.yaml          # Main DAG workflow
│   ├── templates/
│   │   ├── prepare-data.yaml
│   │   ├── train-model.yaml
│   │   └── evaluate-model.yaml
│   └── workflow-template.yaml    # Reusable WorkflowTemplate
├── src/
│   ├── prepare_data.py
│   ├── train.py
│   └── evaluate.py
├── k8s/
│   ├── argo-install.yaml
│   └── minio.yaml
└── Makefile
```

## Getting Started

```bash
# 1. Install Argo Workflows
kubectl apply -f k8s/argo-install.yaml

# 2. Install MinIO for artifact storage
kubectl apply -f k8s/minio.yaml

# 3. Submit the pipeline
argo submit -n argo workflows/ml-pipeline.yaml --watch

# 4. View in the UI
kubectl port-forward -n argo deployment/argo-server 2746:2746
```

## Status

⏳ In progress
