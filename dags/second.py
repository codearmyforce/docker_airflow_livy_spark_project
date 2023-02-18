from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Ravi',
    'start_date': days_ago(2)
}

second_dag = DAG(
    dag_id='second_dag',
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False
)


start_task = DummyOperator(task_id='start_task1', dag=second_dag)

livy_spark_submit = BashOperator(
    task_id='spark-submit',
    bash_command="spark-submit.sh",
    dag=second_dag
)

end_task = DummyOperator(task_id='end_task', dag=second_dag)

start_task >> livy_spark_submit >> end_task

