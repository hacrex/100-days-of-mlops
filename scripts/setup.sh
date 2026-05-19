#!/bin/bash
# setup.sh — Bootstrap the development environment for 100-days-of-mlops

set -euo pipefail

PYTHON_MIN_VERSION="3.10"

echo "==> Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "    Found Python $python_version"

echo "==> Creating virtual environment..."
python3 -m venv .venv
echo "    Virtual environment created at .venv/"

echo "==> Activating virtual environment..."
# shellcheck disable=SC1091
source .venv/bin/activate

echo "==> Upgrading pip..."
pip install --upgrade pip --quiet

echo "==> Installing base tools..."
pip install --quiet \
    black \
    isort \
    ruff \
    mypy \
    pre-commit \
    ipykernel \
    jupyterlab

echo "==> Setting up pre-commit hooks (if .pre-commit-config.yaml exists)..."
if [ -f ".pre-commit-config.yaml" ]; then
    pre-commit install
    echo "    Pre-commit hooks installed."
else
    echo "    No .pre-commit-config.yaml found, skipping."
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "    source .venv/bin/activate"
echo ""
echo "To start working on a specific day:"
echo "    cd days/day-001-python-venv"
echo "    pip install -r requirements.txt"
