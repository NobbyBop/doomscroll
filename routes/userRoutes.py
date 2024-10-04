import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from validation import *
from data.userData import *

from flask import Blueprint, render_template, request, session, redirect

user_routes = Blueprint("user_routes", __name__, template_folder="templates")

@user_routes.route('/login', methods=["GET", "POST"])
def login():
    #If the user is already logged in, send them home.
    if "uuid" in session:
        return redirect("/home")
    
    # POST
    if request.method == "POST":
        # Retrieve the form data and validate. 
        email = request.form["email"].strip()
        password = request.form["password"].strip()
        try:
            vEmail(email)
            vPassword(password)
        except ValueError as e:
            return render_template("error.html", message=e)
        # If credentials are valid, log the user in.
        try:
            user = loginUser(email, password)
            session["uuid"] = user[0]
            session["email"] = user[1]
            session.permanent = True
            return redirect("/home")
        except ValueError as e:
            return render_template("error.html", message=f"You didn't log in. {e}")
    # GET
    else:
        return render_template("login.html")

@user_routes.route('/register', methods=["GET", "POST"])
def register():
    # If the user is already logged in, send them home.
    if "uuid" in session:
        return redirect("/home")
    
    # POST
    if request.method == "POST":
        # Retrieve the form data and validate. 
        email = request.form["email"].strip()
        password = request.form["password"].strip()
        try:
            vEmail(email)
            vPassword(password)
        except ValueError as e:
            return render_template("error.html", message=e)
        # If creditials are valid, create the new user.
        try:
            createUser(email, password)
            # If successfully created user (should be every time) log them in and redirect home.
            try:
                user = loginUser(email, password)
                session["uuid"] = user[0]
                session["email"] = user[1]
                session.permanent = True
                return redirect("/home")
            except ValueError as e:
                return render_template("error.html", message=f"You registered but didn't log in. {e}")
        except ValueError as e:
            return render_template("register.html", message=f"You didn't register. {e}")
    # GET
    else:
        return render_template("register.html")
    
@user_routes.route('/logout', methods=["GET"])
def logout():
    if "uuid" not in session:
        return redirect("/home")
    else:
        for item in list(session.keys()):
            del session[item]
        return redirect("/home")