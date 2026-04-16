# ============================================
# Diabetes Prediction using Machine Learning
# Full pipeline: Preprocessing + Scaling + Full Evaluation + Feature Importance
# ============================================

# 1. Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)

# 2. Load data
data = pd.read_csv('/content/diabetes.csv')
print("Original data shape:", data.shape)
print("Original columns:\n", data.columns.tolist())

# 3. Replace zeros with NaN (domain knowledge: Glucose, BP, SkinThickness, Insulin, BMI cannot be 0)
zero_to_nan_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df = data.copy()
for col in zero_to_nan_cols:
    df[col] = df[col].replace(0, np.nan)

print("\nMissing values after zero replacement:")
print(df.isnull().sum())

# 4. Impute missing values using median
imputer = SimpleImputer(strategy='median')
df[zero_to_nan_cols] = imputer.fit_transform(df[zero_to_nan_cols])
print("\nMissing values after imputation:")
print(df.isnull().sum())

# 5. Outlier detection and capping (IQR method)
def cap_outliers_iqr(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df[col] = df[col].clip(lower, upper)
    return df

feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
                'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
df = cap_outliers_iqr(df, feature_cols)

# 6. Split features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# 7. Train-test split (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2, stratify=y
)

# 8. Feature scaling (StandardScaler) – only for Logistic Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 9. Logistic Regression (with scaling)
log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train_scaled, y_train)
y_pred_lr = log_reg.predict(X_test_scaled)
y_proba_lr = log_reg.predict_proba(X_test_scaled)[:, 1]

# 10. Random Forest (no scaling needed, but use original features)
rf = RandomForestClassifier(
    n_estimators=300, max_depth=6, min_samples_leaf=10,
    max_features='sqrt', class_weight='balanced', random_state=42
)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_proba_rf = rf.predict_proba(X_test)[:, 1]

# 11. Evaluation function
def evaluate_model(name, y_true, y_pred, y_proba=None):
    print(f"\n{'='*50}")
    print(f"Model: {name}")
    print(f"{'='*50}")
    print(f"Accuracy  : {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision : {precision_score(y_true, y_pred):.4f}")
    print(f"Recall    : {recall_score(y_true, y_pred):.4f}")
    print(f"F1 Score  : {f1_score(y_true, y_pred):.4f}")
    if y_proba is not None:
        print(f"ROC-AUC   : {roc_auc_score(y_true, y_proba):.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))

# 12. Evaluate both models
evaluate_model("Logistic Regression (Test Set)", y_test, y_pred_lr, y_proba_lr)
evaluate_model("Random Forest (Test Set)", y_test, y_pred_rf, y_proba_rf)

# 13. Feature Importance Analysis (Random Forest)
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]
feature_names = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=feature_names[indices], palette="viridis")
plt.title("Random Forest - Feature Importance", fontsize=14)
plt.xlabel("Importance Score", fontsize=12)
plt.ylabel("Features", fontsize=12)
plt.tight_layout()
plt.show()

print("\nFeature importance ranking:")
for i, idx in enumerate(indices):
    print(f"{i+1}. {feature_names[idx]} : {importances[idx]:.4f}")

# 14. (Optional) Compare models side by side
comparison = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest'],
    'Accuracy': [accuracy_score(y_test, y_pred_lr), accuracy_score(y_test, y_pred_rf)],
    'Recall': [recall_score(y_test, y_pred_lr), recall_score(y_test, y_pred_rf)],
    'ROC-AUC': [roc_auc_score(y_test, y_proba_lr), roc_auc_score(y_test, y_proba_rf)]
})
print("\n" + "="*50)
print("Model Comparison Summary")
print(comparison.to_string(index=False))
