# Data Engineering Assignment

### Hoa Han - Junior Data Engineer

#### Project Summary
In this assignment, 

The project follows the follow steps:
* Step 1: Scope the Project and Gather Data
* Step 2: Explore and Assess the Data
* Step 3: Define the Data Model
* Step 4: Run ETL to Model the Data
* Step 5: Complete Project Write Up


### Step 1: Scope the Project and Gather Data

#### 1.1 Scope 
##### 1.1.1 Format of data
- CSV file

##### 1.1.2 Programing language, library and frameworks
- Python: language using for processing data, including:
    * pandas: using for explorating data on small dataset
    * PySpark: using for preprocessing data on large dataset

#### 1.2 Describe and Gather Data 
#### 1.2.1 Dataset 
| Dataset | Format | Description |
| -------- | -------- | -------- |
| [deals](https://github.com/hoahan191/DE_assignment/blob/main/data/deals.csv)     | CSV     | This data is collected .     |
| [invites](https://github.com/hoahan191/DE_assignment/blob/main/data/invites.csv) | CSV    | This dataset is taken |
| [offers](https://github.com/hoahan191/DE_assignment/blob/main/data/offers.csv)  | CSV    | This data is collected from [|
| [orders](https://github.com/hoahan191/DE_assignment/blob/main/data/orders.csv)| CSV    | This data is taken from |

##### 1.2.2 Gathering data
After explorating invites data, only column **invite_first_viewed_at** has 62% nan value

## Requirements
However, we do have a couple of requirements:
- Prepare your solution in a local git repo on your computer, commiting code as if you were working as part of a real team.
- Write a README.md that explains your solution, so we can focus on the less obvious parts during the discussion.
- The system should be designed to run automatically, without manual input.
- Do have a database where you load the raw data into, do transformations in and feed the report form
- Data quality must be tested. Requiring manual input in case of a failing data quality check is fine.
- Use Apache Airflow for orchestration, following relevant best practices.
- NICE TO HAVE (not mandatory): Deploy your work in a cloud environment. Deployment automation and infrastructure as code are not required.
