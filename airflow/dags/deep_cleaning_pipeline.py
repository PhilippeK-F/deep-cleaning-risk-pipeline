from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="deep_cleaning_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["cleaning", "risk", "pipeline"],
) as dag:

    generate_raw_missions = BashOperator(
        task_id="generate_raw_missions",
        bash_command="python /opt/airflow/scripts/generate_missions.py",
    )

    transform_missions = BashOperator(
        task_id="transform_missions",
        bash_command="python /opt/airflow/scripts/transform_missions.py",
    )

    load_to_postgres = BashOperator(
        task_id="load_to_postgres",
        bash_command="python /opt/airflow/scripts/load_to_postgres.py",
    )

    generate_raw_missions >> transform_missions >> load_to_postgres