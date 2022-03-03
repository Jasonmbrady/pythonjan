from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models.User import User
import requests
import os
import json


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    logged_user = User.get_by_username({"username": request.form['username']})
    if not logged_user:
        flash("Invalid Username/Password combination")
        redirect("/")
    session['user_id'] = logged_user.id
    return redirect("/dashboard")

@app.route("/register", methods=["POST"])
def register():
    session['user_id'] = User.create(request.form)
    return redirect("/dashboard")
    
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("You must be logged in!")
        return redirect("/")
    this_user = User.get_by_id({"id":session['user_id']})
    r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?lat={this_user.lat}&lon={this_user.lon}&units=imperial&appid={os.environ.get('WEATHER_API_KEY')}")
    w = json.dumps(r.json())
    weather = json.loads(w)
    return render_template("dashboard.html", user = this_user, weather = weather)

@app.route("/logout")
def logout():
    session.pop("user_id")
    return redirect("/")