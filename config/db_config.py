import sqlite3

DB_NAME = "database/grocery_store.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

