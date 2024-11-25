import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data():
    # Load raw weather data
    df = pd.read_csv('data/raw/weather_data.csv')
    
    # Clean data (e.g., handling missing values or unnecessary columns)
    df = df.dropna()  # Drop rows with missing values
    
    # Standardize temperature and wind speed for modeling
    scaler = StandardScaler()
    df['Temperature'] = scaler.fit_transform(df[['Temperature']])
    df['Wind Speed'] = scaler.fit_transform(df[['Wind Speed']])
    
    # Save processed data
    df.to_csv('data/processed/weather_data.csv', index=False)
    print("Weather data preprocessed and saved to 'data/processed/weather_data.csv'")
