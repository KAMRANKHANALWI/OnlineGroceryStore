from config.db_config import get_connection


def insert_customer(customer):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    INSERT INTO Customer
    (
        customer_id,
        login_id,
        customer_name,
        address,
        contact_number
    )
    VALUES(?,?,?,?,?)
    """

    cur.execute(
        query,
        (
            customer.customer_id,
            customer.login_id,
            customer.customer_name,
            customer.address,
            customer.contact_number,
        ),
    )

    conn.commit()
    conn.close()


def update_customer(customer):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    UPDATE Customer
    SET
        customer_name = ?,
        address = ?,
        contact_number = ?
    WHERE customer_id = ?
    """

    cur.execute(
        query,
        (
            customer.customer_name,
            customer.address,
            customer.contact_number,
            customer.customer_id,
        ),
    )

    conn.commit()
    conn.close()


def get_customer_by_id(customer_id):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    SELECT *
    FROM Customer
    WHERE customer_id=?
    """

    cur.execute(query, (customer_id,))

    customer = cur.fetchone()

    conn.close()

    return customer


def get_customer_by_email(email):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    SELECT c.*, l.email
    FROM Customer c
    JOIN Login l
        ON c.login_id = l.login_id
    WHERE l.email=?
    """

    cur.execute(query, (email,))

    customer = cur.fetchone()

    conn.close()

    return customer
