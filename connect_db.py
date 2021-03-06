# Postgres driver
import psycopg2


def initial_connect_db():
    # establishing the connection
    return psycopg2.connect(database="postgres", user='postgres',
                            password='welcome333', host='127.0.0.1', port='5432')


def connect_db(db_name):
    # establishing the connection
    return psycopg2.connect(database=db_name, user='postgres',
                            password='welcome333', host='127.0.0.1', port='5432')
