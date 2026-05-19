#!/bin/bash
# Day 1 - Python Virtual Environments
# All commands used during this day's practice

# --- Create a virtual environment ---
python3 -m venv .venv

# --- Activate (Linux/macOS) ---
source .venv/bin/activate

# --- Verify the environment ---
which python
python --version
pip --version

# --- Upgrade pip first (good habit) ---
pip install --upgrade pip

# --- Install packages ---
pip install numpy==1.26.4 pandas==2.2.1 scikit-learn==1.4.1.post1

# --- List installed packages ---
pip list

# --- Freeze to requirements.txt ---
pip freeze > requirements.txt

# --- Deactivate ---
deactivate

# --- Recreate from requirements.txt ---
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# --- Check a specific package version ---
python -c "import numpy; print(numpy.__version__)"

# --- Show where a package is installed ---
pip show numpy
