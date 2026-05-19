<<<<<<< HEAD
# Day 41 - Feast Feature Store

## Objective

Set up Feast as a feature store to manage, serve, and reuse ML features consistently between training and inference.

## Background

The "training-serving skew" problem is one of the most common causes of ML model degradation in production: features are computed differently during training vs inference. A feature store solves this by providing a single source of truth for feature definitions and serving them consistently to both training pipelines and production models.

## Topics Covered

- Feature store concepts: entities, feature views, online store, offline store
- Initializing a Feast project
- Defining feature views in Python
- `feast apply` — registering features
- `feast materialize` — populating the online store
- Fetching historical features for training
- Fetching online features for inference

## Tools Used

- `feast` — Open-source feature store

## Prerequisites

- Days 1–31 completed

## Setup

```bash
cd days/day-041-feast-feature-store
pip install -r requirements.txt

# Initialize a Feast project
feast init my_feature_repo
cd my_feature_repo/feature_repo
feast apply
```

## Key Commands

```bash
# Initialize a new Feast project
feast init my_feature_repo

# Apply feature definitions to the registry
feast apply

# Materialize features to the online store
feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")

# List feature views
feast feature-views list

# List entities
feast entities list
```

## Example Feature Definition

```python
# feature_repo/features.py
from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64

# Define the entity (the "key" for feature lookup)
driver = Entity(name="driver_id", description="Driver ID")

# Define the data source
driver_stats_source = FileSource(
    path="data/driver_stats.parquet",
    timestamp_field="event_timestamp",
)

# Define the feature view
driver_stats_fv = FeatureView(
    name="driver_hourly_stats",
    entities=[driver],
    ttl=timedelta(days=1),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Int64),
    ],
    source=driver_stats_source,
)
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Feast separates the **offline store** (historical features for training) from the **online store** (low-latency features for inference)
- `feast materialize` copies features from the offline store to the online store — this is the "materialization" step
- The `entity_df` for historical feature retrieval must have an `event_timestamp` column — Feast does a point-in-time join to prevent leakage
- Feature definitions are Python code — they're versioned in git alongside your model code

## Common Pitfalls

- Not running `feast apply` after changing feature definitions — the registry won't reflect your changes
- Forgetting to materialize before serving — the online store will be empty
- Using `event_timestamp` in the future for historical features — Feast will return no data

## References

- [Feast documentation](https://docs.feast.dev)
- [Feast quickstart](https://docs.feast.dev/getting-started/quickstart)

## Next Steps

- Day 42: Feast Online Store — Redis and DynamoDB backends
=======
# Day 41 - Feast Feature Store

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
