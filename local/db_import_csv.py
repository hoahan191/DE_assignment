import pandas as pd

from sqlalchemy import create_engine

 

 

pg_user='postgres'

pg_pass='123PostgreS'

pg_port='5432'

pg_dbname='postgres'

pg_table=''

 

from glob import glob

 

files={}

print('Hello')  

engine = create_engine('postgresql://%s:%s@localhost:5432/%s'%(pg_user, pg_pass, pg_dbname))


for fname in glob('DE_assignment/data/*.csv'):

    print(fname.split("/")[-1][:-4])

    tbname=fname.split("/")[-1][:-4]

    files[tbname] = fname


print(files)
# Offer:

tablename='offers'

filename=files[tablename]

df=pd.read_csv(filename)

df['offer_created_at'] = pd.to_datetime(df['offer_created_at'], utc=True)

df['offer_valid_from'] = pd.to_datetime(df['offer_valid_from'], utc=True)

df['offer_valid_until'] = pd.to_datetime(df['offer_valid_until'], utc=True)

df['offer_total_sale'] = df['offer_total_quantity_kg'] * df['unit_price_nationalcurrency']

df.to_sql(tablename, engine)

 

 

# Order:

tablename='orders'

filename=files[tablename]

df=pd.read_csv(filename)

df['order_created_at'] = pd.to_datetime(df['order_created_at'], utc=True)

df['order_placed_at'] = pd.to_datetime(df['order_placed_at'], utc=True)

 

df.to_sql(tablename, engine)

 

 

# Invite:

tablename='invites'

filename=files[tablename]

df=pd.read_csv(filename)

df['invite_created_at'] = pd.to_datetime(df['invite_created_at'], utc=True)

df['invite_first_viewed_at'] = pd.to_datetime(df['invite_first_viewed_at'], utc=True)

 

df.to_sql(tablename, engine)

 

 

# Deal:

tablename='deals'

filename=files[tablename]

df=pd.read_csv(filename)

df['deal_created_at'] = pd.to_datetime(df['deal_created_at'], utc=True)

df['deal_valid_from'] = pd.to_datetime(df['deal_valid_from'], utc=True)

df['deal_valid_to'] = pd.to_datetime(df['deal_valid_to'], utc=True)

 

df.to_sql(tablename, engine)