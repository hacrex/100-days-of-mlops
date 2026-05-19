# Day 41 — Implementation Notes

## What I Did

Initialized a Feast project, defined feature views for a driver stats dataset, materialized features, and fetched them for both training and inference.

## Feast Architecture

```
Offline Store (Parquet/BigQuery/Redshift)
    ↓ feast materialize
Online Store (SQLite/Redis/DynamoDB)
    ↓ get_online_features()
Inference Service
```

## Project Structure After feast init

```
my_feature_repo/
├── feature_repo/
│   ├── feature_store.yaml    # Store configuration
│   ├── example_repo.py       # Example feature definitions
│   └── data/
│       └── driver_stats.parquet
└── README.md
```

## feature_store.yaml

```yaml
project: my_feature_repo
registry: data/registry.db
provider: local
online_store:
  type: sqlite
  path: data/online_store.db
offline_store:
  type: file
entity_key_serialization_version: 2
```

## Training vs Inference Feature Retrieval

### Training (historical features)

```python
from feast import FeatureStore
import pandas as pd
from datetime import datetime

store = FeatureStore(repo_path=".")

# Entity dataframe with timestamps — Feast does point-in-time join
entity_df = pd.DataFrame({
    "driver_id": [1001, 1002, 1003],
    "event_timestamp": [
        datetime(2024, 6, 1),
        datetime(2024, 6, 2),
        datetime(2024, 6, 3),
    ]
})

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
        "driver_hourly_stats:avg_daily_trips",
    ]
).to_df()
```

### Inference (online features)

```python
features = store.get_online_features(
    features=[
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
    ],
    entity_rows=[{"driver_id": 1001}]
).to_dict()
```

## Point-in-Time Join

This is the key feature that prevents training-serving skew. When you request historical features with a timestamp, Feast returns the feature values that were available at that exact point in time — not future values.

```
driver_id | event_timestamp | conv_rate
1001      | 2024-06-01      | 0.72      ← value as of 2024-06-01
1001      | 2024-06-02      | 0.75      ← value as of 2024-06-02
```

## Observations

- The local provider (SQLite + Parquet) is great for development but not production
- For production, use Redis for the online store and BigQuery/Redshift for the offline store
- Feast's Python SDK is clean and well-documented
