# Apply forecasting for all counties
counties = data.columns[1:]  # Skip 'Date' column
all_forecasts = pd.DataFrame()

for county in counties:
    print(f"Forecasting for {county}...")
    forecast = forecast_county(data, county)
    forecast.rename(columns={'yhat': county}, inplace=True)
    
    # Merge forecasts into a single dataframe
    if all_forecasts.empty:
        all_forecasts = forecast
    else:
        all_forecasts = pd.merge(all_forecasts, forecast, on='ds', how='outer')

# Save the combined forecast to a CSV file
output_file = 'Counties_Forecast.csv'
all_forecasts.rename(columns={'ds': 'Date'}, inplace=True)
all_forecasts.to_csv(f'data/{output_file}', index=False)

print(f"Combined forecast saved to {output_file}.")

# Defining the function
def extract_data (file,start_date,end_date):
    df = pd.read_csv(f'data/{file}')
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', inplace = True)
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    return df.to_csv(f'data/load_data_from_{start_date}_to_{end_date}.csv')