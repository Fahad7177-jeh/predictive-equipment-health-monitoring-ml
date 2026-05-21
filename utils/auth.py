from utils.database import connection

cursor = connection.cursor()

# Register User
def register_user(username, password):

    query = """
    INSERT INTO users (username, password)
    VALUES (%s, %s)
    """

    values = (username, password)

    cursor.execute(query, values)

    connection.commit()


# Login User
def login_user(username, password):

    query = """
    SELECT *
    FROM users
    WHERE username=%s
    AND password=%s
    """

    values = (username, password)

    cursor.execute(query, values)

    user = cursor.fetchone()

    return user