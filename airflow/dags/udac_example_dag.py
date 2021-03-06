from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

# default dag properties
default_args = {
    'owner': 'udacity',
    'start_date': datetime(2018, 11, 1),
    'end_date': datetime(2018, 11, 30),
    'depends_on_past': False,
    'catchup': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_retry': False
}

dag = DAG('udac_example_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='@daily'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)


# Load log data from S3 to staging events on redshift 
stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    table="staging_events",
    s3_bucket="udacity-dend",
    s3_key="log_data/{{execution_date.year}}/{{execution_date.month}}/{{execution_date.strftime('%Y-%m-%d')}}-events.json",
    json_option="s3://udacity-dend/log_json_path.json",
    dag=dag
)



# Load log data from S3 to staging songs on redshift 
stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    table="staging_songs",
    s3_bucket="udacity-dend",
    s3_key="song_data/",
    json_option="auto",
    dag=dag
)


# Load songplay data
load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    redshift_conn_id="redshift",
    table_target="songplays",
    table_select="songplay_table_select",
    dag=dag
)


# Load users data
load_users_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    redshift_conn_id="redshift",
    table_target="users",
    table_select="user_table_select",
    truncateData=False,
    dag=dag
)


# Load song data
load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    redshift_conn_id="redshift",
    table_target="songs",
    table_select="song_table_select",
    truncateData=True,
    dag=dag
)

# Load artist data
load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    redshift_conn_id="redshift",
    table_target="artists",
    table_select="artist_table_select",
    truncateData=True,
    dag=dag
)

# Load time data
load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    redshift_conn_id="redshift",
    table_target="time",
    table_select="time_table_select",
    truncateData=False,
    dag=dag
)

# Quality check
run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    redshift_conn_id="redshift",
    table_targets = ["songplays", "users", "songs", "artists", "time"],
    dag=dag
)


end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)


# Pipe line data
start_operator >> stage_events_to_redshift
start_operator >> stage_songs_to_redshift


stage_events_to_redshift >> load_songplays_table
stage_songs_to_redshift >> load_songplays_table


load_songplays_table >> load_users_dimension_table
load_songplays_table >> load_song_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table


load_users_dimension_table >> run_quality_checks
load_song_dimension_table >> run_quality_checks
load_artist_dimension_table >> run_quality_checks
load_time_dimension_table >> run_quality_checks


run_quality_checks >> end_operator