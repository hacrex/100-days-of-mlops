<<<<<<< HEAD
# Day 31 — Implementation Notes

## What I Did

Built a full scikit-learn training pipeline for a classification task with mixed feature types, cross-validation, and MLflow logging.

## The Data Leakage Problem

```python
# WRONG — scaler sees test data during fit
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # fits on ALL data
X_train, X_test = train_test_split(X_scaled, ...)

# CORRECT — scaler only sees training data
X_train, X_test = train_test_split(X, ...)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fits on train only
X_test_scaled = scaler.transform(X_test)         # transforms test only

# BEST — Pipeline handles this automatically
pipeline = Pipeline([("scaler", StandardScaler()), ("clf", RandomForestClassifier())])
pipeline.fit(X_train, y_train)  # scaler.fit_transform on X_train, then clf.fit
pipeline.predict(X_test)        # scaler.transform on X_test, then clf.predict
```

## Full Pipeline Code

```python
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load Titanic dataset
titanic = fetch_openml("titanic", version=1, as_frame=True)
X = titanic.data[["pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]]
y = (titanic.target == "1").astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

numeric_features = ["age", "sibsp", "parch", "fare"]
categorical_features = ["pclass", "sex", "embarked"]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features),
])

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", GradientBoostingClassifier(n_estimators=100, random_state=42)),
])

# Cross-validate
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="roc_auc")
print(f"CV ROC-AUC: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")

# Final fit and evaluate
with mlflow.start_run():
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("cv_roc_auc_mean", cv_scores.mean())
    mlflow.log_metric("cv_roc_auc_std", cv_scores.std())
    mlflow.sklearn.log_model(pipeline, "pipeline")

    print(classification_report(y_test, y_pred))

# Save locally
joblib.dump(pipeline, "models/titanic_pipeline.joblib")
```

## Key Insight: Pipeline at Inference Time

```python
# Load the pipeline
pipeline = joblib.load("models/titanic_pipeline.joblib")

# New data — raw, unprocessed
new_passenger = pd.DataFrame({
    "pclass": [1], "sex": ["female"], "age": [28.0],
    "sibsp": [0], "parch": [0], "fare": [100.0], "embarked": ["S"]
})

# Pipeline handles all preprocessing automatically
prediction = pipeline.predict(new_passenger)
probability = pipeline.predict_proba(new_passenger)
```
=======
# Notes

Add your implementation notes here.
>>>>>>> 74eb85e2773b642d35fdd2d5a363469d366b02f4
