"""Model evaluation module for End-to-End ML System."""

import os
import logging
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
import json
from datetime import datetime
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    roc_auc_score, confusion_matrix, classification_report
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
FEATURES_DIR = DATA_DIR / "features"
MODELS_DIR = Path(__file__).parent.parent.parent / "models"
EVALUATION_DIR = Path(__file__).parent.parent.parent / "evaluations"


def load_latest_model() -> tuple:
    """Load the most recent model file.
    
    Returns:
        Tuple of (model, model_path)
    """
    if not MODELS_DIR.exists():
        raise FileNotFoundError(f"Models directory not found: {MODELS_DIR}")
    
    model_files = list(MODELS_DIR.glob("*.pkl"))
    if not model_files:
        raise FileNotFoundError("No .pkl files found in models directory")
    
    latest_file = max(model_files, key=lambda f: f.stat().st_mtime)
    logger.info(f"Loading model from: {latest_file}")
    
    model = joblib.load(latest_file)
    return model, latest_file


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


def evaluate_model(model, X_test, y_test) -> dict:
    """Comprehensive model evaluation.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels
        
    Returns:
        Dictionary of evaluation results
    """
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    # Basic metrics
    metrics = {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'precision': float(precision_score(y_test, y_pred)),
        'recall': float(recall_score(y_test, y_pred)),
        'f1': float(f1_score(y_test, y_pred)),
        'roc_auc': float(roc_auc_score(y_test, y_proba))
    }
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    metrics['confusion_matrix'] = cm.tolist()
    
    # Classification report
    report = classification_report(y_test, y_pred, output_dict=True)
    metrics['classification_report'] = report
    
    # Feature importance (if available)
    if hasattr(model, 'feature_importances_'):
        metrics['feature_importance'] = model.feature_importances_.tolist()
    
    return metrics


def save_evaluation_results(metrics: dict, output_path: Path = None) -> Path:
    """Save evaluation results to disk.
    
    Args:
        metrics: Evaluation metrics dictionary
        output_path: Optional custom output path
        
    Returns:
        Path to saved file
    """
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        EVALUATION_DIR.mkdir(parents=True, exist_ok=True)
        output_path = EVALUATION_DIR / f"evaluation_{timestamp}.json"
    
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    logger.info(f"Saved evaluation results to: {output_path}")
    return output_path


def main():
    """Main evaluation pipeline."""
    try:
        # Load model and data
        model, model_path = load_latest_model()
        df = load_features()
        
        # Prepare test data (same split as training)
        exclude_cols = ['customer_id', 'churned', 'age_group']
        feature_cols = [col for col in df.columns if col not in exclude_cols]
        
        X = df[feature_cols].select_dtypes(include=[np.number])
        y = df['churned']
        
        # Use last 20% as test set (matching train.py)
        split_idx = int(len(X) * 0.8)
        X_test = X.iloc[split_idx:]
        y_test = y.iloc[split_idx:]
        
        # Evaluate
        logger.info("Running model evaluation...")
        metrics = evaluate_model(model, X_test, y_test)
        
        # Save results
        output_path = save_evaluation_results(metrics)
        
        # Log summary
        logger.info("\n=== Evaluation Summary ===")
        logger.info(f"Accuracy:  {metrics['accuracy']:.4f}")
        logger.info(f"Precision: {metrics['precision']:.4f}")
        logger.info(f"Recall:    {metrics['recall']:.4f}")
        logger.info(f"F1 Score:  {metrics['f1']:.4f}")
        logger.info(f"ROC AUC:   {metrics['roc_auc']:.4f}")
        
        return output_path, metrics
        
    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        raise


if __name__ == "__main__":
    main()
