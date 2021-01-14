import psycopg2 #import the module
from psycopg2 import Error

try:
    con = psycopg2.connect(database="assignment3", user="postgres", password="123", host="127.0.0.1", port="5432") #define the connection to connect to postgres

    print("Database opened successfully")

    cur = con.cursor()
    cur.execute("select * from bank.employee")
    rows = cur.fetchall()
    for row in rows:
        print("Record =", rows[0])

    print("Operation done successfully")
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (con):
        cur.close()
        con.close()
        print("PostgreSQL connection is closed")
