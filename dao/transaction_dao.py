from config.db_config import get_connection


def save_transaction(
    customer_id, payment_method, total_amount, no_of_items, transaction_date
):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    INSERT INTO Transactions
    (
        customer_id,
        payment_method,
        total_amount,
        no_of_items,
        transaction_date
    )
    VALUES(?,?,?,?,?)
    """

    cur.execute(
        query,
        (customer_id, payment_method, total_amount, no_of_items, transaction_date),
    )

    conn.commit()

    transaction_id = cur.lastrowid

    conn.close()

    return transaction_id


def save_transaction_item(transaction_id, product_id, quantity, price):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    INSERT INTO Transaction_Items
    (
        transaction_id,
        product_id,
        quantity,
        price
    )
    VALUES(?,?,?,?)
    """

    cur.execute(query, (transaction_id, product_id, quantity, price))

    conn.commit()

    conn.close()
