import psycopg2
from psycopg2 import Error

users = (
    (5,'mery','walker', 45),
    (6,'elsa','princess',21)
)


try:
    #connect to an existing database
    connection = psycopg2.connect( 
               user = "postgres",
                password = "123",
                #host = "127.0.0.1",
                host = "localhost",
                port = "5432",
                database = "FS103"
                            )
    if(connection):
        print("Connection success")
        cursor = connection.cursor()
        
        # create_table_query = '''CREATE TABLE IF NOT EXISTS Users
        # (ID INT PRIMARY KEY NOT NULL,
        # first_name character varying(50) NOT NULL,
        # last_name character varying(50) NOT NULL,
        # age INT NOT NULL);'''

        #execute a command 
        #cursor.execute(create_table_query)
        #print("Table Created Successfully")
        #insert records into table
        # insert_table_query = '''
        #     INSERT INTO users(ID,first_name,last_name,age)
        #     Values (3, 'Johnny', 'Walker' ,35),
        #            (4, 'Lisa', 'Chan',30);'''
        # cursor.execute(insert_table_query)
        # print("to check records")
        # count = cursor.rowcount
        # connection.commit()
        #print(count,"records Inserted Successfully")        
        # query = "INSERT into users(ID,first_name,last_name,age) VALUES(%s,%s,%s,%s)"
        # cursor.executemany(query,users)
        # count = cursor.rowcount
        # connection.commit()
        # print(count,"records inserted successfully")

        select_query = "Select * from users order by first_name asc"
        cursor.execute(select_query)
        data_fetch = cursor.fetchall()
        # record = [record for record in data_fetch]
        for row in data_fetch:
            print("data from table",row)
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")