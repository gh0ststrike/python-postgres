import connect_db as db


def create_db(db_name):
    # get connection instance
    conn = db.initial_connect_db()

    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %(value)s", {'value': db_name})
    exists = cursor.fetchone()
    if not exists:
        cursor.execute("CREATE DATABASE " + db_name)
        print("Database created successfully........")
    else:
        print("Database already exists........")

    # Closing the connection
    conn.close()
