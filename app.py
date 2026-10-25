import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('model.sav')

# Title and description
st.title("Advertising Sales Prediction App")
st.write("Input the advertising budgets below to predict the estimated Sales.")

# User Inputs
tv = st.number_input("TV Advertising Budget ($)", min_value=0.0, value=100.0, step=1.0)
radio = st.number_input("Radio Advertising Budget ($)", min_value=0.0, value=20.0, step=1.0)
newspaper = st.number_input("Newspaper Advertising Budget ($)", min_value=0.0, value=15.0, step=1.0)

# Prediction button
if st.button("Predict Sales"):
    # Create dataframe matching the training features structure
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    prediction = model.predict(input_data)[0]
    
    st.success(f"Predicted Sales: {prediction:.2f} units")
