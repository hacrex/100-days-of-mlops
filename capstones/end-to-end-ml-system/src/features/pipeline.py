"""Feature engineering pipeline for End-to-End ML System."""

import logging
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
FEATURES_DIR = DATA_DIR / "features"


def load_processed_data() -> pd.DataFrame:
    """Load the most recent processed data file."""
    if not PROCESSED_DIR.exists():
        raise FileNotFoundError(f"Processed data directory not found: {PROCESSED_DIR}")
    
    processed_files = list(PROCESSED_DIR.glob("*.csv"))
    if not processed_files:
        raise FileNotFoundError("No CSV files found in processed data directory")
    
    latest_file = max(processed_files, key=lambda f: f.stat().st_mtime)
    logger.info(f"Loading processed data from: {latest_file}")
    
    return pd.read_csv(latest_file)


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create features for model training.
    
    Args:
        df: Processed input dataframe
        
    Returns:
        Dataframe with engineered features
    """
    logger.info(f"Creating features for {len(df)} records...")
    
    # Encode categorical variables
    df['age_group_encoded'] = df['age_group'].map({
        'young': 0, 'mid': 1, 'senior': 2, 'elderly': 3
    })
    
    # Interaction features
    df['income_age_ratio'] = df['income'] / df['age']
    df['tenure_product_interaction'] = df['tenure_months'] * df['num_products']
    
    # Normalized features
    df['income_normalized'] = (df['income'] - df['income'].mean()) / df['income'].std()
    df['age_normalized'] = (df['age'] - df['age'].mean()) / df['age'].std()
    
    # Risk score (simple heuristic)
    df['risk_score'] = (
        0.3 * (1 - df['tenure_months'] / df['tenure_months'].max()) +
        0.3 * (df['num_products'] / df['num_products'].max()) +
        0.4 * (df['age'] / df['age'].max())
    )
    
    logger.info(f"Created {len(df.columns)} features")
    return df


def save_features(df: pd.DataFrame, output_path: Path = None) -> Path:
    """Save feature matrix to disk.
    
    Args:
        df: Feature dataframe
        output_path: Optional custom output path
        
    Returns:
        Path to saved file
    """
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = FEATURES_DIR / f"features_{timestamp}.csv"
    
    FEATURES_DIR.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    logger.info(f"Saved features to: {output_path}")
    
    return output_path


def main():
    """Main feature engineering pipeline."""
    try:
        # Load processed data
        df = load_processed_data()
        
        # Create features
        df_features = create_features(df)
        
        # Save
        output_path = save_features(df_features)
        
        logger.info(f"Feature pipeline complete. Output: {output_path}")
        return output_path
        
    except Exception as e:
        logger.error(f"Feature engineering failed: {e}")
        raise


if __name__ == "__main__":
    main()
