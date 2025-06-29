from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

#define the dag
with DAG(
    dag_id="example_dag",
    start_date=datetime(2023, 3, 21),
    schedule_interval="@daily",
    catchup=False
) as dag:
    #define task
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo 'Hello World!'",
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo 'This is a test DAG'",
    )

    #define task dependencies
    task_1>>task_2