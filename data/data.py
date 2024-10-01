import sq3lite

def initDB():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE users(uuid, email, password)")
    cur.execute("CREATE TABLE interests(uuid, interest)")
    cur.execute("CREATE TABLE prompts(uuid, text, suggestions, completed)")
    cur.execute("CREATE TABLE completed(uuid, date, prompt, description, image)")