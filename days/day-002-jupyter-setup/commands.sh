<<<<<<< HEAD
#!/bin/bash
# Day 2 - Jupyter Notebook Setup

# --- Install JupyterLab and related tools ---
pip install jupyterlab ipykernel nbconvert nbstripout

# --- Register the venv as a Jupyter kernel ---
python -m ipykernel install --user --name mlops --display-name "Python (mlops)"

# --- List all registered kernels ---
jupyter kernelspec list

# --- Start JupyterLab ---
jupyter lab

# --- Start JupyterLab without opening a browser (for remote/headless) ---
jupyter lab --no-browser --port 8888

# --- Convert notebook to Python script ---
jupyter nbconvert --to script src/exploration.ipynb

# --- Convert notebook to HTML report ---
jupyter nbconvert --to html src/exploration.ipynb

# --- Execute a notebook and save output ---
jupyter nbconvert --to notebook --execute src/exploration.ipynb --output src/exploration_executed.ipynb

# --- Strip outputs from a notebook ---
nbstripout src/exploration.ipynb

# --- Install nbstripout as a git pre-commit filter ---
nbstripout --install

# --- Remove a kernel ---
jupyter kernelspec uninstall mlops
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
