from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "data_engineer",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    "social_sentiment_pipeline",
    default_args=default_args,
    description="Airflow orchestration for social sentiment ingestion + processing",
    schedule_interval=None,
    catchup=False,
    tags=["sentiment", "streaming", "kafka", "spark"]
) as dag:

    ingest_facebook = BashOperator(
        task_id="ingest_facebook",
        bash_command="python -m ingestion.facebook_ingest",
        cwd="/opt/airflow/sanlam-social-media-sentiments"
    )

    ingest_twitter = BashOperator(
        task_id="ingest_twitter",
        bash_command="python -m ingestion.twitter_ingest",
        cwd="/opt/airflow/sanlam-social-media-sentiments"
    )

    ingest_instagram = BashOperator(
        task_id="ingest_instagram",
        bash_command="python -m ingestion.instagram_ingest",
        cwd="/opt/airflow/sanlam-social-media-sentiments"
    )

    ingest_linkedin = BashOperator(
        task_id="ingest_linkedin",
        bash_command="python -m ingestion.linkedin_ingest",
        cwd="/opt/airflow/sanlam-social-media-sentiments"
    )

    spark_process = BashOperator(
        task_id="run_spark_stream",
        bash_command="python -m processing.spark_stream",
        cwd="/opt/airflow/sanlam-social-media-sentiments"
    )

    export_csv = BashOperator(
        task_id="export_sentiment_csv",
        bash_command="python processing/export_results.py",
        cwd="/opt/airflow/sanlam-social-media-sentiments"
    )

    ingest_facebook >> ingest_twitter >> ingest_instagram >> ingest_linkedin >> spark_process >> export_csv