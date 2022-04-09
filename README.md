# Data Engineering Assignment

### Hoa Han - Junior Data Engineer

#### Project Summary
In this assignment, I will base on data of Immigration in US and other related datasources like temperature, population etc. to design a data warehouse schema shipping with an ETL pipeline. This data warehouse purpose is to provide data for analytic teams to get some insight from the data such as:

+ Which time of the year have most people immigrating to New York State?
+ Find out the average sex ratio of top ten states with the most immigrants in 2016
+ Find out immigrants coming from hot country (temp > 30°C)

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

