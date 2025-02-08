# Load connection packages
import psycopg2
import os

# Database configuration
ip_address = "http://127.0.0.1:8000"
port = 8000
dbname = "local"
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

def create_connection():
    """Creates a new database connection and returns it."""
    conn = psycopg2.connect(
        dbname = dbname,
        user = user,
        password = password,
        host = ip_address,
        port = port
    )
    return conn

def create_cursor(conn):
    """Creates a new cursor using the specified connection."""
    return conn.cursor()

def close_connection(conn):
    """Closes the database connection."""
    if conn:
        conn.close()
