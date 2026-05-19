<<<<<<< HEAD
#!/bin/bash
# Day 41 - Feast Feature Store

# --- Install Feast ---
pip install feast==0.38.0

# --- Initialize a new Feast project ---
feast init my_feature_repo
cd my_feature_repo

# --- Inspect the generated structure ---
ls -la feature_repo/

# --- Apply feature definitions to the registry ---
cd feature_repo
feast apply

# --- Materialize features to the online store ---
feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")

# --- Materialize a specific time range ---
feast materialize 2024-01-01T00:00:00 2024-12-31T23:59:59

# --- Fetch online features (for inference) ---
python -c "
from feast import FeatureStore
store = FeatureStore(repo_path='.')
features = store.get_online_features(
    features=['driver_hourly_stats:conv_rate', 'driver_hourly_stats:acc_rate'],
    entity_rows=[{'driver_id': 1001}, {'driver_id': 1002}]
).to_dict()
print(features)
"

# --- Fetch historical features (for training) ---
python -c "
import pandas as pd
from feast import FeatureStore
from datetime import datetime

store = FeatureStore(repo_path='.')
entity_df = pd.DataFrame({
    'driver_id': [1001, 1002, 1003],
    'event_timestamp': [datetime(2024, 1, 1)] * 3
})
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=['driver_hourly_stats:conv_rate', 'driver_hourly_stats:acc_rate']
).to_df()
print(training_df)
"

# --- List all feature views ---
feast feature-views list

# --- List all entities ---
feast entities list

# --- Tear down the feature store ---
feast teardown
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
