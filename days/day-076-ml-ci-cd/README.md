<<<<<<< HEAD
# Day 76 - ML CI/CD Pipelines

## Objective

Build a CI/CD pipeline for an ML project that automatically trains, evaluates, and deploys a model when code is pushed — with a quality gate that blocks deployment if the model doesn't meet accuracy thresholds.

## Background

Standard CI/CD (lint → test → deploy) isn't enough for ML. You also need to train the model, evaluate it, and only deploy if it meets quality criteria. This "model validation gate" is what separates ML CI/CD from regular CI/CD.

## Topics Covered

- GitHub Actions workflow for ML
- Model training and evaluation in CI
- Model validation gates (accuracy thresholds)
- Artifact storage (trained models, metrics)
- Docker image building and pushing in CI
- Caching pip dependencies in CI

## Tools Used

- `GitHub Actions` — CI/CD platform
- `pytest` — Testing framework
- `Docker` — Container building
- `gh` — GitHub CLI

## Prerequisites

- Days 1–67 completed
- GitHub repository with Actions enabled

## Setup

```bash
cd days/day-076-ml-ci-cd
pip install -r requirements.txt
```

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
      - run: pytest tests/ -v

  train-and-validate:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"
      - run: pip install -r requirements.txt
      - run: python src/train.py
      - run: python src/evaluate.py
      - name: Validate model quality
        run: python src/validate_model.py --min-accuracy 0.90
      - uses: actions/upload-artifact@v4
        with:
          name: trained-model
          path: models/

  deploy:
    needs: train-and-validate
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with:
          name: trained-model
          path: models/
      - run: docker build -t ml-api:${{ github.sha }} .
      - run: docker push ml-api:${{ github.sha }}
```

## Model Validation Gate

```python
# src/validate_model.py
import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--min-accuracy", type=float, default=0.90)
args = parser.parse_args()

metrics = json.load(open("metrics.json"))
accuracy = metrics["accuracy"]

if accuracy < args.min_accuracy:
    print(f"❌ Model failed validation: accuracy={accuracy:.4f} < threshold={args.min_accuracy}")
    sys.exit(1)

print(f"✅ Model passed validation: accuracy={accuracy:.4f} >= threshold={args.min_accuracy}")
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- The model validation gate is the key difference between ML CI/CD and regular CI/CD
- Use `actions/cache` or `setup-python`'s built-in cache for pip — saves 2-3 minutes per run
- Store trained models as GitHub Actions artifacts — they're available to downstream jobs
- Tag Docker images with `github.sha` for full traceability
- Run tests before training — no point training if the code is broken

## Common Pitfalls

- Not caching pip dependencies — CI takes 5+ minutes just to install packages
- Training on CI with large datasets — use a small representative sample for CI
- Not storing metrics as artifacts — you lose the ability to compare runs

## References

- [GitHub Actions docs](https://docs.github.com/en/actions)
- [GitHub Actions for ML](https://github.com/iterative/cml)

## Next Steps

- Day 77: GitHub Actions for ML — advanced patterns with CML and DVC
=======
# Day 76 - Ml Ci Cd

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
