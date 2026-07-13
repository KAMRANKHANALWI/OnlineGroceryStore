from config.db_config import get_connection


def insert_login(login):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO Login
    (
        email,
        password,
        user_type,
        status
    )
    VALUES(?,?,?,?)
    """

    cur.execute(query, (login.email, login.password, login.user_type, login.status))

    conn.commit()

    login_id = cur.lastrowid

    conn.close()

    return login_id


def get_login_by_email(email):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    SELECT *
    FROM Login
    WHERE email = ?
    """

    cur.execute(query, (email,))
    record = cur.fetchone()

    conn.close()

    return record


def validate_login(email, password):
    conn = get_connection()

    cur = conn.cursor()

    query = """
    SELECT * 
    FROM Login
    WHERE email=?
    AND password=?
    """

    cur.execute(query, (email, password))

    record = cur.fetchone()

    conn.close()

    return record

