import mysql.connector
from mysql.connector import Error

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

# --- CRUD FUNCTIONS ---

def create_employee(conn, name, pos, sal):
    """CREATE: Adds a new record."""
    cursor = conn.cursor()
    query = "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, pos, sal))
    conn.commit()
    print(f"✅ Created: {name} (ID: {cursor.lastrowid})")
    cursor.close()

def read_employees(conn):
    """READ: Fetches all records."""
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    print("\n--- Current Employee List ---")
    for row in rows:
        print(f"[{row['id']}] {row['name']} - {row['position']} (${row['salary']})")
    cursor.close()

def update_salary(conn, emp_id, new_salary):
    """UPDATE: Modifies an existing record."""
    cursor = conn.cursor()
    query = "UPDATE employees SET salary = %s WHERE id = %s"
    cursor.execute(query, (new_salary, emp_id))
    conn.commit()
    print(f"✅ Updated ID {emp_id}: New salary set to ${new_salary}")
    cursor.close()

def delete_employee(conn, emp_id):
    """DELETE: Removes a record."""
    cursor = conn.cursor()
    query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(query, (emp_id,))
    conn.commit()
    print(f"✅ Deleted ID {emp_id}")
    cursor.close()

# --- MAIN EXECUTION ---

db_conn = create_connection()

if db_conn and db_conn.is_connected():
    setup_table(db_conn)

    # 1. CREATE
    create_employee(db_conn, "Alice Smith", "Developer", 75000)
    create_employee(db_conn, "Bob Jones", "Designer", 65000)

    # 2. READ
    read_employees(db_conn)

    # 3. UPDATE (Updating Alice's salary)
    update_salary(db_conn, 1, 80000)

    # 4. DELETE (Deleting Bob)
    delete_employee(db_conn, 2)

    # Final Check
    read_employees(db_conn)

    db_conn.close()
    print("\nConnection closed.")