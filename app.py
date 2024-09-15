import streamlit as st
import pickle
import pandas as pd

# Load the trained model from the pickle file
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app code
st.title('Real Estate Price Prediction')

# Input form for user data
with st.form("prediction_form"):
    st.write("Please enter the following details to predict real estate prices:")
    house_age = st.number_input('House Age:', min_value=0, max_value=100, value=50, step=1)
    distance_to_mrt = st.number_input('Distance to the nearest MRT station:', min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    num_convenience_stores = st.number_input('Number of Convenience Stores:', min_value=0, max_value=10, value=5, step=1)
    latitude = st.number_input('Latitude:', min_value=0.0, max_value=90.0, value=25.0, step=0.0001)
    longitude = st.number_input('Longitude:', min_value=0.0, max_value=180.0, value=121.0, step=0.0001)
    
    # Submit button for the form
    submit_button = st.form_submit_button("Predict Price")

# When the user clicks the submit button, make a prediction and display it
if submit_button:
    user_inputs = pd.DataFrame({
        'House age': [house_age],
        'Distance to the nearest MRT station': [distance_to_mrt],
        'Number of convenience stores': [num_convenience_stores],
        'Latitude': [latitude],
        'Longitude': [longitude]
    })

    predicted_price = model.predict(user_inputs)[0]

    # Display the predicted price
    st.subheader(f'Predicted House Price: ${predicted_price:.2f}')
