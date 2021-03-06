import connect_db as db


def query_table(db_name):
    # get connection instance
    conn = db.connect_db(db_name)
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM EMPLOYEE")

    # Retrieve query results
    records = cur.fetchall()
    print(records)
