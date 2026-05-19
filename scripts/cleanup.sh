#!/bin/bash
# cleanup.sh — Remove generated artifacts and temporary files

set -euo pipefail

echo "==> Cleaning Python cache files..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.pyo" -delete 2>/dev/null || true
find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
echo "    Done."

echo "==> Cleaning Jupyter checkpoints..."
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true
echo "    Done."

echo "==> Cleaning MLflow artifacts..."
if [ -d "mlruns" ]; then
    rm -rf mlruns/
    echo "    Removed mlruns/"
fi
if [ -d "mlartifacts" ]; then
    rm -rf mlartifacts/
    echo "    Removed mlartifacts/"
fi

echo "==> Cleaning log files..."
find . -type f -name "*.log" -delete 2>/dev/null || true
echo "    Done."

echo "==> Cleaning pytest / coverage artifacts..."
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name ".coverage" -delete 2>/dev/null || true
echo "    Done."

echo ""
echo "✅ Cleanup complete."
echo ""
echo "Note: Virtual environments (.venv/, venv/) were NOT removed."
echo "To also remove the venv, run: rm -rf .venv venv"
