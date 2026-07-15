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

    # CART TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cart(
            cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            product_id TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            
            FOREIGN KEY(customer_id)
                REFERENCES Customer(customer_id),
                
            FOREIGN KEY(product_id)
                REFERENCES Product(product_id)
    )    
    """)

    # TRANSACTIONS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions(
            transactions_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            payment_method TEXT NOT NULL,
            total_amount REAL NOT NULL,
            no_of_items INTEGER NOT NULL,
            transaction_date TEXT NOT NULL,
            
            FOREIGN KEY(customer_id)
                REFERENCES Customer(customer_id)
    )
    """)

    # TRANSACTION ITEMS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transaction_Items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_id INTEGER NOT NULL,
            product_id TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,

            FOREIGN KEY(transaction_id)
                REFERENCES Transactions(transaction_id),

            FOREIGN KEY(product_id)
                REFERENCES Product(product_id)
    );
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
