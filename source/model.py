import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
feature_path = BASE_DIR / "data" / "processed" / "features.csv"

feature_df = pd.read_csv(feature_path)

feature_df = feature_df[feature_df['Winner'] != 'Draw']

feature_df['Winner'] = feature_df['Winner'].map({'Home': 0, 'Away': 1})

X = feature_df.drop(columns=['Winner', 'Home_Team', 'Away_Team'])
y = feature_df['Winner']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))