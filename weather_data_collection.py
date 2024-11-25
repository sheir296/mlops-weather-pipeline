import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Load API key from .env
API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def collect_weather_data():
    params = {
        'q': 'London,GB',  # Example city (Change it if you need)
        'cnt': 5,  # Get 5 days of forecast
        'appid': API_KEY,
        'units': 'metric',  # Get temperature in Celsius
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Extracting relevant data
    weather_data = []
    for entry in data['list']:
        weather_data.append({
            'DateTime': entry['dt_txt'],
            'Temperature': entry['main']['temp'],
            'Humidity': entry['main']['humidity'],
            'Wind Speed': entry['wind']['speed'],
            'Weather Condition': entry['weather'][0]['description'],
        })
    
    # Save the raw data to a CSV file
    df = pd.DataFrame(weather_data)
    df.to_csv('data/raw/weather_data.csv', index=False)
    print("Weather data collected and saved to 'data/raw/weather_data.csv'")
