from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register_user():
    if not User.validate_reg(request.form):
        return redirect("/")
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['f_name'],
        "last_name": request.form['l_name'],
        "email": request.form['email'],
        "password": hashed_pass
    }
    user_id = User.create(data)
    session["uid"] = user_id
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    # retrieve user form DB by email address
    this_user = User.read_by_email({"email": request.form['email']})
    if bcrypt.check_password_hash(this_user.password, request.form['password']):
        session['uid'] = this_user.id
        return redirect("dashboard")
    else:
        flash("Invalid username/password combination")
        return redirect("/")

@app.route("/dashboard")
def dashboard():
    if "uid" not in session:
        flash("Must be logged in")
        return redirect("/")
    this_user = User.read_by_id({"id": session['uid']})
    all_shows = Show.read_all()
    return render_template("dashboard.html", user = this_user, all_shows = all_shows)

@app.route("/logout")
def logout():
    session.pop("uid")
    return redirect("/")