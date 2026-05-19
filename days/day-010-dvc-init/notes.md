<<<<<<< HEAD
# Day 10 — Implementation Notes

## What I Did

Initialized DVC in a git repo, tracked a CSV dataset, configured a local remote, and practiced the push/pull workflow.

## What dvc init Creates

```
.dvc/
├── .gitignore       # Ignores cache/ and tmp/
├── config           # DVC configuration
└── tmp/             # Temporary files
```

## The .dvc Pointer File

After `dvc add data/raw/train.csv`:

```yaml
# data/raw/train.csv.dvc
outs:
- md5: a1b2c3d4e5f6...
  size: 1024
  path: train.csv
```

This tiny file is what gets committed to git. The actual data lives in `.dvc/cache/` locally and in the remote.

## DVC Cache Structure

```
.dvc/cache/
└── files/
    └── md5/
        └── a1/
            └── b2c3d4e5f6...  # The actual file content
```

DVC uses content-addressable storage — files are stored by their MD5 hash.

## Workflow Summary

```
Developer A                    Developer B
-----------                    -----------
dvc add data/train.csv
git commit train.csv.dvc
dvc push
git push
                               git pull
                               dvc pull
                               # Now has the same data
```

## DVC vs git-lfs

| Feature | DVC | git-lfs |
|---------|-----|---------|
| Storage backends | S3, GCS, Azure, SSH, local | GitHub/GitLab LFS servers |
| Pipeline support | ✅ Yes | ❌ No |
| Experiment tracking | ✅ Yes | ❌ No |
| Cost | Free (bring your own storage) | Paid above limits |
| ML-specific features | ✅ Many | ❌ None |

## Observations

- The `.dvc` file is tiny (~100 bytes) — git handles it perfectly
- DVC's cache deduplicates files by content — if you add the same file twice, it's only stored once
- `dvc status` is like `git status` for data — it shows what's changed vs the last commit
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
