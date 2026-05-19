#!/bin/bash
# Day 50 - Docker Training Environment

# --- Build the training image ---
docker build -t ml-training:latest .

# --- Build with a specific tag ---
docker build -t ml-training:v1.0.0 .

# --- Build with build args ---
docker build \
  --build-arg PYTHON_VERSION=3.11 \
  --build-arg MODEL_TYPE=random_forest \
  -t ml-training:latest .

# --- Run training in a container ---
docker run --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/models:/app/models \
  ml-training:latest

# --- Run with environment variables ---
docker run --rm \
  -e MLFLOW_TRACKING_URI=http://host.docker.internal:5000 \
  -e N_ESTIMATORS=200 \
  -v $(pwd)/data:/app/data \
  ml-training:latest

# --- Run interactively for debugging ---
docker run -it --rm \
  -v $(pwd)/data:/app/data \
  ml-training:latest bash

# --- Check image size ---
docker images ml-training

# --- Inspect image layers ---
docker history ml-training:latest

# --- Push to a registry ---
docker tag ml-training:latest your-registry/ml-training:latest
docker push your-registry/ml-training:latest

# --- Clean up ---
docker rmi ml-training:latest
docker system prune -f
