# import functions from other files
from create_db import create_db
from create_table import create_table
from insert_data import insert_data
from query_table import query_table
from drop_db import drop_db

# Press the green arrow to run the script.
if __name__ == '__main__':
    # Create variable with name of database
    db_name = "my_test_db"

    print('Call Create DB Function')
    create_db(db_name)

    print('Call Create Table Function')
    create_table(db_name)

    print('Call Insert Data Function')
    insert_data(db_name)

    print('Call Query Table Function')
    query_table(db_name)

    # Uncomment if you want to drop the DB
    # print('Delete DB')
    # drop_db(db_name)


