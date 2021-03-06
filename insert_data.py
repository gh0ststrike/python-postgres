import connect_db as db


def insert_data(db_name):
    # get connection instance
    conn = db.connect_db(db_name)
    # Setting auto commit false
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing SQL queries to INSERT a record into the database.
    cursor.execute('''INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) 
   VALUES ('Shiba', 'Inu', 25, 'F', 200)''')

    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")

    # Closing the connection
    conn.close()
