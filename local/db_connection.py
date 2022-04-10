import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123PostgreS")
cur = conn.cursor()
# cur.execute('SELECT * FROM deals')
# #one = cur.fetchone()
# all = cur.fetchall()

drop_table = ["DROP TABLE IF EXISTS orders;",
"DROP TABLE IF EXISTS deals;",
"DROP TABLE IF EXISTS invites;",
"DROP TABLE IF EXISTS offers;",
]

for line in drop_table:
    cur.execute(line)
    print("OK")

