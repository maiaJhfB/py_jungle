import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost", "root", 'Escola2015!!')


def create_database(connection, query):
    dbcursor = connection.cursor()
    try:
        dbcursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database('Local instance MySQL80','USE Py_Jungle;')
