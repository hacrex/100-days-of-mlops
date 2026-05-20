# Day 31 - Scikit-learn Training Pipeline

## Objective

Build a complete, production-ready scikit-learn training pipeline using `Pipeline` and `ColumnTransformer` to handle preprocessing and model training in a single, serializable object.

## Background

A common mistake in ML is fitting preprocessing steps (scalers, encoders) on the full dataset before splitting, which leaks information from the test set. scikit-learn's `Pipeline` solves this by chaining preprocessing and modeling steps so that fitting only happens on training data.

## Topics Covered

- `sklearn.pipeline.Pipeline` for chaining steps
- `ColumnTransformer` for handling mixed feature types
- `StandardScaler`, `OneHotEncoder`, `SimpleImputer`
- Cross-validation with `cross_val_score`
- Saving and loading pipelines with `joblib`
- Integrating with MLflow

## Tools Used

- `scikit-learn` — ML framework
- `pandas` — Data manipulation
- `joblib` — Model serialization
- `mlflow` — Experiment tracking

## Prerequisites

- Days 1–20 completed

## Setup

```bash
cd days/day-031-scikit-training
pip install -r requirements.txt
```

## Key Commands

```bash
# Run the training pipeline
python src/train.py

# Evaluate the saved model
python src/evaluate.py

# Run with MLflow tracking
mlflow server --port 5000 &
python src/train.py
```

## Example Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier

numeric_features = ["age", "income", "score"]
categorical_features = ["city", "category"]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features),
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
])

# Fit on training data only
pipeline.fit(X_train, y_train)

# Predict — preprocessing is applied automatically
y_pred = pipeline.predict(X_test)

# Save the entire pipeline (preprocessor + model)
import joblib
joblib.dump(pipeline, "models/pipeline.joblib")
```

## Implementation Notes

See [notes.md](notes.md) for detailed implementation notes.

## Key Learnings

- `Pipeline` prevents data leakage — `fit_transform` is only called on training data during cross-validation
- `ColumnTransformer` handles different preprocessing for numeric vs categorical features in one step
- `joblib.dump(pipeline, ...)` saves the entire pipeline including fitted transformers — no need to save preprocessing separately
- `pipeline.predict(X_new)` applies all preprocessing steps automatically — no manual preprocessing at inference time

## Common Pitfalls

- Fitting the scaler on the full dataset before splitting — this leaks test set statistics into training
- Forgetting `handle_unknown="ignore"` in `OneHotEncoder` — will fail on unseen categories at inference
- Not using a Pipeline — you have to manually apply preprocessing at inference time and it's easy to get wrong

## References

- [scikit-learn Pipeline docs](https://scikit-learn.org/stable/modules/pipeline.html)
- [ColumnTransformer docs](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)

## Next Steps

- Day 32: Pipelines & ColumnTransformer — advanced pipeline patterns
