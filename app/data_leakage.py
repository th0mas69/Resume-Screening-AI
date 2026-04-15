from sklearn.model_selection import GroupShuffleSplit
import pandas as pd

df = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/pairs.csv")

X = df[["similarity_score", "skill_overlap"]]
y = df["label"]
groups = df["resume_id"]   # IMPORTANT

gss = GroupShuffleSplit(test_size=0.2, random_state=42)

train_idx, test_idx = next(gss.split(X, y, groups))

X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]