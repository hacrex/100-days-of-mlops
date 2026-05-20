# Day 2 - Jupyter Notebook Setup

## Objective

Configure JupyterLab inside a virtual environment with the correct kernel, useful extensions, and best practices for ML experimentation.

## Background

Jupyter notebooks are the standard interactive environment for ML exploration. But running Jupyter correctly — with the right kernel pointing to your project's venv, not the system Python — requires a bit of setup. This day covers that setup plus productivity extensions.

## Topics Covered

- Installing JupyterLab inside a venv
- Registering a venv as a Jupyter kernel
- Useful JupyterLab extensions for ML
- Notebook best practices (cell ordering, outputs, version control)
- Converting notebooks to scripts with `nbconvert`

## Tools Used

- `JupyterLab` — Next-gen notebook interface
- `ipykernel` — Registers Python environments as Jupyter kernels
- `nbconvert` — Converts notebooks to scripts, HTML, PDF
- `nbstripout` — Strips notebook outputs before committing to git

## Prerequisites

- Day 1 completed (virtual environment set up)

## Setup

```bash
cd days/day-002-jupyter-setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Key Commands

```bash
# Install JupyterLab and ipykernel
pip install jupyterlab ipykernel

# Register the current venv as a kernel named "mlops"
python -m ipykernel install --user --name mlops --display-name "Python (mlops)"

# List registered kernels
jupyter kernelspec list

# Start JupyterLab
jupyter lab

# Start classic Jupyter Notebook
jupyter notebook

# Convert a notebook to a Python script
jupyter nbconvert --to script notebook.ipynb

# Convert a notebook to HTML
jupyter nbconvert --to html notebook.ipynb

# Strip outputs from a notebook (before committing)
nbstripout notebook.ipynb

# Remove a kernel
jupyter kernelspec uninstall mlops
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Always register your venv as a kernel — otherwise Jupyter uses the system Python and your installed packages won't be available
- Add `*.ipynb` outputs to `.gitignore` or use `nbstripout` as a pre-commit hook to avoid committing large diffs
- JupyterLab extensions are installed via `pip install` (for modern extensions) — no separate `jupyter labextension install` needed for most
- Restart the kernel after installing new packages in a notebook cell

## Common Pitfalls

- Running `jupyter lab` without activating the venv — you get the system Jupyter, not your project's
- Committing notebooks with outputs — causes huge diffs and merge conflicts
- Not restarting the kernel after `pip install` in a cell — the new package isn't loaded

## References

- [JupyterLab docs](https://jupyterlab.readthedocs.io)
- [ipykernel docs](https://ipykernel.readthedocs.io)
- [nbstripout](https://github.com/kynan/nbstripout)

## Next Steps

- Day 3: uv Package Manager — faster alternative to pip
