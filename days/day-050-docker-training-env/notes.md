# Day 50 — Implementation Notes

## What I Did

Built a Docker image for an ML training job, experimented with multi-stage builds, and connected the container to a local MLflow server.

## Dockerfile (Multi-stage)

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim AS runtime
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src/ ./src/
COPY configs/ ./configs/
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "src/train.py"]
```

## Image Size Comparison

| Base Image | Size |
|-----------|------|
| python:3.11 | ~920MB |
| python:3.11-slim | ~150MB |
| python:3.11-alpine | ~60MB (but harder to build ML deps) |
| Multi-stage slim | ~200MB (with ML deps) |

## Layer Caching Strategy

```dockerfile
# WRONG — requirements.txt changes invalidate the COPY src/ cache
COPY . .
RUN pip install -r requirements.txt

# CORRECT — requirements.txt is copied first; src/ changes don't invalidate pip cache
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ ./src/
```

## Connecting to MLflow

From inside a container, `localhost` refers to the container itself, not the host machine.

```bash
# On Docker Desktop (Mac/Windows)
docker run -e MLFLOW_TRACKING_URI=http://host.docker.internal:5000 ml-training

# On Linux
docker run --network host -e MLFLOW_TRACKING_URI=http://localhost:5000 ml-training

# Using Docker Compose (recommended)
# docker-compose.yml sets up a shared network
```

## .dockerignore

```
.git/
.venv/
venv/
__pycache__/
*.pyc
data/
models/
mlruns/
*.log
.env
notebooks/
tests/
```

## Security: Non-root User

```dockerfile
# Add a non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser
WORKDIR /home/appuser/app
```

## Observations

- Multi-stage builds reduced the image from 850MB to 210MB
- Layer caching is critical for fast CI builds — always copy requirements before source code
- The `.dockerignore` file is as important as `.gitignore` — without it, the build context is huge
