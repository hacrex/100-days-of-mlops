#!/bin/bash
# Day 100 - Observability Capstone

# --- Start the full observability stack ---
docker compose up -d

# --- Check all services are healthy ---
curl http://localhost:9090/-/healthy   # Prometheus
curl http://localhost:3000/api/health  # Grafana
curl http://localhost:16686/           # Jaeger
curl http://localhost:9200/_cluster/health  # Elasticsearch

# --- Install Python dependencies ---
pip install -r requirements.txt

# --- Run the instrumented ML API ---
python src/app.py

# --- Generate some traffic ---
for i in $(seq 1 100); do
  curl -s -X POST http://localhost:8080/predict \
    -H "Content-Type: application/json" \
    -d '{"features": [5.1, 3.5, 1.4, 0.2]}' > /dev/null
done

# --- Check metrics ---
curl http://localhost:8080/metrics | grep ml_

# --- Query Prometheus ---
curl 'http://localhost:9090/api/v1/query?query=rate(ml_api_requests_total[5m])'

# --- Check Jaeger for traces ---
curl 'http://localhost:16686/api/services'

# --- Check Elasticsearch for logs ---
curl 'http://localhost:9200/ml-logs-*/_search?pretty&size=5'

# --- Run drift detection ---
python src/drift_check.py

# --- Stop everything ---
docker compose down
