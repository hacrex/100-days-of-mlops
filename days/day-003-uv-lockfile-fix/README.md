<<<<<<< HEAD
# Day 3 - uv Package Manager & Lockfiles

## Objective

Replace `pip` with `uv` for dramatically faster dependency resolution and installation, and understand how lockfiles ensure reproducible environments.

## Background

`uv` is a Rust-based Python package manager from Astral (the makers of Ruff). It's 10–100x faster than pip for installs and resolution. It also supports lockfiles natively, which is something pip lacks without pip-tools.

## Topics Covered

- Installing and using `uv`
- `uv pip install` vs `pip install`
- `uv pip compile` for generating lockfiles
- `uv pip sync` for reproducible installs
- `uv venv` for creating virtual environments
- When to use `uv` vs `pip` vs `conda`

## Tools Used

- `uv` — Fast Python package manager written in Rust
- `pip-tools` — For comparison (pip-compile / pip-sync)

## Prerequisites

- Day 1 completed (understand venv basics)

## Setup

```bash
# Install uv
pip install uv

cd days/day-003-uv-lockfile-fix
```

## Key Commands

```bash
# Install uv
pip install uv

# Create a venv with uv
uv venv .venv

# Install a package with uv (much faster than pip)
uv pip install numpy pandas scikit-learn

# Install from requirements.txt
uv pip install -r requirements.txt

# Compile a lockfile from requirements.in
uv pip compile requirements.in -o requirements.txt

# Sync environment to exactly match lockfile
uv pip sync requirements.txt

# Show what uv would install without actually installing
uv pip install --dry-run numpy

# Check for dependency conflicts
uv pip check
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- `uv` resolves and installs packages in parallel — a full ML stack that takes 60s with pip takes ~5s with uv
- `uv pip sync` is stricter than `pip install -r` — it removes packages not in the lockfile, giving you a clean environment
- `uv pip compile` is equivalent to `pip-compile` from pip-tools — it takes loose constraints and produces a fully pinned lockfile
- The lockfile pattern: maintain `requirements.in` (your direct deps) and commit `requirements.txt` (the compiled lockfile)

## Common Pitfalls

- `uv pip sync` removes packages not in the lockfile — don't run it in a shared environment
- `uv` doesn't yet support all pip features (e.g., editable installs in some edge cases)

## References

- [uv documentation](https://docs.astral.sh/uv)
- [uv GitHub](https://github.com/astral-sh/uv)
- [pip-tools](https://pip-tools.readthedocs.io)

## Next Steps

- Day 4: ML Project Structure — organizing a real ML codebase
=======
# Day 3 - Uv Lockfile Fix

## Objective
Document hands-on implementation and learnings for this MLOps task.

## Topics Covered
- TODO

## Tools Used
- Python
- Docker
- Kubernetes
- MLflow

## Commands

```bash
# Add commands here
```

## Learnings
- TODO

## Screenshots
Add screenshots here.

## References
- Official Documentation
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
