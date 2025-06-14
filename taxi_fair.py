import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

st.title("TripFare Prediction App")
st.markdown("Predict total taxi fare based on trip details using the Linear Regression model.")

try:
    with open("LinearRegression_model.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

VendorID = st.selectbox("Vendor ID", [1, 2])
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)
pickup_date = st.date_input("Pickup Date")
pickup_time = st.time_input("Pickup Time")
dropoff_date = st.date_input("Dropoff Date")
dropoff_time = st.time_input("Dropoff Time")

pickup_datetime = datetime.combine(pickup_date, pickup_time)
dropoff_datetime = datetime.combine(dropoff_date, dropoff_time)

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

RatecodeID = st.selectbox("Ratecode ID", [1, 2, 3, 4, 5, 6])

store_and_fwd_flag_str = st.selectbox("Store and Forward Flag", ['N', 'Y'])
store_and_fwd_flag = 0 if store_and_fwd_flag_str == 'N' else 1

payment_type = st.selectbox("Payment Type", [1, 2, 3, 4, 5, 6])

fare_amount = st.number_input("Fare Amount (Rs)", value=10.0)
extra = st.number_input("Extra Charges (Rs)", value=0.5)
mta_tax = st.number_input("MTA Tax (Rs)", value=0.5)
tip_amount = st.number_input("Tip Amount (Rs)", value=2.0)
tolls_amount = st.number_input("Tolls Amount (Rs)", value=0.0)
improvement_surcharge = st.number_input("Improvement Surcharge (Rs)", value=0.3)

pickup_hour = pickup_datetime.hour
pickup_day = pickup_datetime.weekday()
is_night = int(pickup_hour >= 20 or pickup_hour < 5)
am_pm = int(pickup_hour >= 12)
is_weekend = int(pickup_day in [5, 6])

trip_duration = (dropoff_datetime - pickup_datetime).total_seconds() / 60  # duration in minutes
trip_distance = np.sqrt(
    (dropoff_longitude - pickup_longitude)**2 +
    (dropoff_latitude - pickup_latitude)**2
) * 69  # Approx miles, rough estimate

input_data = pd.DataFrame([{
    'VendorID': VendorID,
    'passenger_count': passenger_count,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'RatecodeID': RatecodeID,
    'store_and_fwd_flag': store_and_fwd_flag,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'payment_type': payment_type,
    'fare_amount': fare_amount,
    'extra': extra,
    'mta_tax': mta_tax,
    'tip_amount': tip_amount,
    'tolls_amount': tolls_amount,
    'improvement_surcharge': improvement_surcharge,
    'pickup_hour': pickup_hour,
    'pickup_day': pickup_day,
    'is_weekend': is_weekend,
    'am_pm': am_pm,
    'is_night': is_night,
    'trip_duration': trip_duration,
    'trip_distance': trip_distance
}])

if st.button("Predict Total Fare"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Total Fare: Rs{prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
