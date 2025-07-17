import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Convert recordDate to datetime
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])

    # Create a copy of the DataFrame shifted by 1 day
    prev_weather = weather.copy()
    prev_weather['recordDate'] = prev_weather['recordDate'] + pd.Timedelta(days=1)

    # Merge current weather with previous day's weather
    merged = pd.merge(weather, prev_weather, on='recordDate', suffixes=('', '_prev'))

    # Filter where today's temp is higher than yesterday's temp
    result = merged[merged['temperature'] > merged['temperature_prev']]

    # Return only the id column
    return result[['id']]
