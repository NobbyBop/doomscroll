import sqlite3
from data.userData import *
def initDB():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE users(uuid, email, password)")
    cur.execute("CREATE TABLE interests(uuid, interest)")
    cur.execute("CREATE TABLE prompts(uuid, text, suggestions, completed)")
    cur.execute("CREATE TABLE completed(uuid, date, prompt, description, image)")


# Test
# initDB()
def clear_table(table_name):
    con = sqlite3.connect("users.db")  # Replace with your database name
    cur = con.cursor()

    # Execute the DELETE statement
    cur.execute(f"DELETE FROM {table_name}")

    con.commit()  # Commit the changes
    con.close()   # Close the connection

clear_table("users")  
clear_table("interests")  
clear_table("prompts") 
clear_table("completed") 

try:
    createUser("nicholasmirigliani@gmail.com", "P@ssW0r4")
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT uuid, email, password FROM users")
    print(res.fetchall())
    cur.close()
    con.close()
except ValueError as e:
    print(e)

# try:
#     updatePassword("nicholasmirigliani@gmail.com", "newPa@ss5")
#     con = sqlite3.connect("users.db")
#     cur = con.cursor()
#     res = cur.execute(f"SELECT uuid, email, password FROM users")
#     print(res.fetchall())
#     cur.close()
#     con.close()
# except ValueError as e:
#     print(e)

# try:
#     deleteUser("nicholasmirigliani@gmail.com", "P@ssW0r4")
#     con = sqlite3.connect("users.db")
#     cur = con.cursor()
#     res = cur.execute(f"SELECT uuid, email, password FROM users")
#     print(res.fetchall())
#     cur.close()
#     con.close()
# except ValueError as e:
#     print(e)

# try:
#     deleteUser("nicholasmirigliani@gmail.com", "newPa@ss5")
#     con = sqlite3.connect("users.db")
#     cur = con.cursor()
#     res = cur.execute(f"SELECT uuid, email, password FROM users")
#     print(res.fetchall())
#     cur.close()
#     con.close()
# except ValueError as e:
#     print(e)
