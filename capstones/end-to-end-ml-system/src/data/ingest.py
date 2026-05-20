"""Data ingestion module for End-to-End ML System."""

import os
import logging
from pathlib import Path
import pandas as pd
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DIR = DATA_DIR / "raw"


def load_sample_data() -> pd.DataFrame:
    """Load sample data for demonstration.
    
    In production, this would connect to databases, APIs, or file storage.
    """
    # Create synthetic dataset for demonstration
    n_samples = 1000
    
    data = {
        'customer_id': range(1, n_samples + 1),
        'age': pd.np.random.randint(18, 70, n_samples),
        'income': pd.np.random.uniform(20000, 150000, n_samples),
        'tenure_months': pd.np.random.randint(1, 72, n_samples),
        'num_products': pd.np.random.randint(1, 10, n_samples),
        'churned': pd.np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    }
    
    df = pd.DataFrame(data)
    return df


def ingest_data(output_path: Path = None) -> Path:
    """Ingest raw data and save to data/raw directory.
    
    Args:
        output_path: Optional custom output path
        
    Returns:
        Path to saved data file
    """
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = RAW_DIR / f"raw_data_{timestamp}.csv"
    
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    
    logger.info("Loading sample data...")
    df = load_sample_data()
    
    logger.info(f"Saving {len(df)} records to {output_path}")
    df.to_csv(output_path, index=False)
    
    logger.info(f"Data ingestion complete: {output_path}")
    return output_path


if __name__ == "__main__":
    ingest_data()
