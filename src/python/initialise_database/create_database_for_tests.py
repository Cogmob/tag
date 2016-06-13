from python.initialise_database.initialise_database import initialise_database
import sqlite3

def up():
    return get_database_in_memory(), {}

def down(conn, cursor):
    cursor.close()
    conn.close()

def get_database_in_memory():
    conn = sqlite3.connect(':memory:')
    conn.isolation_level = None
    cursor = conn.cursor()
    initialise_database(conn)
    return conn, cursor
