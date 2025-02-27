from fastapi import APIRouter
from app.ai_model import anomaly_detector
import numpy as np

router = APIRouter()

@router.post("/alerts/")
def detect_anomalies(log_data: list):
    log_features = np.array(log_data)
    predictions = anomaly_detector.predict(log_features)
    anomalies = [log_data[i] for i in range(len(predictions)) if predictions[i] == -1]
    return {"anomalies": anomalies}