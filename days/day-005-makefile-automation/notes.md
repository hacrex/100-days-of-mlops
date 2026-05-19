<<<<<<< HEAD
# Day 5 — Implementation Notes

## What I Did

Built a practical Makefile for an ML project covering the full development workflow.

## The Makefile

```makefile
.PHONY: help install lint format test train evaluate clean

PYTHON   := python3
VENV     := .venv
PIP      := $(VENV)/bin/pip
PYTEST   := $(VENV)/bin/pytest
PYTHON_V := $(VENV)/bin/python

# Default target
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
	$(VENV)/bin/ruff check src/ tests/

format:  ## Format code with black and isort
	$(VENV)/bin/black src/ tests/
	$(VENV)/bin/isort src/ tests/

test:  ## Run tests
	$(PYTEST) tests/ -v --tb=short

train:  ## Train the model
	$(PYTHON_V) src/train.py

evaluate:  ## Evaluate the trained model
	$(PYTHON_V) src/evaluate.py

clean:  ## Remove generated artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf mlruns/ .pytest_cache/ htmlcov/ .coverage
	@echo "✅ Cleaned."
```

## Key Observations

### Tab vs Space Issue

This is the #1 Makefile gotcha. The recipe lines MUST start with a tab character, not spaces.

```makefile
# WRONG (spaces)
install:
    pip install -r requirements.txt

# CORRECT (tab)
install:
	pip install -r requirements.txt
```

### Self-documenting Help Target

The `help` target uses `grep` + `awk` to extract `## comments` from target definitions. This means the documentation lives next to the code.

```bash
$ make help
  install              Create venv and install dependencies
  lint                 Run ruff linter
  format               Format code with black and isort
  test                 Run tests
  train                Train the model
  clean                Remove generated artifacts
```

### Dependency Chaining

```makefile
# train depends on install — running 'make train' will run install first if needed
train: install
	$(PYTHON_V) src/train.py
```

## Makefile vs Shell Scripts

| Aspect | Makefile | Shell Script |
|--------|----------|--------------|
| Dependency tracking | ✅ Built-in | ❌ Manual |
| Self-documenting | ✅ Easy | ❌ Harder |
| Incremental builds | ✅ File timestamps | ❌ Manual |
| Portability | ✅ Unix universal | ✅ Unix universal |
| Windows support | ⚠️ Needs make | ✅ Git Bash / WSL |
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
