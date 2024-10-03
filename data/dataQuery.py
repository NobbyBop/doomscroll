import sqlite3
con = sqlite3.connect("users.db")
cur = con.cursor()

answer = ""
print("Databse Query Tool:\nEnter SQLite commands in the terminal to view output. 'Q' to quit.")
while(True):
    answer = input("> ")
    if answer.lower() == "q":
        break
    try:
        res = cur.execute(answer)
        print(res.fetchall())
        print("Command issued successfully.")
    except:
        print(f"Command '{answer}' unsuccessful.")
print("Program terminated.")

