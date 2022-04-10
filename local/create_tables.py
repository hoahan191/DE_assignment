import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    - Creates and connects to the covestrodb
    - Returns the connection and cursor to covestrodb
    Args:
        cur (psycopg.cursor): a database cursor
        conn (psycopg2.connection): a database connection
    """
    
    # connect to default database
    try: 
        conn = psycopg2.connect("host=localhost dbname=covestrodb user=postgres password=123PostgreS")
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
        
    try: 
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get curser to the Database")
        print(e)
        
    conn.set_session(autocommit=True)
    
    
    # create sparkify database with UTF8 encoding
    try: 
        cur.execute("DROP DATABASE IF EXISTS covestrodb")
    except psycopg2.Error as e:
        print("Error: Could not drop Database")
        print(e)
    
    try:
        cur.execute("CREATE DATABASE covestrodb WITH ENCODING 'utf8' TEMPLATE template0")
        print("Error: Could not create Database")
        print(e)

    # close connection to default database
    conn.close()    
    
    # connect to covestro database
    try: 
        conn = psycopg2.connect("host=localhost dbname=covestrodb user=postgres password=123PostgreS")
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    
    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get curser to the Database")
        print(e)
        
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    Args:
        cur (psycopg.cursor): a database cursor
        conn (psycopg2.connection): a database connection
    """
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Could not drop table from query: {}".format(query))
            print(e)
    

def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Could not create table from query: {}".format(query))
            print(e)



def main():
    """
    - Drops (if exists) and Creates the covestro database. 
    
    - Establishes connection with the covestro database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    Args:
        cur (psycopg.cursor): a database cursor
        conn (psycopg2.connection): a database connection
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    cur.close():
    conn.close()


if __name__ == "__main__":
    main()