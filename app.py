from flask import Flask, render_template, redirect, request, session
from validation import *
from data.userData import *
from routes.userRoutes import user_routes
import os


app = Flask(__name__)
app.secret_key = os.environ["Flask-Secret-Key"]
app.register_blueprint(user_routes)

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/home', methods=["GET", "POST"])
def home():
    if "uuid" in session:
        return render_template("home.html", uuid=session["uuid"], email=session["email"])
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)