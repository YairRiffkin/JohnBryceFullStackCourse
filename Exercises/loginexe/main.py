from flask import Flask, render_template, redirect, request, session, flash
import json

app = Flask(__name__)
app.secret_key = "super duper secure password"

@app.route("/")
def hompepage():
    return render_template("home.html", session = session)

@app.route("/about")
def about():
    return render_template("about.html", session = session)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        with open("users.json", "r") as f:
            users = json.load(f)
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            session["username"] = username
            return redirect("/")
        else:
            flash("The username or password is incorrect", "error")
    return render_template("login.html", session = session)
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html", session = session)

app.run(debug= True)
