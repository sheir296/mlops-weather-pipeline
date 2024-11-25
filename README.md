# MLOps Weather Prediction Pipeline

This project demonstrates an MLOps pipeline using Airflow, DVC, and machine learning models to predict weather conditions based on collected weather data.

## Project Structure

- `dags/`: Contains the Airflow DAGs to automate the pipeline.
- `data/`: Contains the raw and processed weather data.
- `models/`: Contains the trained machine learning models.
- `weather_data_collection.py`: Script to collect weather data using an API.
- `weather_data_preprocessing.py`: Script to preprocess the collected weather data.
- `weather_model_training.py`: Script to train the machine learning model for weather prediction.
- `dvc.yaml`: DVC pipeline configuration for managing data and model versioning.

## Setup

1. Clone the repository and install dependencies:
