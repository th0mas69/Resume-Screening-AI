import joblib
import numpy as np

def load_model():
    return joblib.load("ml_models/ranking_model.pkl")

def rank_score(features):
    model = load_model()
    return model.predict([features])[0]
