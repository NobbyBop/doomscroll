import sqlite3, uuid, bcrypt
from validation import *

def initDB():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE user(uuid, email, password)")
    cur.execute("CREATE TABLE interests(uuid, interest)")
    cur.execute("CREATE TABLE prompt(uuid, text, suggestions, completed)")
    cur.execute("CREATE TABLE completed(uuid, prompt, description, image)")

def createUser(username, password):
    try:
        vUser(username)
        vPassword(password)
    except ValueError as e:
        raise ValueError(e.message)
    
    username = username.lower()

    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute(f"SELECT username FROM user WHERE username='{username}'")
    if(res.fetchall() != None):
        raise ValueError("Username is unavailable.")
    return 
