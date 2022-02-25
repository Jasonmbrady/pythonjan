from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.User import User
from flask_app.models.Truck import Truck
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate(request.form):
        return redirect("/")
    data = {
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session["user_id"] = User.create(data)
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    this_user = User.get_by_email({"email": request.form['email']})
    if not this_user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect("/")
    session["user_id"] = this_user.id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Must be logged in to do that")
        return redirect("/")
    
    return render_template("dashboard.html", user = User.get_by_id({"id": session["user_id"]}), all_trucks = Truck.read_all())

@app.route("/logout")
def logout():
    session.pop("user_id")
    return redirect("/")