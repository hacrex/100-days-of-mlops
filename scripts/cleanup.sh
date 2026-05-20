#!/bin/bash
# Cleanup generated artifacts

set -e

echo "🧹 Cleaning up generated artifacts..."

# Remove Python cache
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true

# Remove virtual environments
rm -rf .venv 2>/dev/null || true
find . -type d -name ".venv" -exec rm -rf {} + 2>/dev/null || true

# Remove Jupyter checkpoints
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true

# Remove MLflow runs (optional, comment out to keep)
# rm -rf mlruns 2>/dev/null || true
# find . -type d -name "mlruns" -exec rm -rf {} + 2>/dev/null || true

# Remove DVC cache (optional, comment out to keep)
# rm -rf .dvc/cache 2>/dev/null || true

# Remove build artifacts
rm -rf build/ dist/ *.egg-info 2>/dev/null || true
find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true

# Remove pytest cache
rm -rf .pytest_cache 2>/dev/null || true
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

# Remove mypy cache
rm -rf .mypy_cache 2>/dev/null || true
find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true

# Remove black cache
rm -rf .black_cache 2>/dev/null || true

echo "✅ Cleanup complete!"
