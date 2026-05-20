# Day 5 - Makefile Automation

## Objective

Use a `Makefile` to automate repetitive ML project tasks — environment setup, training, testing, linting, and cleanup — with a single command.

## Background

Makefiles are a simple, universal way to document and automate project workflows. They're language-agnostic, require no extra dependencies, and work on any Unix-like system. In ML projects, they're great for encoding the "how do I run this?" knowledge that otherwise lives only in someone's head.

## Topics Covered

- Makefile syntax: targets, prerequisites, recipes
- `.PHONY` targets for non-file targets
- Variables and pattern rules
- Chaining targets (dependencies)
- A practical ML project Makefile

## Tools Used

- `make` — Build automation tool (pre-installed on Linux/macOS)

## Prerequisites

- Days 1–4 completed

## Setup

```bash
cd days/day-005-makefile-automation
```

## Key Commands

```bash
# Run the default target (usually 'help' or 'all')
make

# Run a specific target
make install
make train
make test
make clean

# Dry run — see what would execute without running it
make -n train

# Override a variable
make train EPOCHS=50

# Run from a different directory
make -C /path/to/project train
```

## Example Makefile

See [src/Makefile](src/Makefile) for the full example.

```makefile
.PHONY: help install lint test train clean

PYTHON := python3
VENV := .venv

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

lint:  ## Run linters
	$(VENV)/bin/ruff check src/
	$(VENV)/bin/black --check src/

test:  ## Run tests
	$(VENV)/bin/pytest tests/ -v

train:  ## Train the model
	$(VENV)/bin/python src/train.py

clean:  ## Remove generated files
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf $(VENV) mlruns/ .pytest_cache/
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- `.PHONY` tells make that a target is not a file — without it, if a file named `clean` exists, `make clean` won't run
- The `##` comment pattern enables self-documenting Makefiles via the `help` target
- Makefile recipes must use tabs, not spaces — a common source of confusing errors
- Variables can be overridden from the command line: `make train MODEL=rf`
- Chaining targets as prerequisites ensures correct ordering: `make deploy` can depend on `make test`

## Common Pitfalls

- Using spaces instead of tabs for recipe indentation — make will fail with a cryptic error
- Not declaring `.PHONY` targets — make may skip them if a file with the same name exists
- Hardcoding paths — use variables so the Makefile works from any directory

## References

- [GNU Make Manual](https://www.gnu.org/software/make/manual/make.html)
- [Makefile Tutorial](https://makefiletutorial.com)

## Next Steps

- Day 6: Pre-commit Hooks — automate code quality checks on every commit
