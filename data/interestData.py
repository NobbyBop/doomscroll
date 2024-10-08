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
    try:
        vInterest(interest)
    except ValueError as e:
        raise ValueError(e)
    
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    res = cur.execute("SELECT from users WHERE uuid = ?", uuid)
    if(res.fetchone() == None):
        raise ValueError("User with specified uuid does not exist.")
    res = cur.execute("INSERT INTO interests (uuid,interest) VALUE (?, ?)", (uuid, interest))
    
    
    