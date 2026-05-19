# Day 4 - ML Project Structure

## Objective

Establish a standard, reproducible directory layout for ML projects that separates concerns and scales from experimentation to production.

## Background

A consistent project structure is one of the most underrated MLOps practices. It makes onboarding faster, CI/CD easier, and the boundary between research and production code clearer. This day covers the `src` layout pattern and how it differs from flat scripts.

## Topics Covered

- The `src` layout vs flat layout
- Separating data, notebooks, source code, and configs
- `pyproject.toml` for project metadata
- Cookiecutter for templating new projects
- What belongs in `src/` vs `notebooks/` vs `scripts/`

## Tools Used

- `cookiecutter` — Project templating tool
- `pyproject.toml` — Modern Python project configuration
- `setuptools` — Package build backend

## Prerequisites

- Days 1–3 completed

## Setup

```bash
cd days/day-004-ml-project-structure
pip install -r requirements.txt
```

## Key Commands

```bash
# Install cookiecutter
pip install cookiecutter

# Create a project from the cookiecutter-data-science template
cookiecutter https://github.com/drivendataorg/cookiecutter-data-science

# Install your own package in editable mode
pip install -e .

# Verify the package is importable
python -c "import mypackage; print('OK')"

# Check project structure
find . -type f | grep -v __pycache__ | grep -v .git | sort
```

## Recommended Project Layout

```
my-ml-project/
├── data/
│   ├── raw/          # Original, immutable data
│   ├── processed/    # Cleaned, transformed data
│   └── features/     # Feature-engineered data
├── models/           # Trained model artifacts
├── notebooks/        # Jupyter notebooks (exploration only)
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── data/     # Data loading and processing
│       ├── features/ # Feature engineering
│       ├── models/   # Model training and evaluation
│       └── serving/  # Inference code
├── tests/
├── configs/          # YAML/JSON configuration files
├── scripts/          # One-off scripts
├── pyproject.toml
├── requirements.txt
├── Makefile
└── README.md
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- The `src` layout prevents accidental imports of your package from the project root — you must install it with `pip install -e .` first
- `data/` should be in `.gitignore` — use DVC to version it instead
- `notebooks/` are for exploration; production code lives in `src/`
- `configs/` keeps hyperparameters and settings out of code — makes experiments reproducible without code changes
- `pyproject.toml` replaces `setup.py` + `setup.cfg` + `requirements.txt` for packages

## Common Pitfalls

- Putting all code in notebooks — hard to test, import, and reuse
- Hardcoding paths — use `pathlib.Path` relative to the project root
- Mixing raw and processed data in the same directory

## References

- [Cookiecutter Data Science](https://drivendataorg.github.io/cookiecutter-data-science)
- [Python src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout)
- [pyproject.toml spec](https://packaging.python.org/en/latest/specifications/pyproject-toml)

## Next Steps

- Day 5: Makefile Automation — automate common project tasks
