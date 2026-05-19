<<<<<<< HEAD
#!/bin/bash
# Day 67 - Prometheus + Grafana Monitoring

# --- Start Prometheus and Grafana with Docker Compose ---
docker compose up -d

# --- Check Prometheus is running ---
curl http://localhost:9090/-/healthy

# --- Check Grafana is running ---
curl http://localhost:3000/api/health

# --- Query Prometheus via API ---
curl 'http://localhost:9090/api/v1/query?query=up'

# --- Query a range of data ---
curl 'http://localhost:9090/api/v1/query_range?query=rate(http_requests_total[5m])&start=2024-01-01T00:00:00Z&end=2024-01-01T01:00:00Z&step=60'

# --- Run the instrumented Flask app ---
pip install prometheus-client flask
python src/app.py

# --- Check the /metrics endpoint ---
curl http://localhost:8080/metrics

# --- Reload Prometheus config without restart ---
curl -X POST http://localhost:9090/-/reload

# --- Check Prometheus targets ---
curl http://localhost:9090/api/v1/targets

# --- Check Prometheus rules ---
curl http://localhost:9090/api/v1/rules

# --- Stop everything ---
docker compose down
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
