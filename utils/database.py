import mysql.connector
import pandas as pd

# MySQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="predictive_maintenance"
)

cursor = connection.cursor()

# Function to save prediction
def save_prediction(
    air_temp,
    process_temp,
    rpm,
    torque,
    tool_wear,
    failure_probability,
    prediction
):

    query = """
    INSERT INTO prediction_history
    (
        air_temp,
        process_temp,
        rpm,
        torque,
        tool_wear,
        failure_probability,
        prediction
    )

    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        air_temp,
        process_temp,
        rpm,
        torque,
        tool_wear,
        failure_probability,
        prediction
    )

    cursor.execute(query, values)

    connection.commit()


# Fetch prediction history
def get_prediction_history():

    query = """
    SELECT *
    FROM prediction_history
    ORDER BY created_at DESC
    """

    df = pd.read_sql(query, connection)

    return df