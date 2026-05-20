# Day 76 — Implementation Notes

## What I Did

Built a GitHub Actions CI/CD pipeline for an ML project that runs tests, trains a model, evaluates it against a threshold, and deploys if it passes.

## GitHub Actions Workflow

```yaml
# .github/workflows/ml-pipeline.yml
name: ML CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v --tb=short

  train-and-evaluate:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"
      - run: pip install -r requirements.txt
      - name: Train model
        run: python src/train.py
      - name: Evaluate model
        run: python src/evaluate.py
      - name: Check accuracy threshold
        run: |
          ACCURACY=$(python -c "import json; d=json.load(open('metrics.json')); print(d['accuracy'])")
          python -c "
          accuracy = float('$ACCURACY')
          threshold = 0.90
          if accuracy < threshold:
              print(f'FAIL: accuracy {accuracy:.4f} < threshold {threshold}')
              exit(1)
          print(f'PASS: accuracy {accuracy:.4f} >= threshold {threshold}')
          "
      - name: Upload model artifact
        uses: actions/upload-artifact@v4
        with:
          name: trained-model
          path: models/

  deploy:
    needs: train-and-evaluate
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Download model artifact
        uses: actions/download-artifact@v4
        with:
          name: trained-model
          path: models/
      - name: Build Docker image
        run: docker build -t ml-api:${{ github.sha }} .
      - name: Push to registry
        run: |
          echo "${{ secrets.REGISTRY_PASSWORD }}" | docker login -u "${{ secrets.REGISTRY_USERNAME }}" --password-stdin
          docker push ml-api:${{ github.sha }}
```

## Model Validation Gate

```python
# src/evaluate.py
import json
import sys
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

model = joblib.load("models/model.joblib")
X_test = pd.read_parquet("data/processed/test.parquet")
y_test = X_test.pop("label")

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

metrics = {
    "accuracy": accuracy_score(y_test, y_pred),
    "f1_score": f1_score(y_test, y_pred, average="weighted"),
    "roc_auc": roc_auc_score(y_test, y_proba),
}

Path("metrics.json").write_text(json.dumps(metrics, indent=2))
print(json.dumps(metrics, indent=2))
```

## CI/CD Stages for ML

```
Code Push
    ↓
Lint & Type Check (ruff, mypy)
    ↓
Unit Tests (pytest)
    ↓
Data Validation (great_expectations)
    ↓
Model Training
    ↓
Model Evaluation (accuracy >= threshold)
    ↓
Build Docker Image
    ↓
Push to Registry
    ↓
Deploy to Staging
    ↓
Integration Tests
    ↓
Deploy to Production
```

## Observations

- GitHub Actions caches pip dependencies between runs — speeds up CI significantly
- The model validation gate is the key MLOps addition over standard CI/CD
- Storing metrics as JSON artifacts makes it easy to compare across runs
- Using `github.sha` as the image tag ensures every commit has a unique, traceable image
