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
| [deals Dataset](DE_assignment/data/deals.csv)     | SAS     | This data is collected from the [US National Tourism and Trade Office](https://www.trade.gov/). This dataset contains immigration data of individuals coming to USA in the year 2016. A data dictionary is included in the workspace. immigration_data_sample.csv contains the sample data.     |
| [invites Dataset](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/information/) | CSV    | This dataset is taken from [Kaggle](https://www.kaggle.com/). This dataset contains information of temperatures by city for each country.|
| [offers Dataset](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)  | CSV    | This data is collected from [OpenSoft](https://public.opendatasoft.com/). This dataset contains information about the demographics of all US cities and census-designated places with a population greater or equal to 65,000. This data comes from the US Census Bureau's 2015 American Community Survey.|
| [orders Dataset](https://datahub.io/core/airport-codes#data)| CSV    | This data is taken from [Our Airports](http://ourairports.com/data/). It is a simple table of airport codes and corresponding cities. It contains the list of all airport codes, the attributes are identified in datapackage description. Some of the columns contain attributes identifying airport locations, other codes (IATA, local if exist) that are relevant to identification of an airport.|

##### 1.2.2 Gathering data

For **I94 Immigration Data**, in order to reading faster, we will convert all data to **parquet format**

After explorating SAS data, only **data of June** have difference columns so we will read June's data as a different dataframe then join with the rest.