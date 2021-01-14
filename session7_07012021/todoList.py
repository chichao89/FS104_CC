import psycopg2
import csv
from psycopg2 import Error

#create toDoListObject
#to do list table  - id, title description,duedate,priority
toDoList = (
    (1,"Clean the Cabinets","Clean 3 Cabinets in the room","09/01/2021","High"),
    (2,"Buy Ingredients", "Buy Pork and Spinach for Dinner Cooking","10/01/2021","High"),
    (3,"Get Letters","Collect the letters from the post office","10/01/2021","Medium"),
    (4,"Buy Gifts","Buy presents for nephew","19/01/2021","Low")
)

try:
    connection = psycopg2.connect( 
                                    user = "postgres",
                                    password = "123",
                                    host = "localhost",
                                    port = "5432",
                                    database = "FS103"
                                ) 
    connection.autocommit = True
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE IF NOT EXISTS ToDoList
                            (ID INT NOT NULL,
                            Title TEXT NOT NULL,
                            Description TEXT NOT NULL,
                            Due_Date Date NOT NULL,
                            Priority TEXT NOT NULL,
                            CONSTRAINT pk_ToDoList PRIMARY KEY (ID)
                            );'''

    cursor.execute(create_table_query)
    print("Table Created Successfully")

    # query = "INSERT into ToDoList(ID,Title,Description,Due_Date,Priority) VALUES(%s,%s,%s,%s,%s)"
    # cursor.executemany(query,toDoList)
    # count = cursor.rowcount
    # print(count,"records inserted successfully")

    select_query = "Select * from ToDoList where priority = 'High' and due_date = current_date"
    cursor.execute(select_query)
    columns = [i[0] for i in cursor.description]
    data_fetch = cursor.fetchall()
    
    print("Creating File")
    with open('toDoList.csv', 'w', newline='') as f_output:
        writer = csv.writer(f_output)
        writer.writerow(columns)
        for row in data_fetch:
            writer.writerow(row)

    #with open('toDoList.csv', 'w', newline='') as f_output:
        #   cursor.copy_to(f_output,data_fetch,sep=",")
    #     writer = csv.writer(f_handle)
    #     header = ['ID', 'title', 'Description', 'Due_Date','Priority']
    #     writer.writerow(header)
    # # Iterate over `data`  and  write to the csv file
    #     for row in data_fetch:
    #         writer.writerow(row)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
