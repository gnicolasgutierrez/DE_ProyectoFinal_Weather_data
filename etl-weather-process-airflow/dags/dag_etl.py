import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from modules import get_defaultairflow_args, extraer_data, transformar_data, cargar_data, send_email

with DAG(
    dag_id="weather_etl",
    default_args=get_defaultairflow_args(),
    description="ETL pipeline to extract, transform, and load weather data",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    args = [f"{datetime.now().strftime('%Y-%m-%d %H')}", os.getcwd()]

    # Tasks
    # 1. Extraction
    task_extract = PythonOperator(
        task_id="extract_weather_data",
        python_callable=extraer_data,
        op_args=args,
    )

    # 2. Transformation
    task_transform = PythonOperator(
        task_id="transform_weather_data",
        python_callable=transformar_data,
        op_args=args,
    )

    # 3. Loading
    task_load_data = PythonOperator(
        task_id="load_weather_data",
        python_callable=cargar_data,
        op_args=args,
    )

    # 4. Send email alert
    task_send_email = PythonOperator(
        task_id="send_email_alert",
        python_callable=send_email,
    )

    # Task dependencies
    task_extract >> task_transform >> task_load_data >> task_send_email
