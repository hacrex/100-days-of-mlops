# Day 1 - Python Virtual Environments

## Objective

Set up isolated Python environments using `venv` so that project dependencies don't conflict with each other or the system Python.

## Background

Every ML project has its own set of dependencies — different versions of numpy, scikit-learn, or TensorFlow. Without isolation, installing one project's packages can break another. Virtual environments solve this by giving each project its own Python interpreter and package directory.

## Topics Covered

- Why virtual environments matter in ML projects
- Creating and activating a `venv`
- Installing and pinning dependencies with `pip`
- Generating `requirements.txt` for reproducibility
- The difference between `venv`, `virtualenv`, `conda`, and `uv`

## Tools Used

- `venv` — Python's built-in virtual environment module
- `pip` — Package installer
- `pip-tools` — For compiling pinned requirements

## Prerequisites

- Python 3.10+ installed
- Basic command line familiarity

## Setup

```bash
cd days/day-001-python-venv
```

## Key Commands

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate it (Linux/macOS)
source .venv/bin/activate

# Activate it (Windows)
.venv\Scripts\activate

# Verify you're using the venv's Python
which python   # should point to .venv/bin/python

# Install a package
pip install numpy==1.26.4

# Freeze current environment to requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Deactivate the environment
deactivate

# Remove the environment entirely
rm -rf .venv
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- `venv` creates a lightweight copy of the Python interpreter — it doesn't copy all packages, just the interpreter and pip
- Always add `venv/`, `.venv/` to `.gitignore` — never commit the environment itself
- `pip freeze` captures exact versions including transitive dependencies, which is good for reproducibility but can make upgrades harder
- `pip-tools` (`pip-compile`) is better for large projects: you maintain a `requirements.in` with loose constraints and it generates a fully pinned `requirements.txt`
- For ML projects, prefer pinning major + minor versions (e.g., `numpy==1.26.*`) rather than exact patch versions to allow security patches

## Common Pitfalls

- Forgetting to activate the venv before installing packages — packages end up in the system Python
- Committing the `venv/` folder to git — it's large, platform-specific, and unnecessary
- Using `pip freeze` in a shared environment — you'll capture unrelated packages

## References

- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [pip-tools](https://pip-tools.readthedocs.io)
- [Real Python: Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

## Next Steps

- Day 2: Jupyter Notebook Setup — running notebooks inside a venv
