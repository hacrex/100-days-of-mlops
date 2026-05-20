"""Pydantic schemas for ML serving API."""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class PredictionRequest(BaseModel):
    """Request schema for single prediction."""
    
    age: int = Field(..., ge=18, le=100, description="Customer age")
    income: float = Field(..., gt=0, description="Annual income in USD")
    tenure_months: int = Field(..., ge=0, description="Months as customer")
    num_products: int = Field(..., ge=1, le=20, description="Number of products owned")


class PredictionResponse(BaseModel):
    """Response schema for single prediction."""
    
    prediction: int = Field(..., description="Churn prediction (0 or 1)")
    probability: float = Field(..., ge=0, le=1, description="Churn probability")
    risk_level: str = Field(..., description="Risk level: low, medium, or high")
    timestamp: str = Field(..., description="ISO format timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "prediction": 0,
                "probability": 0.23,
                "risk_level": "low",
                "timestamp": "2024-01-15T10:30:00"
            }
        }


class BatchPredictionRequest(BaseModel):
    """Request schema for batch predictions."""
    
    requests: List[PredictionRequest] = Field(
        ..., 
        min_length=1, 
        max_length=100,
        description="List of prediction requests"
    )


class BatchPredictionResponse(BaseModel):
    """Response schema for batch predictions."""
    
    predictions: List[Optional[PredictionResponse]]
    errors: List[str] = []


class HealthResponse(BaseModel):
    """Health check response."""
    
    status: str
    model_loaded: bool
    timestamp: str
    version: str = "1.0.0"
