"""
Day 31 - Scikit-learn Training Pipeline
Full Pipeline with ColumnTransformer, cross-validation, and MLflow logging.
"""

import json
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

MODELS_DIR = Path("models")
MODELS_DIR.mkdir(exist_ok=True)


def build_pipeline(n_estimators: int = 100, max_depth: int | None = None) -> Pipeline:
    """Build a scikit-learn Pipeline with preprocessing and classifier."""
    numeric_features = [0, 1, 2, 3]  # All Iris features are numeric

    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_transformer, numeric_features),
    ])

    return Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42,
        )),
    ])


def train():
    mlflow.set_experiment("day-031-scikit-pipeline")

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = build_pipeline(n_estimators=100, max_depth=5)

    # Cross-validate
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="accuracy")
    print(f"CV Accuracy: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

    with mlflow.start_run():
        # Final fit
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="weighted")

        # Log to MLflow
        mlflow.log_params({
            "n_estimators": 100,
            "max_depth": 5,
            "cv_folds": 5,
        })
        mlflow.log_metrics({
            "cv_accuracy_mean": cv_scores.mean(),
            "cv_accuracy_std": cv_scores.std(),
            "test_accuracy": accuracy,
            "test_f1": f1,
        })
        mlflow.sklearn.log_model(pipeline, "pipeline")

        print(f"\nTest Accuracy: {accuracy:.4f}")
        print(f"Test F1: {f1:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

    # Save locally
    model_path = MODELS_DIR / "iris_pipeline.joblib"
    joblib.dump(pipeline, model_path)
    print(f"\nModel saved to {model_path}")

    # Save metrics
    metrics = {"accuracy": accuracy, "f1_score": f1}
    (MODELS_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    train()
