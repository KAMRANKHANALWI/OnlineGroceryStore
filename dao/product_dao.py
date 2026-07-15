from config.db_config import get_connection


def insert_product(product):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    INSERT INTO Product
    VALUES (?,?,?,?,?,?,?)
    """

    cur.execute(
        query,
        (
            product.product_id,
            product.product_name,
            product.description,
            product.company_name,
            product.category,
            product.price,
            product.stock_quantity,
        ),
    )

    conn.commit()
    conn.close()


def update_product(product):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    UPDATE Product
    SET
        product_name=?,
        description=?,
        company_name=?,
        category=?,
        price=?,
        stock_quantity=?
    WHERE product_id=?
    """

    cur.execute(
        query,
        (
            product.product_name,
            product.description,
            product.company_name,
            product.category,
            product.price,
            product.stock_quantity,
            product.product_id,
        ),
    )

    conn.commit()
    conn.close()


def get_product_by_id(product_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * 
        FROM Product
        WHERE product_id=?
        """,
        (product_id,),
    )

    product = cur.fetchone()

    conn.close()

    return product


def get_all_products():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM Product
    """)

    products = cur.fetchall()

    conn.close()

    return products


def update_product_stock(product_id, new_quantity):

    conn = get_connection()

    cur = conn.cursor()

    query = """
    UPDATE Product
    SET stock_quantity=?
    WHERE product_id=?
    """

    cur.execute(query, (new_quantity, product_id))

    conn.commit()
    conn.close()
