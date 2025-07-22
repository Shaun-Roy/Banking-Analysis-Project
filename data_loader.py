import mysql.connector
import pandas as pd

def load_customer_data():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="banking_case"
    )

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM customers")

    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=columns)

    cursor.close()
    cnx.close()

    return df


