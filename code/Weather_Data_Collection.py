import numpy as np
import pandas as pd
from retry_requests import retry
import openmeteo_requests
import requests_cache
import time
import random
import os


# Setup cached session with retry functionality
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry = Retry(total=5, backoff_factor=0.2)
retry_session = requests_cache.CachedSession('.cache', expire_after=3600)
openmeteo = openmeteo_requests.Client(session=retry_session)

# List of coordinates (latitude, longitude)
coordinates = [
    (42.6, -73.97), (42.5273, -73.908), (42.6632, -73.8903),
    (42.25, -78.02), (42.3408, -77.9462), (42.1825, -77.966),
    (40.85, -73.8667),
    (42.17, -75.82), (42.0935, -75.8327), (42.2335, -75.8336),
    (42.25, -78.68), (42.1957, -78.6287), (42.3213, -78.6293),
    (42.95, -76.56), (43.0382, -76.524), (43.0324, -76.6587),
    (42.25, -79.37), (42.3169, -79.3912), (42.2706, -79.4473),
    (42.15, -76.75), (42.1932, -76.8433), (42.2487, -76.6562),
    (42.5, -75.6), (42.509, -75.5603), (42.5852, -75.5167),
    (44.75, -73.7), (44.7984, -73.7165), (44.819, -73.7095),
    (42.25, -73.63), (42.1683, -73.687), (42.1781, -73.5694),
    (42.6, -76.0), (42.6139, -76.086), (42.5666, -76.0895),
    (42.2, -74.95), (42.213, -74.982), (42.1821, -74.9847),
    (41.75, -73.74), (41.8488, -73.757), (41.7248, -73.6964),
    (42.77, -78.64), (42.8206, -78.673), (42.839, -78.7131),
    (44.1, -73.77), (44.0899, -73.8463), (44.0396, -73.6853),
    (44.59, -74.34), (44.4999, -74.4129), (44.6333, -74.3266),
    (43.1, -74.43), (43.1869, -74.5102), (43.038, -74.3446),
    (43.0, -78.19), (42.9548, -78.0943), (42.932, -78.1732),
    (42.3, -74.13), (42.2518, -74.1249), (42.3921, -74.2229),
    (43.67, -74.5), (43.6537, -74.4334), (43.7283, -74.5597),
    (43.42, -74.98), (43.5023, -75.0579), (43.4821, -74.8937),
    (44.0, -75.92), (44.0255, -76.0046), (44.0407, -75.9948),
    (40.65, -73.95),
    (43.79, -75.46), (43.8139, -75.5525), (43.848, -75.4359),
    (42.73, -77.78), (42.6432, -77.706), (42.7847, -77.7621),
    (42.9, -75.7), (42.9976, -75.7697), (42.8931, -75.6475),
    (43.15, -77.62), (43.1521, -77.5636), (43.1053, -77.6019),
    (42.9, -74.42), (42.9634, -74.4109), (42.8675, -74.47),
    (40.74, -73.64),
    (40.7831, -73.9712),
    (43.31, -78.97), (43.3969, -78.972), (43.3256, -78.9341),
    (43.24, -75.43), (43.3357, -75.3502), (43.1585, -75.5288),
    (43.0, -76.2), (42.9936, -76.1988), (43.014, -76.1712),
    (42.85, -77.28), (42.9361, -77.2098), (42.815, -77.1844),
    (41.4, -74.3), (41.4114, -74.3941), (41.4477, -74.2001),
    (43.25, -78.23), (43.3, -78.2743), (43.2886, -78.1854),
    (43.46, -76.27), (43.487, -76.2653), (43.5173, -76.2727),
    (42.66, -75.0), (42.5666, -75.0284), (42.7171, -75.0154),
    (41.43, -73.74),
    (40.742, -73.7694),
    (42.71, -73.51), (42.6241, -73.4122), (42.6497, -73.5621),
    (40.5795, -74.1502),
    (41.15, -73.95),
    (44.45, -75.0), (44.3836, -75.0768), (44.425, -74.9352),
    (43.1, -73.86), (43.0371, -73.9361), (43.1261, -73.8703),
    (42.81, -73.95),
    (42.66, -74.31), (42.6428, -74.4031), (42.6698, -74.3269),
    (42.38, -76.9), (42.4407, -76.915), (42.3183, -76.8097),
    (42.83, -76.83), (42.9109, -76.7693), (42.7416, -76.8044),
    (42.27, -77.38), (42.3368, -77.3559), (42.2979, -77.4301),
    (40.96, -72.69), (40.8938, -72.6109), (40.8888, -72.6118),
    (41.7, -74.77), (41.6114, -74.8241), (41.616, -74.7274),
    (42.17, -76.35), (42.1724, -76.3101), (42.2179, -76.298),
    (42.45, -76.47), (42.5157, -76.4528), (42.5222, -76.4449),
    (41.93, -74.27), (42.0144, -74.1736), (42.0277, -74.2152),
    (43.58, -73.77), (43.6572, -73.8086), (43.5552, -73.6773),
    (43.35, -73.42), (43.2725, -73.4727), (43.3773, -73.4402),
    (43.07, -77.0), (43.1199, -77.0886), (43.0837, -77.0676),
    (41.15, -73.75), (41.0824, -73.7235), (41.1497, -73.8129),
    (42.73, -78.21), (42.6543, -78.2517), (42.7225, -78.1886),
    (42.65, -77.1)
]


