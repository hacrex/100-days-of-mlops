<<<<<<< HEAD
# Day 20 - MLflow Experiment Tracking

## Objective

Track ML experiments with MLflow — logging parameters, metrics, and model artifacts — so that runs are reproducible and comparable.

## Background

Without experiment tracking, ML development is chaotic: you run a script, tweak a hyperparameter, run it again, and quickly lose track of which configuration produced which result. MLflow solves this by recording every run with its inputs (parameters), outputs (metrics), and artifacts (models, plots).

## Topics Covered

- MLflow concepts: experiments, runs, parameters, metrics, artifacts
- Starting the MLflow tracking server
- Logging with `mlflow.log_param`, `mlflow.log_metric`, `mlflow.log_artifact`
- Auto-logging with `mlflow.sklearn.autolog()`
- Comparing runs in the MLflow UI
- The MLflow Model Registry

## Tools Used

- `mlflow` — Experiment tracking, model registry, and serving
- `scikit-learn` — ML framework for the example model

## Prerequisites

- Days 1–10 completed
- Python virtual environment active

## Setup

```bash
cd days/day-020-mlflow-tracking
pip install -r requirements.txt

# Start the MLflow UI
mlflow server --host 0.0.0.0 --port 5000
```

Then open `http://localhost:5000` in your browser.

## Key Commands

```bash
# Start MLflow server
mlflow server --host 0.0.0.0 --port 5000

# Run the training script
python src/train.py

# List all experiments
mlflow experiments list

# List runs in an experiment
mlflow runs list --experiment-id 1

# Serve a model from a run
mlflow models serve -m "runs:/<run_id>/model" --port 8080

# Test the served model
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"dataframe_split": {"columns": ["f1","f2","f3","f4"], "data": [[5.1,3.5,1.4,0.2]]}}'
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- Every `with mlflow.start_run():` block creates a new run with a unique ID
- Parameters are logged once per run; metrics can be logged multiple times (e.g., per epoch)
- `mlflow.sklearn.autolog()` automatically logs params, metrics, and the model — great for quick experiments
- The MLflow UI's "Compare" feature lets you plot metrics across runs side-by-side
- The Model Registry adds staging/production lifecycle management on top of runs

## Common Pitfalls

- Not setting `mlflow.set_experiment()` — all runs go to the "Default" experiment
- Logging metrics inside a loop without a `step` parameter — you lose the time dimension
- Forgetting to end a run — use `with mlflow.start_run():` context manager, not `mlflow.start_run()` + `mlflow.end_run()`

## References

- [MLflow documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)

## Next Steps

- Day 21: MLflow Projects — packaging experiments for reproducibility
=======
# Day 20 - Mlflow Tracking

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
