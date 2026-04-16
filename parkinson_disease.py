# ============================================
# Parkinson's Disease Prediction using Voice Measurements
# Full pipeline: Preprocessing → Scaling → Multiple Models → Comparison → Feature Importance
# ============================================

# 1. Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)

# 2. Load data
data = pd.read_csv('/content/parkinsons.data')
print("Original data shape:", data.shape)
print("First 2 rows:\n", data.head(2))

# 3. Check for missing values
print("\nMissing values:\n", data.isnull().sum())

# 4. Explore target distribution
print("\nTarget distribution:\n", data['status'].value_counts())
print("\nMean feature values by status:\n", data.groupby('status').mean(numeric_only=True).round(4))

# 5. Drop the 'name' column (not a feature)
if 'name' in data.columns:
    data = data.drop('name', axis=1)

# 6. Separate features (X) and target (y)
X = data.drop('status', axis=1)
y = data['status']

print("\nFeature names:", X.columns.tolist())
print(f"Features shape: {X.shape}, Target shape: {y.shape}")

# 7. Train-test split (stratified to preserve class balance)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 8. Feature scaling (StandardScaler) – needed for SVM & Logistic Regression
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 9. Define models to compare
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "SVM (RBF Kernel)": SVC(kernel='rbf', probability=True, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

# 10. Train & evaluate each model
results = []

for name, model in models.items():
    # Train
    model.fit(X_train_scaled, y_train)
    # Predict
    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else None
    
    # Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc = roc_auc_score(y_test, y_proba) if y_proba is not None else None
    
    results.append({
        "Model": name,
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1 Score": f1,
        "ROC-AUC": roc
    })
    
    # Print detailed report
    print(f"\n{'='*50}")
    print(f"Model: {name}")
    print(f"{'='*50}")
    print(f"Accuracy  : {acc:.4f}")
    print(f"Precision : {prec:.4f}")
    print(f"Recall    : {rec:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    if roc:
        print(f"ROC-AUC   : {roc:.4f}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

# 11. Compare all models side by side
results_df = pd.DataFrame(results)
print("\n" + "="*60)
print("MODEL COMPARISON SUMMARY")
print("="*60)
print(results_df.to_string(index=False))

# 12. Feature Importance from Random Forest (best interpretable model)
rf_model = models["Random Forest"]
importances = rf_model.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 6))
sns.barplot(x=importances[indices][:15], y=feature_names[indices][:15], palette="viridis")
plt.title("Random Forest - Top 15 Feature Importances", fontsize=14)
plt.xlabel("Importance Score", fontsize=12)
plt.ylabel("Features", fontsize=12)
plt.tight_layout()
plt.show()

print("\nTop 10 most important features:")
for i, idx in enumerate(indices[:10]):
    print(f"{i+1}. {feature_names[idx]} : {importances[idx]:.4f}")

# 13. (Optional) Save the best model (e.g., SVM if it performs best)
best_model_name = results_df.loc[results_df['ROC-AUC'].idxmax(), 'Model']
print(f"\nBest model based on ROC-AUC: {best_model_name}")

# 14. Example prediction for a new sample (using the best model)
best_model = models[best_model_name]
# Sample input (first row of original data without 'name' and 'status')
sample = X.iloc[0].values.reshape(1, -1)
sample_scaled = scaler.transform(sample)
prediction = best_model.predict(sample_scaled)
probability = best_model.predict_proba(sample_scaled)[0, 1] if hasattr(best_model, "predict_proba") else None

print(f"\nExample prediction for sample patient:")
print(f"Predicted status: {'Parkinson' if prediction[0]==1 else 'Healthy'}")
if probability:
    print(f"Probability of Parkinson: {probability:.4f}")
