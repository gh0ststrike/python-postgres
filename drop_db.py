import connect_db as db


def drop_db(db_name):
    # get connection instance
    conn = db.connect_db(db_name)

    conn.autocommit = True

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("DROP DATABASE " + db_name)

    # Closing the connection
    conn.close()
