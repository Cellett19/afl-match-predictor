import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
feature_path = BASE_DIR / "data" / "processed" / "features.csv"

feature_df = pd.read_csv(feature_path)

feature_df = feature_df[feature_df['Winner'] != 'Draw']

feature_df['Winner'] = feature_df['Winner'].map({'Home': 0, 'Away': 1})

train_df = feature_df[feature_df["Season"] <= 2020]
test_df  = feature_df[feature_df["Season"] >= 2021]

X_train = train_df.drop(columns=[
    "Season",
    "Winner",
    "Home_Team",
    "Away_Team"
])

y_train = train_df["Winner"]

X_test = test_df.drop(columns=[
    "Season",
    "Winner",
    "Home_Team",
    "Away_Team"
])

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

y_test = test_df["Winner"]

# Logistic Regression Model
logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train, y_train)

logistic_pred = logistic_model.predict(X_test)

logistic_accuracy = accuracy_score(y_test, logistic_pred)
print(f"Logistic Regression Accuracy: {logistic_accuracy:.4f}")

print("\nLogistic Confusion Matrix")
print(confusion_matrix(y_test, logistic_pred))

print("\nLogistic Classification Report")
print(classification_report(y_test, logistic_pred))

# Random Forest Model
random_forest_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

random_forest_model.fit(X_train, y_train)

random_forest_pred = random_forest_model.predict(X_test)

random_forest_accuracy = accuracy_score(y_test, random_forest_pred)

print(f"Random Forest Accuracy: {random_forest_accuracy:.4f}")

print("\nRandom Forest Confusion Matrix")
print(confusion_matrix(y_test, random_forest_pred))

print("\nRandom Forest Classification Report")
print(classification_report(y_test, random_forest_pred))

