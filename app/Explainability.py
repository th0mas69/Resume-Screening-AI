import shap
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/pairs.csv")

X = df[["similarity_score", "skill_overlap"]]
y = df["label"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# SHAP
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

# Summary plot
shap.summary_plot(shap_values, X)


