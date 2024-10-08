import re

def vUser(user):
    if not re.match("^[a-zA-Z][a-zA-Z0-9]*(?:_[a-zA-Z0-9]+)*{4,14}$", user):
        raise ValueError("Username must meet requirements.")
    return True

def vEmail(email):
    if not re.match("^[^@]+@[^@]+\\.[^@]+$", email):
        raise ValueError("Invalid email.")
    return True

def vPassword(password):
    if not re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,24}$", password):
        raise ValueError("Password must meet requirements.")
    return True

def vInterest(interest):
    if not isinstance(interest, str):
        raise ValueError("Interest must be a string.")
    if len(interest)< 3:
        raise ValueError("Interest must be at least 3 characters.")
    return True
