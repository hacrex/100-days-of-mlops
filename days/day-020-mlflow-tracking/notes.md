<<<<<<< HEAD
# Day 20 — Implementation Notes

## What I Did

Set up MLflow tracking, logged a scikit-learn experiment with parameters, metrics, and artifacts, and explored the MLflow UI.

## Training Script

```python
# src/train.py
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# Set the tracking URI (default: ./mlruns)
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("day-020-iris-classification")

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Hyperparameters to try
configs = [
    {"n_estimators": 50, "max_depth": 3},
    {"n_estimators": 100, "max_depth": 5},
    {"n_estimators": 200, "max_depth": None},
]

for config in configs:
    with mlflow.start_run():
        # Log parameters
        mlflow.log_params(config)

        # Train
        model = RandomForestClassifier(**config, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="weighted")

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)

        # Log the model
        mlflow.sklearn.log_model(model, "model")

        print(f"Config: {config} | Accuracy: {accuracy:.4f} | F1: {f1:.4f}")
```

## MLflow Concepts

| Concept | Description |
|---------|-------------|
| Experiment | A named group of runs (e.g., "iris-classification") |
| Run | A single execution with its own params, metrics, artifacts |
| Parameter | Input to the run (e.g., `n_estimators=100`) |
| Metric | Output measurement (e.g., `accuracy=0.97`) |
| Artifact | Files saved during the run (model, plots, data) |
| Tag | Key-value metadata (e.g., `git_commit=abc123`) |

## MLflow UI

After running `mlflow server --port 5000`, the UI at `http://localhost:5000` shows:
- All experiments and runs
- Parameter/metric comparison across runs
- Artifact browser
- Model registry

## Auto-logging

MLflow supports auto-logging for scikit-learn:

```python
mlflow.sklearn.autolog()
# Now all params, metrics, and the model are logged automatically
model.fit(X_train, y_train)
```

## Observations

- The `mlruns/` directory is created automatically when using the default file-based backend
- Auto-logging is convenient but logs too much for production — explicit logging is cleaner
- The MLflow UI's parallel coordinates plot is great for hyperparameter analysis
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
