import streamlit as st
import pandas as pd
import joblib

# Load trained model and feature columns
model = joblib.load("crop_yield_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# Streamlit app UI
st.title("🌾 Crop Yield Prediction App")

# Input fields
state = st.selectbox("Select State", ["Karnataka", "Maharashtra", "Tamil Nadu", "Punjab"])
crop = st.selectbox("Select Crop", ["Rice", "Wheat", "Sugarcane", "Maize"])
season = st.selectbox("Select Season", ["Kharif", "Rabi", "Summer", "Winter", "Whole Year"])

# Predict on button click
if st.button("Predict Yield"):
    # Prepare input
    input_dict = {
        "state": state,
        "crop": crop,
        "season": season
    }

    # Convert to DataFrame and encode
    input_df = pd.DataFrame([input_dict])
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

    # Make prediction
    prediction = model.predict(input_encoded)
    st.success(f"🌱 Predicted Crop Yield: **{prediction[0]:.2f}** units")
