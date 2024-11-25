from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import weather_data_collection
import weather_data_preprocessing
import weather_model_training

# Define default arguments for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 25),
    'retries': 1,
}

# Instantiate the DAG
dag = DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='A pipeline to collect, preprocess and train ML models for weather data',
    schedule_interval='@daily',  # Runs once a day
)

# Define tasks
collect_data_task = PythonOperator(
    task_id='collect_weather_data',
    python_callable=weather_data_collection.collect_weather_data,
    dag=dag,
)

preprocess_data_task = PythonOperator(
    task_id='preprocess_weather_data',
    python_callable=weather_data_preprocessing.preprocess_data,
    dag=dag,
)

train_model_task = PythonOperator(
    task_id='train_weather_model',
    python_callable=weather_model_training.train_model,
    dag=dag,
)

# Set task dependencies
collect_data_task >> preprocess_data_task >> train_model_task
