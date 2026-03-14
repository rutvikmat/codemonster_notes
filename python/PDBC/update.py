def update_user_email(connection, user_id, new_email):
    cursor = connection.cursor()
    sql = "UPDATE users SET email = %s WHERE id = %s"
    val = (new_email, user_id)
    
    cursor.execute(sql, val)
    connection.commit()
    
    print(f"{cursor.rowcount} record(s) updated.")
    cursor.close()