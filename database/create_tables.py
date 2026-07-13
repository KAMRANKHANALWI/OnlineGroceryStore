from config.db_config import get_connection
from utils.constants import ADMIN, ACTIVE, DEFAULT_ADMIN_EMAIL, DEFAULT_ADMIN_PASSWORD


def create_tables():
    conn = get_connection()

    cursor = conn.cursor()

    # LOGIN TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Login(
        login_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        user_type TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # CUSTOMER TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer(
        customer_id INTEGER PRIMARY KEY,
        login_id INTEGER,
        customer_name TEXT NOT NULL,
        address TEXT,
        contact_number TEXT,
        FOREIGN KEY(login_id) REFERENCES Login(login_id)
    )
    """)

    # PRODUCT TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Product(
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            description TEXT,
            company_name TEXT,
            category TEXT,
            price REAL,
            stock_quantity INTEGER
    )
    """)

    conn.commit()

    insert_default_admin(cursor)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")


def insert_default_admin(cursor):

    cursor.execute(
        """
        SELECT * 
        FROM Login
        WHERE email = ?
        """,
        (DEFAULT_ADMIN_EMAIL,),
    )

    admin = cursor.fetchone()

    if admin is None:
        cursor.execute(
            """
        INSERT INTO Login
        (
            email,
            password,
            user_type,
            status
        )
        VALUES(?,?,?,?)
        """,
            (DEFAULT_ADMIN_EMAIL, DEFAULT_ADMIN_PASSWORD, ADMIN, ACTIVE),
        )

        print("Default Admin Created.")
