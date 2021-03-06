import connect_db as db


# get connection instance
def create_table(db_name):
    conn = db.connect_db(db_name)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    conn.autocommit = True

    # Droping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Creating table as per requirement
    sql = '''CREATE TABLE EMPLOYEE (
      FIRST_NAME CHAR(20) NOT NULL,
      LAST_NAME CHAR(20),
      AGE INT,
      SEX CHAR(1),
      INCOME FLOAT
   )'''
    cursor.execute(sql)
    print("Table created successfully........")

    # Closing the connection
    conn.close()
