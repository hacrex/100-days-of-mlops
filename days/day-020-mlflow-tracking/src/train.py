"""
Day 20 - MLflow Experiment Tracking
Train an Iris classifier with MLflow logging.
"""

import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

EXPERIMENT_NAME = "day-020-iris-classification"

# Hyperparameter grid to explore
CONFIGS = [
    {"n_estimators": 50, "max_depth": 3},
    {"n_estimators": 100, "max_depth": 5},
    {"n_estimators": 200, "max_depth": None},
]


def train():
    mlflow.set_experiment(EXPERIMENT_NAME)

    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    for config in CONFIGS:
        with mlflow.start_run():
            # Log parameters
            mlflow.log_params(config)
            mlflow.set_tag("dataset", "iris")
            mlflow.set_tag("model_type", "RandomForestClassifier")

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

            print(
                f"Config: {config} | "
                f"Accuracy: {accuracy:.4f} | "
                f"F1: {f1:.4f}"
            )


if __name__ == "__main__":
    train()
