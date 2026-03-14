def delete_user(connection, user_id):
    cursor = connection.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    val = (user_id,) # Note the comma: MySQL connector expects a tuple
    
    cursor.execute(sql, val)
    connection.commit()
    
    print(f"{cursor.rowcount} record(s) deleted.")
    cursor.close()