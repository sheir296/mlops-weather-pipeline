import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    # Load preprocessed data
    df = pd.read_csv('data/processed/weather_data.csv')
    
    # Feature engineering (e.g., predicting temperature using wind speed and humidity)
    X = df[['Wind Speed', 'Humidity']]
    y = df['Temperature']
    
    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save the model
    joblib.dump(model, 'models/weather_model.pkl')
    print("Model trained and saved as 'models/weather_model.pkl'")
