from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.tweet import Tweet
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/register', methods=["POST"])
def register_user():
    if not User.is_valid(request.form):
        return redirect('/')
    hash_pwd = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "password": hash_pwd
    }
    session["user_id"] = User.create(data)
    return redirect("/dashboard")
    
@app.route('/users/login', methods=["POST"])
def login_user():
    db_user = User.read_one_by_email({"email": request.form['email']})
    print(db_user)
    if not db_user or not bcrypt.check_password_hash(db_user.password, request.form['password']):
        flash("Invalid email/password")
        return redirect("/")

    session["user_id"] = db_user.id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id": session["user_id"]
    }
    logged_user = User.read_one(data)
    all_tweets = Tweet.read_all()
    return render_template("dashboard.html", user = logged_user, tweets = all_tweets)

@app.route("/logout")
def logout():
    session.pop("user_id")
    return redirect("/")