from flask import Flask, render_template, redirect, request
from validation import *
from data.userData import *
from routes.userRoutes import user_routes


app = Flask(__name__)

app.register_blueprint(user_routes)

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)