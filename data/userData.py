import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from validation import *

import sqlite3, uuid, bcrypt

"""User data functions perform their associated task and then 
return the user object associated with the query."""
def createUser(email, password):
    try:
        vEmail(email)
        vPassword(password)
    except ValueError as e:
        raise ValueError(e)
    
    email = email.lower()

    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("SELECT email FROM users WHERE email=?", (email,))
    if res.fetchone() != None:
        con.close()
        raise ValueError("Email is already in use.")
    
    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    res = cur.execute("INSERT INTO users (uuid, email, password) VALUES (?, ?, ?) RETURNING *", (str(uuid.uuid4()), email, hashpass) )
    user = res.fetchone()
    con.commit()
    con.close()
    return user

def deleteUser(email, password ):
    try:
        vEmail(email)
        vPassword(password)
    except ValueError as e:
        raise ValueError(e)

    email = email.lower() 

    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("SELECT uuid, email, password FROM users WHERE email=?", (email,))
    match = res.fetchone()
    if match == None:
        raise ValueError("Email is not associated with an account.")
    if bcrypt.checkpw(password.encode('utf-8'), match[2]):
        # res = cur.execute("SELECT * from users WHERE email=?", (match[1],))
        res = cur.execute("DELETE FROM users WHERE email=? RETURNING *", (match[1],))
        user = res.fetchone()
        con.commit()
        con.close()
        return user
    else:
        con.close()
        raise ValueError("Invalid credentials.")

def updatePassword(email, newPassword):
    try:
        vEmail(email)
        vPassword(newPassword)
    except ValueError as e:
        raise ValueError(e)

    email = email.lower() 
    hashpass = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())

    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("UPDATE users SET password=? WHERE email=? RETURNING *", (hashpass, email))
    user = res.fetchone()
    if(res == None):
        con.close()
        raise ValueError("Email is not associated with an account.")
    con.commit()
    con.close()
    return user

def loginUser(email, password):
    try:
        vEmail(email)
        vPassword(password)
    except ValueError as e:
        raise ValueError(e)
    email=email.lower()
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("SELECT uuid, email, password FROM users WHERE email=?", (email,))
    match = res.fetchone()
    if match == None:
        con.close()
        raise ValueError("Email is not associated with an account.")
    if bcrypt.checkpw(password.encode('utf-8'), match[2]):
        res = cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = res.fetchone()
        con.close()
        return user
    else:
        con.close()
        raise ValueError("Invalid credentials.")