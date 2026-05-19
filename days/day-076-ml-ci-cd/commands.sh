#!/bin/bash
# Day 76 - ML CI/CD Pipelines

# --- Run the full pipeline locally (simulating CI) ---
pip install -r requirements.txt
python -m pytest tests/ -v
python src/train.py
python src/evaluate.py

# --- Check if metrics meet threshold ---
python -c "
import json
metrics = json.load(open('metrics.json'))
threshold = 0.90
accuracy = metrics['accuracy']
if accuracy < threshold:
    print(f'FAIL: accuracy {accuracy:.4f} < threshold {threshold}')
    exit(1)
print(f'PASS: accuracy {accuracy:.4f} >= threshold {threshold}')
"

# --- Lint and type check ---
ruff check src/
mypy src/ --ignore-missing-imports

# --- Build Docker image with git SHA tag ---
GIT_SHA=$(git rev-parse --short HEAD)
docker build -t ml-api:${GIT_SHA} .

# --- Run tests in Docker ---
docker run --rm ml-api:${GIT_SHA} pytest tests/ -v

# --- Trigger a GitHub Actions workflow manually ---
gh workflow run ml-pipeline.yml

# --- View workflow runs ---
gh run list --workflow=ml-pipeline.yml

# --- View a specific run's logs ---
gh run view <run-id> --log
