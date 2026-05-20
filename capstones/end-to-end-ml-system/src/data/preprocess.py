"""Data preprocessing module for End-to-End ML System."""

import logging
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def load_latest_raw_data() -> pd.DataFrame:
    """Load the most recent raw data file."""
    if not RAW_DIR.exists():
        raise FileNotFoundError(f"Raw data directory not found: {RAW_DIR}")
    
    raw_files = list(RAW_DIR.glob("*.csv"))
    if not raw_files:
        raise FileNotFoundError("No CSV files found in raw data directory")
    
    latest_file = max(raw_files, key=lambda f: f.stat().st_mtime)
    logger.info(f"Loading raw data from: {latest_file}")
    
    return pd.read_csv(latest_file)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply preprocessing transformations.
    
    Args:
        df: Raw input dataframe
        
    Returns:
        Preprocessed dataframe
    """
    logger.info(f"Preprocessing {len(df)} records...")
    
    # Handle missing values
    df = df.dropna()
    
    # Feature engineering
    df['income_per_tenure'] = df['income'] / (df['tenure_months'] + 1)
    df['products_per_tenure'] = df['num_products'] / (df['tenure_months'] + 1)
    
    # Log transform income to handle skewness
    df['log_income'] = np.log1p(df['income'])
    
    # Age bins
    df['age_group'] = pd.cut(
        df['age'], 
        bins=[0, 25, 35, 50, 70], 
        labels=['young', 'mid', 'senior', 'elderly']
    )
    
    # Remove outliers (income > 3 std)
    mean_income = df['income'].mean()
    std_income = df['income'].std()
    df = df[
        (df['income'] >= mean_income - 3 * std_income) & 
        (df['income'] <= mean_income + 3 * std_income)
    ]
    
    logger.info(f"Preprocessing complete. {len(df)} records remaining.")
    return df


def save_processed_data(df: pd.DataFrame, output_path: Path = None) -> Path:
    """Save processed data to disk.
    
    Args:
        df: Processed dataframe
        output_path: Optional custom output path
        
    Returns:
        Path to saved file
    """
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = PROCESSED_DIR / f"processed_data_{timestamp}.csv"
    
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)
    logger.info(f"Saved processed data to: {output_path}")
    
    return output_path


def main():
    """Main preprocessing pipeline."""
    try:
        # Load raw data
        df = load_latest_raw_data()
        
        # Preprocess
        df_clean = preprocess_data(df)
        
        # Save
        output_path = save_processed_data(df_clean)
        
        logger.info(f"Pipeline complete. Output: {output_path}")
        return output_path
        
    except Exception as e:
        logger.error(f"Preprocessing failed: {e}")
        raise


if __name__ == "__main__":
    main()
