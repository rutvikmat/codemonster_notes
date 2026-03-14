import mysql.connector
from mysql.connector import Error

try:
    # 1. Establish the connection
    connection = mysql.connector.connect(
        host='localhost',
        database='pdbc',
        user='root',
        password='root@123'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
        
        cursor = connection.cursor()
        
        # 2. Execute a query
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print(f"You're connected to database: {record}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 3. Always close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")