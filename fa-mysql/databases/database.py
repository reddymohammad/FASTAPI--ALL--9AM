import mysql.connector


def get_db_connection():
    dbcon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Reddybasha@123",
        database="db19"
    )

    return dbcon