import streamlit as st
import requests
from datetime import datetime
'''
# TaxiFareModel front
'''
st.markdown('''
### Select the parameters of your ride:
''')
# 1. Get the user inputs for the ride parameters
pickup_datetime = st.text_input("Enter the date and time of the ride (YYYY-MM-DD HH:MM:SS)",
                                value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6)
# 2. Build a dictionary containing the parameters for the API
ride_params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}
url = 'https://taxifare.lewagon.ai/predict'
if url == 'https://taxifare.lewagon.ai/predict':
        # API call
        response = requests.get(url, params=ride_params)
        data = response.json()
        # 4. Retrieve and display the prediction
        prediction = data['fare']
        st.success(f"Estimated fare: ${prediction:.2f}")
