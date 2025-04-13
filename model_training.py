import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

# Load the dataset
df = pd.read_csv("crop_yield.csv")

# Set the correct target column name from your CSV
target_column = "Yield"  # 🔁 change this based on your CSV

# Split features and target
X = pd.get_dummies(df.drop(target_column, axis=1))
y = df[target_column]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ R² Score:", r2_score(y_test, y_pred))

# Save model & columns
joblib.dump(model, "crop_yield_model.pkl")
joblib.dump(X.columns.tolist(), "model_columns.pkl")
print("✅ Model and columns saved!")
