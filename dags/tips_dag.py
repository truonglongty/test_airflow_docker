import os
import sys
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

from etl import read_csv_file, insert_data_to_db


start_date = datetime.now()

def start_read_file_csv():
    file_path = r'data\tips.csv'
    header, data = read_csv_file(file_path)
    return header, data

def start_write_csv_to_postgres():
    header, data = start_read_file_csv()
    insert_data_to_db(data)


default_args = {
    'owner': 'longty',
    'start_date': start_date,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}


with DAG('start_dag_etl', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:

    read_csv_task = PythonOperator(
        task_id='start_read_file_csv',
        python_callable=start_read_file_csv,
        retries=1,
        retry_delay=timedelta(seconds=15))

    insert_data_task = PythonOperator(
        task_id='start_write_csv_to_postgres',
        python_callable=start_write_csv_to_postgres,
        retries=1,
        retry_delay=timedelta(seconds=15))
    
    read_csv_task >> insert_data_task