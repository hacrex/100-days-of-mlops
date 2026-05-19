#!/bin/bash
# Day 57 - Flask Model Serving

# --- Install dependencies ---
pip install flask gunicorn joblib scikit-learn

# --- Run the Flask dev server ---
python src/app.py

# --- Run with gunicorn (production) ---
gunicorn --workers 4 --bind 0.0.0.0:8080 "src.app:app"

# --- Test the health endpoint ---
curl http://localhost:8080/health

# --- Test the readiness endpoint ---
curl http://localhost:8080/ready

# --- Test a single prediction ---
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'

# --- Test batch prediction ---
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]}'

# --- Get model info ---
curl http://localhost:8080/model/info

# --- Build and run in Docker ---
docker build -t flask-model-server:latest .
docker run -p 8080:8080 flask-model-server:latest

# --- Load test with wrk ---
wrk -t4 -c100 -d30s -s post.lua http://localhost:8080/predict
