import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123PostgreS")
cur = conn.cursor()
cur.execute('SELECT * FROM deals')
