from asyncio import run_coroutine_threadsafe
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.Restaurant import Restaurant

@app.route("/restaurants/new")
def new_rest():
    return render_template("new_rest.html")

@app.route("/restaurants/create", methods=["POST"])
def create_rest():
    data = {
        "name": request.form['name']
    }
    Restaurant.create(data)
    return redirect("/")