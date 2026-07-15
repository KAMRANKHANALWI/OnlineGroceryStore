from config.db_config import get_connection


def add_to_cart(cart):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    INSERT INTO Cart
    (
        customer_id,
        product_id,
        quantity
    )
    VALUES(?,?,?)
    """

    cur.execute(query, (cart.customer_id, cart.product_id, cart.quantity))

    conn.commit()
    conn.close()


def view_cart(customer_id):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    SELECT *
    FROM Cart
    WHERE customer_id=?
    """

    cur.execute(query, (customer_id,))

    records = cur.fetchall()

    conn.close()

    return records


def remove_from_cart(cart_id, customer_id):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    DELETE FROM Cart
    WHERE cart_id=?
    AND customer_id=?
    """

    cur.execute(query, (cart_id, customer_id))

    conn.commit()

    deleted_rows = cur.rowcount

    conn.close()

    return deleted_rows


def clear_cart(customer_id):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    DELETE FROM Cart
    WHERE customer_id=?
    """

    cur.execute(query, (customer_id,))

    conn.commit()
    conn.close()
