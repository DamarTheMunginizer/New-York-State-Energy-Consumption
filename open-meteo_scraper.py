# imports needed for open-meteo.com data
from retry_requests import retry
import openmeteo_requests
import requests_cache
from requests.adapters import Retry
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
    (40.49, -79.76), (40.49, -78.76), (40.49, -77.76), (40.49, -76.76),
    (40.49, -75.76), (40.49, -74.76), (40.49, -73.76), (40.49, -72.76),
    (41.49, -79.76), (41.49, -78.76), (41.49, -77.76), (41.49, -76.76),
    (41.49, -75.76), (41.49, -74.76), (41.49, -73.76), (41.49, -72.76),
    (42.49, -79.76), (42.49, -78.76), (42.49, -77.76), (42.49, -76.76),
    (42.49, -75.76), (42.49, -74.76), (42.49, -73.76), (42.49, -72.76),
    (43.49, -79.76), (43.49, -78.76), (43.49, -77.76), (43.49, -76.76),
    (43.49, -75.76), (43.49, -74.76), (43.49, -73.76), (43.49, -72.76),
    (44.49, -79.76), (44.49, -78.76), (44.49, -77.76), (44.49, -76.76),
    (44.49, -75.76), (44.49, -74.76), (44.49, -73.76), (44.49, -72.76)
]

# Function to fetch weather data for a single location
def fetch_weather_data(lat, lon):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2024-01-01",
        "end_date": "2024-12-01",
        "daily": [
            "daylight_duration", "sunshine_duration", "rain_sum", "showers_sum",
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
        "daylight_duration": daily.Variables(0).ValuesAsNumpy(),
        "sunshine_duration": daily.Variables(1).ValuesAsNumpy(),
        "rain_sum": daily.Variables(2).ValuesAsNumpy(),
        "showers_sum": daily.Variables(3).ValuesAsNumpy(),
        "snowfall_sum": daily.Variables(4).ValuesAsNumpy(),
        "precipitation_hours": daily.Variables(5).ValuesAsNumpy(),
        "wind_speed_10m_max": daily.Variables(6).ValuesAsNumpy(),
        "wind_gusts_10m_max": daily.Variables(7).ValuesAsNumpy(),
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
    os.makedirs('./data', exist_ok=True)
    
    # Collect weather data
    combined_dataframe, failed_coords = collect_weather_data(coordinates)
    
    # Save to CSV
    combined_dataframe.to_csv('./data/new-york-weather.csv', mode='a', index=False)
    
    # Save failed coordinates to a separate file
    if failed_coords:
        failed_coords_df = pd.DataFrame(failed_coords, columns=['Latitude', 'Longitude'])
        failed_coords_df.to_csv('./data/failed_coordinates.csv', index=False)
        print(f"Saved {len(failed_coords)} failed coordinates to './data/failed_coordinates.csv'")
    
    print("Weather data collection completed and saved to CSV.")

except Exception as e:
    print(f"An error occurred during data collection: {e}")