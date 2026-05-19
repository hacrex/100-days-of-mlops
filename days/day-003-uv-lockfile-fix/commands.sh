<<<<<<< HEAD
#!/bin/bash
# Day 3 - uv Package Manager & Lockfiles

# --- Install uv ---
pip install uv

# --- Check uv version ---
uv --version

# --- Create a venv with uv ---
uv venv .venv
source .venv/bin/activate

# --- Install packages with uv (much faster than pip) ---
uv pip install numpy pandas scikit-learn

# --- Install from requirements.txt ---
uv pip install -r requirements.txt

# --- Compile a lockfile from requirements.in ---
uv pip compile requirements.in -o requirements.txt

# --- Compile for a specific platform (cross-platform lockfile) ---
uv pip compile requirements.in \
  --platform linux \
  --python-version 3.11 \
  -o requirements-linux.txt

# --- Sync environment to exactly match lockfile (removes extra packages) ---
uv pip sync requirements.txt

# --- Dry run (show what would be installed) ---
uv pip install --dry-run numpy pandas

# --- Check for dependency conflicts ---
uv pip check

# --- List installed packages ---
uv pip list

# --- Show package info ---
uv pip show numpy
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
