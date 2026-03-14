import mysql.connector
from mysql.connector import Error


def setup_table(conn):
    """Creates a sample table for this example."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            position VARCHAR(100),
            salary DECIMAL(10, 2)
        )
    """)
    conn.commit()
    cursor.close()

def create_connection():
    """Establishes connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         # Change if your username is different
            password='root@123', # Replace with your actual password
            database='pdbc'   # Replace with your schema name
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
def create_employee(conn, name, pos, sal):
    """CREATE: Adds a new record."""
    cursor = conn.cursor()
    query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, pos, sal))
    conn.commit()
    print(f"✅ Created: {name} (ID: {cursor.lastrowid})")
    cursor.close()



db_conn = create_connection()
if db_conn and db_conn.is_connected():
    setup_table(db_conn)

    # 1. CREATE
    create_employee(db_conn, "Alice Smith", "Developer", 75000)
    create_employee(db_conn, "Bob Jones", "Designer", 65000)
