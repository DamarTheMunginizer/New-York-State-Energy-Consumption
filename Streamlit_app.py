import streamlit as st
import pandas as pd
import plotly.express as px
import json
import numpy as np
import pickle

# Load Models
@st.cache
def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

electrical_load_model = load_model('electrical_load_model.pkl') # file path of the pickled model
weather_model = load_model('weather_model.pkl')

# Load Data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

weather_data = load_data('./data/new-new-york-weather.csv') 
electrical_load_data = load_data('electrical_load_data.csv')  

# Sidebar for Year Selection
year = st.sidebar.slider("Select Year", min_value=2005, max_value=2025, step=1)

# Filter Weather Data for Selected Year and Predict
filtered_weather = weather_data[weather_data['Year'] == year]
weather_predictions = weather_model.predict(filtered_weather[['Precipitation', 'WindSpeed', 'SunshineDuration']])
filtered_weather['Prediction'] = weather_predictions

# Filter Electrical Load Data for Selected Year and Predict
filtered_load = electrical_load_data[electrical_load_data['Year'] == year]
load_predictions = electrical_load_model.predict(filtered_load[['Feature1', 'Feature2', 'Feature3']])  # Replace with actual features
filtered_load['Prediction'] = load_predictions

# Visualize Weather Predictions on Scatter Map
st.subheader("Weather Predictions in NY State")
weather_fig = px.scatter_mapbox(
    filtered_weather,
    lat="Latitude",
    lon="Longitude",
    color="Prediction",  # Weather prediction values
    size_max=15,
    mapbox_style="carto-positron",
    zoom=6,
    title=f"Weather Predictions for {year}",
    height=600
)
center_lat, center_lon = 42.9, -75.0  # NY State center
weather_fig.update_layout(mapbox=dict(center={"lat": center_lat, "lon": center_lon}))
st.plotly_chart(weather_fig)

# Visualize Electrical Load Predictions on Scatter Map
st.subheader("Electrical Load Predictions in NY State")
load_fig = px.scatter_mapbox(
    filtered_load,
    lat="Latitude",
    lon="Longitude",
    color="Prediction",  # Predicted load values
    size_max=15,
    mapbox_style="carto-positron",
    zoom=6,
    title=f"Electrical Load Predictions for {year}",
    height=600
)
load_fig.update_layout(mapbox=dict(center={"lat": center_lat, "lon": center_lon}))
st.plotly_chart(load_fig)


