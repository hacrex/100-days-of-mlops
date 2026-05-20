# Makefile for End-to-End ML System

.PHONY: install data features train evaluate serve pipeline clean docker-build docker-push deploy

# Configuration
PYTHON := python3
PIP := pip
MLFLOW_TRACKING_URI := http://localhost:5000
FEAST_SERVING_URL := localhost:6566

install:
@echo "Installing dependencies..."
$(PIP) install -r requirements.txt

data:
@echo "Ingesting and preprocessing data..."
$(PYTHON) src/data/ingest.py
$(PYTHON) src/data/preprocess.py

features:
@echo "Building feature pipeline..."
$(PYTHON) src/features/pipeline.py

train:
@echo "Training model and registering to MLflow..."
$(PYTHON) src/training/train.py

evaluate:
@echo "Evaluating model performance..."
$(PYTHON) src/training/evaluate.py

serve:
@echo "Starting model serving API..."
uvicorn src.serving.app:app --host 0.0.0.0 --port 8000 --reload

pipeline: data features train evaluate
@echo "Full ML pipeline completed!"

clean:
@echo "Cleaning up artifacts..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
rm -rf mlruns/ .pytest_cache/ .mypy_cache/

docker-build:
@echo "Building Docker image..."
docker build -t end-to-end-ml-system:latest .

docker-push:
@echo "Pushing Docker image to registry..."
docker push end-to-end-ml-system:latest

deploy:
@echo "Deploying to Kubernetes..."
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

test:
@echo "Running tests..."
pytest tests/ -v --cov=src

lint:
@echo "Running linters..."
black src/ --check
isort src/ --check
mypy src/

format:
@echo "Formatting code..."
black src/
isort src/
