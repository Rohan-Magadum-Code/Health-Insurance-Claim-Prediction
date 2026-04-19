import streamlit as st
import pandas as pd
import numpy as np
import joblib

scaler = joblib.load('scaler.pkl')
le_diabetic = joblib.load('label_encoder_diabetic.pkl')
le_gender = joblib.load('label_encoder_gender.pkl')
le_smoker = joblib.load('label_encoder_smoker.pkl')
model = joblib.load('best_model.pkl')

st.set_page_config(page_title="Health Insurance Claim Predictor", layout="centered")
st.title("Health Insurance Claim Predictor")
st.write("Please enter the following details below to estimate your health insurance claim amount.")

# Input fields
with st.form(key='input_form'):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0)
        children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    with col2:
        blood_pressure = st.number_input("Blood Pressure", min_value=60, max_value=200, value=120)
        diabetic = st.selectbox("Diabetic", options=le_diabetic.classes_)
        gender = st.selectbox("Gender", options=le_gender.classes_)
        smoker = st.selectbox("Smoker", options=le_smoker.classes_)

    submit_button = st.form_submit_button(label='Predict Claim Amount')

if submit_button:
    # Prepare input data
    input_data = pd.DataFrame({
        'age': [age],
        'gender': le_gender.transform([gender])[0],
        'bmi': [bmi],
        'bloodpressure': [blood_pressure],
        'diabetic': le_diabetic.transform([diabetic])[0],
        'children': [children],
        'smoker': le_smoker.transform([smoker])[0]
    })

    num_cols = ['age', 'bmi', 'bloodpressure', 'children']
    input_data[num_cols] = scaler.transform(input_data[num_cols].values)

    # Predict claim amount
    predicted_claim = model.predict(input_data)[0]
    st.success(f"Estimated Health Insurance Claim Amount: ${predicted_claim:.2f}")