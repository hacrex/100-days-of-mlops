#!/bin/bash
# Install all dependencies for 100 Days of MLOps

set -e

echo "📦 Installing all dependencies..."

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Install global tools
echo "Installing global tools..."
uv pip install \
    jupyterlab \
    jupyter \
    ipykernel \
    black \
    isort \
    mypy \
    pre-commit \
    pytest \
    pylint

echo "✅ Global tools installed"

# Install day-specific dependencies
echo "Installing day-specific dependencies..."

days_dir="days"
for day_folder in "$days_dir"/day-*/; do
    if [ -d "$day_folder" ]; then
        req_file="$day_folder/requirements.txt"
        if [ -f "$req_file" ]; then
            echo "  Installing dependencies for $(basename $day_folder)..."
            uv pip install -r "$req_file"
        fi
    fi
done

echo ""
echo "✅ All dependencies installed!"
