import sqlite3, uuid, bcrypt
from validation import *

def initDB():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE users(uuid, email, password)")
    cur.execute("CREATE TABLE interests(uuid, interest)")
    cur.execute("CREATE TABLE prompts(uuid, text, suggestions, completed)")
    cur.execute("CREATE TABLE completed(uuid, date, prompt, description, image)")

def createUser(email, password):
    try:
        vEmail(email)
        vPassword(password)
    except ValueError as e:
        raise ValueError(e)
    
    email = email.lower()

    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("SELECT email FROM user WHERE email=?", (email,))
    if(res.fetchone() != None):
        raise ValueError("Email is already in use.")
    
    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cur.execute("INSERT INTO user (uuid, email, password) VALUES (?, ?, ?)", (uuid.uuid4(), email, hashpass) )
    con.commit()
    con.close()

def clear_table(table_name):
    con = sqlite3.connect("users.db")  # Replace with your database name
    cur = con.cursor()

    # Execute the DELETE statement
    cur.execute(f"DELETE FROM {table_name}")

    con.commit()  # Commit the changes
    con.close()   # Close the connection


# initDB()

# Example usage
clear_table("users")  # Replace with your table name
clear_table("interests")  # Replace with your table name
clear_table("prompts")  # Replace with your table name
clear_table("completed")  # Replace with your table name

createUser("nicholasmirigliani@gmail.com", "P@ssW0r4")
createUser("nicholasmirigliani@gmail.com", "P@ssW0r4")

con = sqlite3.connect("users.db")
cur = con.cursor()
res = cur.execute(f"SELECT email FROM users")
print(res.fetchall())
