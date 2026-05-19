# Day 4 — Implementation Notes

## What I Did

Created a standard ML project structure from scratch and explored the `src` layout pattern.

## Project Structure Created

```
sample-ml-project/
├── src/
│   └── mlproject/
│       ├── __init__.py
│       ├── data/
│       │   ├── __init__.py
│       │   └── loader.py
│       ├── features/
│       │   ├── __init__.py
│       │   └── engineer.py
│       └── models/
│           ├── __init__.py
│           └── trainer.py
├── notebooks/
│   └── 01-exploration.ipynb
├── tests/
│   └── test_loader.py
├── configs/
│   └── train_config.yaml
├── pyproject.toml
├── requirements.txt
└── Makefile
```

## pyproject.toml

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "mlproject"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "numpy>=1.26",
    "pandas>=2.0",
    "scikit-learn>=1.4",
]

[tool.setuptools.packages.find]
where = ["src"]
```

## Installing in Editable Mode

```bash
pip install -e .
python -c "from mlproject.data.loader import load_data; print('OK')"
```

## Key Insight: src Layout

Without `src` layout:
```python
# This works even without installing the package (bad!)
import mlproject
```

With `src` layout:
```python
# This only works after pip install -e . (good!)
import mlproject
```

The `src` layout forces you to install the package, which means your tests run against the installed version — the same way a user would use it.

## Config File Pattern

```yaml
# configs/train_config.yaml
model:
  type: random_forest
  n_estimators: 100
  max_depth: 5

data:
  train_path: data/processed/train.csv
  test_path: data/processed/test.csv

mlflow:
  experiment_name: day-004-experiment
  tracking_uri: http://localhost:5000
```

Load with:
```python
import yaml
from pathlib import Path

config = yaml.safe_load(Path("configs/train_config.yaml").read_text())
```
