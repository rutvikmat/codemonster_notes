def read_users(connection):
    cursor = connection.cursor(dictionary=True) # Returns results as dictionaries
    cursor.execute("SELECT * FROM users")
    
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row['id']}, Name: {row['name']}, Email: {row['email']}")
    
    cursor.close()