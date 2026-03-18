import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('crime_clean.csv')

# Target: predict if crime is a serious offense (Part 1 = serious, Part 2 = less serious)
df['Serious'] = (df['Part 1-2'] == 1).astype(int)

# Features — deliberately exclude Part 1-2 itself
features = ['Hour', 'Month', 'DayOfWeek', 'AREA']
df_model = df[features + ['Serious']].dropna()

X = df_model[features]
y = df_model['Serious']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc:.2%}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, 
      target_names=['Non-Serious', 'Serious']))

# Feature importance
importances = pd.Series(model.feature_importances_, index=features)
plt.figure(figsize=(8, 5))
sns.barplot(x=importances.values, y=importances.index, color='slateblue')
plt.title('Feature Importance — Serious Crime Prediction')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.close()
print("Saved feature_importance.png")

# Save predictions sample
df_model['Predicted'] = model.predict(X)
df_model.to_csv('crime_predictions.csv', index=False)
print("Saved crime_predictions.csv")