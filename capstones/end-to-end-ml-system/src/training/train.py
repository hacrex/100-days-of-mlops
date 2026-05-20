"""Model training module for End-to-End ML System."""

import os
import logging
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
FEATURES_DIR = DATA_DIR / "features"
MODELS_DIR = Path(__file__).parent.parent.parent / "models"

# MLflow configuration
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
MLFLOW_EXPERIMENT_NAME = "end-to-end-ml-churn"


def load_features() -> pd.DataFrame:
    """Load the most recent feature file."""
    if not FEATURES_DIR.exists():
        raise FileNotFoundError(f"Features directory not found: {FEATURES_DIR}")
    
    feature_files = list(FEATURES_DIR.glob("*.csv"))
    if not feature_files:
        raise FileNotFoundError("No CSV files found in features directory")
    
    latest_file = max(feature_files, key=lambda f: f.stat().st_mtime)
    logger.info(f"Loading features from: {latest_file}")
    
    return pd.read_csv(latest_file)


def prepare_data(df: pd.DataFrame):
    """Prepare features and target for training.
    
    Args:
        df: Feature dataframe
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    # Define feature columns (exclude non-feature columns)
    exclude_cols = ['customer_id', 'churned', 'age_group']
    feature_cols = [col for col in df.columns if col not in exclude_cols]
    
    X = df[feature_cols]
    y = df['churned']
    
    # Handle any remaining categorical columns
    X = X.select_dtypes(include=[np.number])
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    logger.info(f"Training set: {len(X_train)} samples")
    logger.info(f"Test set: {len(X_test)} samples")
    
    return X_train, X_test, y_train, y_test, feature_cols


def train_model(X_train, y_train, params: dict = None):
    """Train a Random Forest classifier.
    
    Args:
        X_train: Training features
        y_train: Training labels
        params: Model hyperparameters
        
    Returns:
        Trained model
    """
    if params is None:
        params = {
            'n_estimators': 100,
            'max_depth': 10,
            'min_samples_split': 5,
            'random_state': 42
        }
    
    logger.info(f"Training model with params: {params}")
    
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    
    logger.info("Model training complete")
    return model


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        
    Returns:
        Dictionary of metrics
    """
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_proba)
    }
    
    logger.info("Model Evaluation:")
    for name, value in metrics.items():
        logger.info(f"  {name}: {value:.4f}")
    
    return metrics


def save_model(model, model_path: Path = None) -> Path:
    """Save model to disk.
    
    Args:
        model: Trained model
        model_path: Optional custom output path
        
    Returns:
        Path to saved model
    """
    if model_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        MODELS_DIR.mkdir(parents=True, exist_ok=True)
        model_path = MODELS_DIR / f"model_{timestamp}.pkl"
    
    import joblib
    joblib.dump(model, model_path)
    logger.info(f"Saved model to: {model_path}")
    
    return model_path


def main():
    """Main training pipeline."""
    try:
        # Set up MLflow
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)
        
        # Load features
        df = load_features()
        
        # Prepare data
        X_train, X_test, y_train, y_test, feature_cols = prepare_data(df)
        
        # Train model
        model = train_model(X_train, y_train)
        
        # Evaluate
        metrics = evaluate_model(model, X_test, y_test)
        
        # Log to MLflow
        with mlflow.start_run():
            mlflow.log_params({
                'n_estimators': 100,
                'max_depth': 10,
                'min_samples_split': 5
            })
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(model, "model")
            
            run_id = mlflow.active_run().info.run_id
            logger.info(f"MLflow run ID: {run_id}")
        
        # Save model locally
        model_path = save_model(model)
        
        logger.info(f"Training pipeline complete. Model saved to: {model_path}")
        return model_path, metrics
        
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise


if __name__ == "__main__":
    main()
