import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("data/training_data.csv")

X = data[["semantic_score", "skill_overlap"]]
y = data["label"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "ml_models/ranking_model.pkl")
