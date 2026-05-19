#!/bin/bash
# Day 20 - MLflow Experiment Tracking

# --- Install MLflow ---
pip install mlflow==2.11.3 scikit-learn==1.4.1.post1

# --- Start the MLflow tracking server (UI) ---
mlflow server --host 0.0.0.0 --port 5000

# --- Start with a specific backend store and artifact store ---
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlartifacts \
  --host 0.0.0.0 \
  --port 5000

# --- Run the training script ---
python src/train.py

# --- List experiments ---
mlflow experiments list

# --- Create a new experiment ---
mlflow experiments create --experiment-name "day-020-experiment"

# --- List runs in an experiment ---
mlflow runs list --experiment-id 1

# --- Get details of a specific run ---
mlflow runs describe --run-id <run_id>

# --- Serve a logged model ---
mlflow models serve -m "runs:/<run_id>/model" --port 8080

# --- Serve from the model registry ---
mlflow models serve -m "models:/MyModel/Production" --port 8080

# --- Build a Docker image for a model ---
mlflow models build-docker -m "runs:/<run_id>/model" -n my-model-image
