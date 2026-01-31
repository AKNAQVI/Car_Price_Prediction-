import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("car_price_model (2).pkl")

# Streamlit UI
st.title("Car Price Prediction")

# User Inputs
car_name = st.text_input("Car Name")
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1)
fuel = st.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Ownership History", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"])
mileage = st.number_input("Mileage (kmpl)", min_value=5.0, max_value=50.0, step=0.1)
engine = st.number_input("Engine Capacity (CC)", min_value=600, max_value=5000, step=50)
max_power = st.number_input("Max Power (bhp)", min_value=20, max_value=500, step=5)
seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8, 9])

# Prediction
if st.button("Predict Price"):
    input_data = pd.DataFrame([[year, 0, mileage, engine, max_power, seats, fuel, transmission, owner]],
                              columns=["year", "km_driven", "mileage", "engine", "max_power", "seats", "fuel", "transmission", "owner"])
    predicted_price = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: {predicted_price:,.2f}")
