"""FastAPI model serving for End-to-End ML System."""

import os
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Optional

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="ML Churn Prediction API",
    description="Customer churn prediction service",
    version="1.0.0"
)

# Prometheus metrics
PREDICTION_COUNTER = Counter(
    'predictions_total',
    'Total number of predictions made'
)
LATENCY_HISTOGRAM = Histogram(
    'prediction_latency_seconds',
    'Prediction latency in seconds'
)
ERROR_COUNTER = Counter(
    'prediction_errors_total',
    'Total number of prediction errors'
)

# Model loading
MODELS_DIR = Path(__file__).parent.parent.parent / "models"
model = None
feature_columns = None


def load_model():
    """Load the latest model from disk."""
    global model, feature_columns
    
    if not MODELS_DIR.exists():
        logger.warning(f"Models directory not found: {MODELS_DIR}")
        return
    
    model_files = list(MODELS_DIR.glob("*.pkl"))
    if not model_files:
        logger.warning("No .pkl files found in models directory")
        return
    
    latest_file = max(model_files, key=lambda f: f.stat().st_mtime)
    model = joblib.load(latest_file)
    
    # Default feature columns (should match training)
    feature_columns = [
        'age', 'income', 'tenure_months', 'num_products',
        'income_per_tenure', 'products_per_tenure', 'log_income',
        'age_group_encoded', 'income_age_ratio', 'tenure_product_interaction',
        'income_normalized', 'age_normalized', 'risk_score'
    ]
    
    logger.info(f"Loaded model from: {latest_file}")


@app.on_event("startup")
async def startup_event():
    """Load model on startup."""
    load_model()


class PredictionRequest(BaseModel):
    """Request schema for prediction."""
    age: int = Field(..., ge=18, le=100, description="Customer age")
    income: float = Field(..., gt=0, description="Annual income")
    tenure_months: int = Field(..., ge=0, description="Months as customer")
    num_products: int = Field(..., ge=1, le=20, description="Number of products")


class PredictionResponse(BaseModel):
    """Response schema for prediction."""
    prediction: int
    probability: float
    risk_level: str
    timestamp: str


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "timestamp": datetime.now().isoformat()
    }


@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/predict", response_model=PredictionResponse)
@LATENCY_HISTOGRAM.time()
async def predict(request: PredictionRequest):
    """Make a churn prediction.
    
    Args:
        request: Prediction request with customer features
        
    Returns:
        Prediction response with churn probability
    """
    try:
        if model is None:
            raise HTTPException(status_code=503, detail="Model not loaded")
        
        # Create feature vector
        features = {
            'age': request.age,
            'income': request.income,
            'tenure_months': request.tenure_months,
            'num_products': request.num_products,
            'income_per_tenure': request.income / (request.tenure_months + 1),
            'products_per_tenure': request.num_products / (request.tenure_months + 1),
            'log_income': np.log1p(request.income),
            'age_group_encoded': min(3, max(0, (request.age - 18) // 10)),
            'income_age_ratio': request.income / request.age,
            'tenure_product_interaction': request.tenure_months * request.num_products,
            'income_normalized': 0,  # Would need population stats
            'age_normalized': 0,
            'risk_score': 0.5  # Placeholder
        }
        
        X = pd.DataFrame([features])[feature_columns]
        
        # Predict
        prediction = int(model.predict(X)[0])
        probability = float(model.predict_proba(X)[0][1])
        
        # Determine risk level
        if probability < 0.3:
            risk_level = "low"
        elif probability < 0.7:
            risk_level = "medium"
        else:
            risk_level = "high"
        
        PREDICTION_COUNTER.inc()
        
        return PredictionResponse(
            prediction=prediction,
            probability=round(probability, 4),
            risk_level=risk_level,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        ERROR_COUNTER.inc()
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/batch-predict")
async def batch_predict(requests: List[PredictionRequest]):
    """Batch prediction endpoint.
    
    Args:
        requests: List of prediction requests
        
    Returns:
        List of prediction responses
    """
    results = []
    for req in requests:
        try:
            result = await predict(req)
            results.append(result)
        except Exception as e:
            results.append({"error": str(e)})
    
    return {"predictions": results}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
