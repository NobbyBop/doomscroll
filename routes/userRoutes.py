import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from validation import *
from data.userData import *

from flask import Blueprint, render_template, request

user_routes = Blueprint("user_routes", __name__, template_folder="templates")
@user_routes.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            vEmail(email)
            vPassword(password)
        except ValueError as e:
            return render_template("error.html", message=e)
        try:
            loginUser(email, password)
            return render_template("error.html", message="You logged in.")
        except ValueError as e:
            return render_template("error.html", message="You didn't log in.")
    else:
        return render_template("login.html")
