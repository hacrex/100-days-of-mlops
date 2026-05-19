<<<<<<< HEAD
# Day 10 - DVC Init & Data Versioning

## Objective

Initialize DVC in an ML project and version a dataset so that data changes are tracked alongside code changes in git.

## Background

Git is great for code but terrible for large files. DVC (Data Version Control) solves this by storing large files (datasets, models) in a remote storage (S3, GCS, local) and tracking only small pointer files (`.dvc` files) in git. This gives you git-like semantics for data.

## Topics Covered

- `dvc init` and what it creates
- Adding files to DVC tracking with `dvc add`
- DVC remote storage configuration
- `dvc push` and `dvc pull`
- The `.dvc` pointer file format
- DVC vs git-lfs

## Tools Used

- `dvc` — Data Version Control
- `dvc-s3` — S3 remote storage plugin (optional)

## Prerequisites

- Days 1–5 completed
- Git repository initialized

## Setup

```bash
cd days/day-010-dvc-init
pip install -r requirements.txt
git init  # if not already in a git repo
```

## Key Commands

```bash
# Initialize DVC in a git repo
dvc init

# Add a data file to DVC tracking
dvc add data/raw/train.csv

# Commit the .dvc pointer file to git
git add data/raw/train.csv.dvc data/.gitignore
git commit -m "Track train.csv with DVC"

# Configure a local remote (for testing)
dvc remote add -d localremote /tmp/dvc-storage

# Configure an S3 remote
dvc remote add -d s3remote s3://my-bucket/dvc-storage

# Push data to remote
dvc push

# Pull data from remote
dvc pull

# Check DVC status
dvc status

# Show what DVC is tracking
dvc list .

# Reproduce a pipeline
dvc repro
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- `dvc init` creates a `.dvc/` directory (similar to `.git/`) — commit it to git
- `dvc add data/train.csv` creates `data/train.csv.dvc` (a small pointer file) and adds `data/train.csv` to `.gitignore`
- The `.dvc` file contains an MD5 hash of the file — DVC uses this to find the actual data in the cache
- DVC cache lives in `.dvc/cache/` by default — don't commit it to git
- `dvc push` uploads data to the remote; `dvc pull` downloads it — just like `git push/pull`

## Common Pitfalls

- Running `dvc add` on a file that's already tracked by git — you need to `git rm --cached` it first
- Forgetting to `dvc push` after adding new data — collaborators can't pull it
- Committing `.dvc/cache/` to git — it can be huge

## References

- [DVC documentation](https://dvc.org/doc)
- [DVC Get Started](https://dvc.org/doc/start)
- [DVC vs git-lfs](https://dvc.org/doc/user-guide/related-technologies#git-lfs)

## Next Steps

- Day 11: DVC Pipelines — define reproducible ML pipelines with `dvc run`
=======
# Day 10 - Dvc Init

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
