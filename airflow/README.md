# **Project: Data Pipelines with Airflow**

## **Introduction**
Sparkify - a music streaming startup, has used their user base and song database and moved their data warehouse to a data lake. They decided to monitoring them to data warehouse ETL pipelines. 

This ETL pipeline loads song and log data in JSON format from S3, processes them into analytics table(s) in a star schema using Spark then finally writes those table(s) into partitioned parquet files on S3.

## **Overview**
This project builds a data pipeline using Apache Airflow to create a scheduler which automates and monitors the running of an ETL pipeline serving Sparkify service.

Configure the task dependencies so that after the dependencies are set, the graph view displays
![](https://r1100713c1104575xreacttogg4cfw.udacity-student-workspaces.com/files/home/workspace/airflow/DAG_graph.jpeg)

## **Datasets***

Song Data Path: ***s3://udacity-dend/song_data***

Log Data Path: ***s3://udacity-dend/log_data Log Data***

## **Structure of folder and files***
There are three major components for the project:

### 1. The **dags** has all the imports and task templates in place,
### 2. The **operators** folder with operator templates 
### 3. The **helper** class for the SQL transformations

About the file: 
+ ```README.md``` : currently opening file

+ ```DAG_graph.png``` : this is graph of DAG workflow

+ ```dags/udac_example_dag.py``` : this is Main DAG

+ ```create_tables.sql``` : this is SQL script to build Redshift tables

+ ```plugins/helpers/sql_queries.py``` : this is select statements used to populate tables

+ ```plugins/operators/data_quality.py``` : this is DAG operator used for data quality checks

+ ```plugins/operators/load_dimensions.py``` : this is DAG operator used to populate dimension tables in a star schema

+ ```plugins/operators/load_fact.py``` : this is DAG operator used to populate fact tables

+ ```plugins/operators/stage_redshift.py``` : this is DAG operator to populate staging tables from source files

## **How project work**
- Add the following Airflow connections:
    * AWS credential
    * Connection to Redshift cluster

- In the workspace, after finishing the code, you can run this command to start: 
```/opt/airflow/start.sh```
