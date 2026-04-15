import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/pairs.csv")

X = df[["similarity_score", "skill_overlap"]]
y = df["label"]

model = RandomForestClassifier(n_estimators=100)

scores = cross_val_score(model, X, y, cv=5, scoring="f1")

print("F1 Scores:", scores)
print("Average F1:", scores.mean())