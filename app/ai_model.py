import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
    
    def train(self, log_features):
        self.model.fit(log_features)
    
    def predict(self, log_features):
        return self.model.predict(log_features)  # Returns -1 for anomalies, 1 for normal

anomaly_detector = AnomalyDetector()