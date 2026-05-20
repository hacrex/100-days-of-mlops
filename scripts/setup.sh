#!/bin/bash
# Bootstrap development environment for 100 Days of MLOps

set -e

echo "🚀 Setting up 100 Days of MLOps environment..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

echo "✅ Python version: $(python3 --version)"

# Install uv if not present
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

echo "✅ uv version: $(uv --version)"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🐍 Creating virtual environment..."
    uv venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install base dependencies
echo "📥 Installing base dependencies..."
uv pip install -r requirements.txt 2>/dev/null || echo "No global requirements.txt found"

# Install pre-commit hooks
if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
    echo "🔧 Installing pre-commit hooks..."
    pre-commit install
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Activate environment: source .venv/bin/activate"
echo "  2. Navigate to a day folder: cd days/day-001-python-venv"
echo "  3. Read the README and start learning!"
