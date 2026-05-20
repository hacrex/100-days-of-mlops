# Day 2 — Implementation Notes

## What I Did

Set up JupyterLab inside the Day 1 virtual environment, registered it as a kernel, and explored notebook best practices for ML projects.

## Step-by-Step

### 1. Install JupyterLab

```bash
source .venv/bin/activate
pip install jupyterlab==4.1.5 ipykernel==6.29.3 nbconvert==7.16.3 nbstripout==0.7.1
```

### 2. Register the kernel

```bash
python -m ipykernel install --user --name mlops-day2 --display-name "Python (mlops)"
```

Verify:
```bash
jupyter kernelspec list
# Available kernels:
#   mlops-day2    /home/user/.local/share/jupyter/kernels/mlops-day2
#   python3       /usr/share/jupyter/kernels/python3
```

### 3. Start JupyterLab

```bash
jupyter lab --no-browser --port 8888
```

Then open `http://localhost:8888` in the browser.

### 4. Set up nbstripout as a pre-commit hook

```bash
nbstripout --install
```

This adds a git filter that strips outputs before every commit.

## Observations

- The kernel registration is per-user (stored in `~/.local/share/jupyter/kernels/`), not per-project. This means the kernel persists even after deleting the venv — you need to manually uninstall it.
- JupyterLab 4.x has a much better UI than classic Jupyter Notebook
- `nbconvert --to script` is useful for turning exploratory notebooks into production scripts

## Notebook Best Practices Learned

1. Keep notebooks linear — cells should run top-to-bottom without errors
2. Use markdown cells to document intent, not just code
3. Restart & Run All before committing to verify the notebook is reproducible
4. Strip outputs before committing (use nbstripout)
5. Move reusable code to `src/` modules; notebooks should be thin wrappers

## Questions / Follow-ups

- How to run notebooks in CI? → `jupyter nbconvert --to notebook --execute notebook.ipynb`
- How to parameterize notebooks? → Papermill (Day 21 territory)
