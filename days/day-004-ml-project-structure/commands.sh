#!/bin/bash
# Day 4 - ML Project Structure

# --- Install cookiecutter ---
pip install cookiecutter

# --- Create a project from cookiecutter-data-science ---
cookiecutter https://github.com/drivendataorg/cookiecutter-data-science

# --- Create the src layout manually ---
mkdir -p src/mlproject/{data,features,models,serving}
touch src/mlproject/__init__.py
touch src/mlproject/data/__init__.py
touch src/mlproject/features/__init__.py
touch src/mlproject/models/__init__.py

# --- Create supporting directories ---
mkdir -p notebooks tests configs data/{raw,processed,features} models

# --- Install the package in editable mode ---
pip install -e .

# --- Verify the package is importable ---
python -c "import mlproject; print('Package installed successfully')"

# --- Check the installed package location ---
pip show mlproject

# --- List the project structure ---
find . -type f | grep -v __pycache__ | grep -v .git | grep -v .venv | sort
