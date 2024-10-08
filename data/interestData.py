import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from validation import *

import sqlite3, uuid
"""
This file works with the "interests" table, which simply stores an interest with its corresponding uuid of the user whose interest it is.
"""
def addInterest(uuid, interest):
    # Creates a new interest for user with uuid.
    vInterest(interest)
    con = sqlite3.connect("users.db")
    cur = con.cursor()

    ##PROBLEM HERE.
    res = cur.execute("SELECT * FROM users WHERE uuid=?", (uuid,))

    
    if(res.fetchone() == None):
        raise ValueError("User with specified uuid does not exist.")
    res = cur.execute("INSERT INTO interests (uuid,interest) VALUE (?, ?) RETURNING *", (uuid, interest))
    interest = res.fetchone()
    return interest

def deleteInterest(uuid, interest):
# Deletes an interest from a user.
    vInterest(interest)
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("DELETE FROM interests WHERE (uuid, interest) = (?, ?) RETURNING *", (uuid, interest))
    if(res.fetchone() == None):
        raise ValueError("Could not find specified interest for spcified user.")
    interest = res.fetchone()
    return interest
    
    
    