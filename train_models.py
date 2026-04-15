import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc



# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv("C:/Users/tluke/Desktop/Resume Screening Project/data/pairs.csv")

print("Dataset size:", df.shape)

# -------------------------
# Features (X) and Labels (y)
# -------------------------
X = df[["similarity_score","skill_overlap"]]   
y = df["label"]

# -------------------------
# Train-test split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)

# -------------------------
# Train model
# -------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

model = GradientBoostingClassifier()
model.fit(X_train, y_train)

print("Model trained successfully!")

joblib.dump(model, "model.pkl")
print("Model saved!")

# -------------------------
# Predictions
# -------------------------
y_pred = model.predict(X_test)


# -------------------------
# Confusion Matrix
# -------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# -------------------------
# ROC Curve
# -------------------------
y_prob = model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()


# -------------------------
# Evaluation
# -------------------------
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))