# Function to fetch weather data for a single location
def fetch_weather_data(lat, lon):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2005-01-01",
        "end_date": "2005-12-31",
        "daily": [
            'temperature_2m_max','temperature_2m_min',"daylight_duration", "sunshine_duration",'uv_index_max', 'uv_index_clear_sky_max', "rain_sum", "showers_sum",
            "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max"
        ],
        "timezone": "America/New_York"
    }

    response = openmeteo.weather_api(url, params=params)[0]

    daily = response.Daily()
    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        ),
        'temperature_2m_max': daily.Variables(0).ValuesAsNumpy(),
        'temperature_2m_min': daily.Variables(1).ValuesAsNumpy(),
        'daylight_duration': daily.Variables(2).ValuesAsNumpy(),
        'sunshine_duration': daily.Variables(3).ValuesAsNumpy(),
        'uv_index_max': daily.Variables(4).ValuesAsNumpy(),
        'uv_index_clear_sky_max': daily.Variables(5).ValuesAsNumpy(),
        'rain_sum': daily.Variables(6).ValuesAsNumpy(),
        'showers_sum': daily.Variables(7).ValuesAsNumpy(),
        'snowfall_sum': daily.Variables(8).ValuesAsNumpy(),
        'precipitation_hours': daily.Variables(9).ValuesAsNumpy(),
        'wind_speed_10m_max': daily.Variables(10).ValuesAsNumpy(),
        'wind_gusts_10m_max': daily.Variables(11).ValuesAsNumpy(),
        "latitude": [lat] * len(daily.Variables(0).ValuesAsNumpy()),
        "longitude": [lon] * len(daily.Variables(0).ValuesAsNumpy()),
    }
    return pd.DataFrame(data=daily_data)

# Main data collection function with comprehensive rate limiting and early stopping
def collect_weather_data(coordinates, max_retries=3, daily_api_limit=10000):
    dataframes = []
    failed_coordinates = []
    request_count = 0
    hourly_request_count = 0
    daily_request_count = 0
    
    for i, (lat, lon) in enumerate(coordinates, 1):
        # Stop collection BEFORE making a request if daily API limit is reached
        if daily_request_count >= daily_api_limit:
            print(f"Daily API limit of {daily_api_limit} requests reached. Stopping data collection early.")
            break
        
        retries = 0
        success = False
        
        while retries < max_retries and not success:
            try:
                print(f"Fetching weather data for coordinates: {lat}, {lon} (Location {i}/{len(coordinates)}, Attempt {retries + 1})")
                
                # Fetch data for the current location
                df = fetch_weather_data(lat, lon)
                dataframes.append(df)
                
                request_count += 1
                hourly_request_count += 1
                daily_request_count += 1
                success = True
                
                # Add delay every 3 requests
                if request_count % 3 == 0:
                    delay = random.uniform(2.5, 4.5)
                    print(f"Pausing for {delay:.2f} seconds to manage request rate...")
                    time.sleep(delay)
                
                # Check and pause for hourly limit
                if hourly_request_count >= 5000:
                    print("Hourly API request limit reached. Pausing for 3600 seconds (1 hour)...")
                    time.sleep(3600)
                    hourly_request_count = 0
            
            except Exception as e:
                error_message = str(e)
                retries += 1
                
                # Check for rate limit errors
                if 'Minutely API request limit exceeded' in error_message:
                    print("API minutely rate limit reached. Pausing for 65 seconds...")
                    time.sleep(65)  # Pause for slightly over a minute
                elif 'Hourly API request limit exceeded' in error_message:
                    print("API hourly rate limit reached. Pausing for 3600 seconds (1 hour)...")
                    time.sleep(3600)
                    hourly_request_count = 0
                else:
                    print(f"Error: {error_message}")
                    print(f"Waiting 10 seconds before retrying (Attempt {retries}/{max_retries})...")
                    time.sleep(10)
        
        # If all retry attempts fail, add to failed coordinates
        if not success:
            print(f"Failed to fetch data for coordinates {lat}, {lon} after {max_retries} attempts")
            failed_coordinates.append((lat, lon))
    
    # Print failed coordinates and request count if any
    if failed_coordinates:
        print("\nFailed to fetch data for the following coordinates:")
        for coord in failed_coordinates:
            print(coord)
    
    print(f"Total requests made: {daily_request_count}")
    
    return pd.concat(dataframes, ignore_index=True), failed_coordinates

# Collect and save data
try:
    # Create data directory if it doesn't exist
    os.makedirs('../data', exist_ok=True)
    
    # Collect weather data
    combined_dataframe, failed_coords = collect_weather_data(coordinates)
    
    # Save to CSV
    combined_dataframe.to_csv('../data/new-york-weather.csv', mode='a', index=False)
    
    # Save failed coordinates to a separate file
    if failed_coords:
        failed_coords_df = pd.DataFrame(failed_coords, columns=['Latitude', 'Longitude'])
        failed_coords_df.to_csv('../data/failed_coordinates.csv', index=False)
        print(f"Saved {len(failed_coords)} failed coordinates to './data/failed_coordinates.csv'")
    
    print("Weather data collection completed and saved to CSV.")

except Exception as e:
    print(f"An error occurred during data collection: {e}")