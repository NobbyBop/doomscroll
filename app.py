from flask import Flask, render_template, redirect, request
from validation import *
from data.users import *
app = Flask(__name__)

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            vEmail(email)
            vPassword(password)
        except ValueError as e:
            return render_template("error.html", message=e)
        if loginUser(email, password):
            return render_template("error.html", message="You logged in.")
        else:
            return render_template("error.html", message="You didn't log in.")
    else:
        return render_template("login.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)