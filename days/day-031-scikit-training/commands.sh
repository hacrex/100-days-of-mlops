<<<<<<< HEAD
#!/bin/bash
# Day 31 - Scikit-learn Training Pipeline

# --- Install dependencies ---
pip install scikit-learn pandas numpy joblib mlflow

# --- Run training ---
python src/train.py

# --- Run evaluation ---
python src/evaluate.py

# --- Cross-validate ---
python -c "
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(clf, X, y, cv=5, scoring='accuracy')
print(f'CV Accuracy: {scores.mean():.4f} +/- {scores.std():.4f}')
"

# --- Save and load a model ---
python -c "
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)
joblib.dump(model, '/tmp/model.joblib')
loaded = joblib.load('/tmp/model.joblib')
print('Loaded model predictions:', loaded.predict(X[:3]))
"

# --- Inspect a pipeline ---
python -c "
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
pipe = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression())])
print(pipe)
print('Steps:', [name for name, _ in pipe.steps])
"
=======
#!/bin/bash

# Add commands here
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
