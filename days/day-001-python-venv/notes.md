# Day 1 — Implementation Notes

## What I Did

Created a virtual environment for a sample ML project and practiced the full lifecycle: create → activate → install → freeze → deactivate → recreate from requirements.

## Environment Details

- Python version: 3.11.x
- OS: Linux/macOS (commands differ slightly on Windows)

## Step-by-Step

### 1. Create the environment

```bash
python3 -m venv .venv
```

This creates a `.venv/` directory with:
- `bin/` (or `Scripts/` on Windows) — Python interpreter and pip
- `lib/` — installed packages
- `pyvenv.cfg` — configuration file

### 2. Activate and verify

```bash
source .venv/bin/activate
which python   # → .venv/bin/python
python --version
pip --version
```

### 3. Install packages

```bash
pip install numpy pandas scikit-learn
```

### 4. Freeze dependencies

```bash
pip freeze > requirements.txt
cat requirements.txt
```

Output looks like:
```
joblib==1.3.2
numpy==1.26.4
pandas==2.2.1
python-dateutil==2.9.0
pytz==2024.1
scikit-learn==1.4.1.post1
scipy==1.12.0
six==1.16.0
threadpoolctl==3.3.0
tzdata==2024.1
```

### 5. Recreate from scratch

```bash
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Observations

- The `.venv/` directory is ~50MB for a basic ML stack — definitely don't commit it
- `pip freeze` captures transitive deps (e.g., `joblib` is a dep of scikit-learn, not something I installed directly)
- On macOS with Homebrew Python, `python3` and `python` may point to different things — always check with `which`

## Questions / Follow-ups

- How does `uv` compare to `pip` for speed? (Day 3 will cover this)
- What's the best way to manage multiple Python versions? → `pyenv`
- Should I use `requirements.txt` or `pyproject.toml`? → For simple projects, `requirements.txt` is fine; for packages, use `pyproject.toml`
