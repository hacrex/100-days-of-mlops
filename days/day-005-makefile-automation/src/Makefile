.PHONY: help install lint format test train clean

PYTHON   := python3
VENV     := .venv
PIP      := $(VENV)/bin/pip
PYTEST   := $(VENV)/bin/pytest
PYTHON_V := $(VENV)/bin/python

.DEFAULT_GOAL := help

help:  ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Create venv and install dependencies
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip --quiet
	$(PIP) install -r requirements.txt --quiet
	@echo "✅ Environment ready. Run: source $(VENV)/bin/activate"

lint:  ## Run ruff linter
	$(VENV)/bin/ruff check src/ tests/ || true

format:  ## Format code with black and isort
	$(VENV)/bin/black src/ tests/ || true
	$(VENV)/bin/isort src/ tests/ || true

test:  ## Run tests
	$(PYTEST) tests/ -v --tb=short

train:  ## Train the model
	$(PYTHON_V) src/train.py

clean:  ## Remove generated artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf mlruns/ .pytest_cache/ htmlcov/ .coverage
	@echo "✅ Cleaned."
