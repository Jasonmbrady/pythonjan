from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.tweet import Tweet

@app.route("/tweets/create", methods=["POST"])
def create_tweet():
    data = {
        "text": request.form['text'],
        "users_id": session["user_id"]
    }
    Tweet.create(data)
    return redirect("/dashboard")