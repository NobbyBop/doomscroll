from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def redirect_home():
    return redirect('/home')

@app.route('/login', methods=["GET"])
def login():
    return render_template("login.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)