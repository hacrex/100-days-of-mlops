<<<<<<< HEAD
# Day 50 - Docker Training Environment

## Objective

Package an ML training job in a Docker container so that it runs identically on any machine — local, CI, or cloud.

## Background

"It works on my machine" is the enemy of reproducible ML. Docker solves this by packaging the code, dependencies, and runtime into a single image. For ML training, this means the same Python version, the same library versions, and the same system libraries — everywhere.

## Topics Covered

- Writing a `Dockerfile` for ML training
- Multi-stage builds to keep images small
- Mounting data volumes vs baking data into the image
- Passing hyperparameters via environment variables
- Connecting to MLflow from inside a container
- Best practices for ML Docker images

## Tools Used

- `Docker` — Container runtime
- `python:3.11-slim` — Base image

## Prerequisites

- Days 1–41 completed
- Docker installed and running

## Setup

```bash
cd days/day-050-docker-training-env
docker build -t ml-training:latest .
```

## Dockerfile

```dockerfile
# Stage 1: Build dependencies
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime image
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy source code
COPY src/ ./src/
COPY configs/ ./configs/

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Default command
CMD ["python", "src/train.py"]
```

## Key Commands

```bash
# Build the image
docker build -t ml-training:latest .

# Run training (mount data and models directories)
docker run --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/models:/app/models \
  -e MLFLOW_TRACKING_URI=http://host.docker.internal:5000 \
  ml-training:latest

# Debug interactively
docker run -it --rm ml-training:latest bash

# Check image size
docker images ml-training

# Inspect layers
docker history ml-training:latest
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Use `python:3.11-slim` not `python:3.11` — the slim image is ~150MB vs ~900MB
- Multi-stage builds keep the final image small — build tools aren't needed at runtime
- Mount data with `-v` rather than `COPY`ing it into the image — data changes frequently, images should be immutable
- Use `--no-cache-dir` with pip to avoid storing the pip cache in the image layer
- `host.docker.internal` resolves to the host machine from inside a container (on Docker Desktop)

## Common Pitfalls

- Running as root inside the container — add a non-root user for security
- Copying `.git/`, `venv/`, or `data/` into the image — use `.dockerignore`
- Not pinning the base image tag — `python:3.11-slim` can change; use `python:3.11.9-slim` for reproducibility

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
```

## References

- [Docker best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Python Docker images](https://hub.docker.com/_/python)

## Next Steps

- Day 51: Multi-stage Docker Builds — advanced build patterns
=======
# Day 50 - Docker Training Env

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
