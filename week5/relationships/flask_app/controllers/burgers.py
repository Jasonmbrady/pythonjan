from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.Burger import Burger
from flask_app.models.Restaurant import Restaurant

@app.route("/")
def index():
    # all_burgers = Burger.get_all_with_rest()
    rest = Restaurant.read_one_w_burgers()
    return render_template("index.html", restaurant=rest)

@app.route("/burgers/new")
def new_burger():
    restaurants = Restaurant.read_all()
    return render_template("new_burger.html", all_rest = restaurants)

@app.route("/burgers/create", methods=["POST"])
def create_burger():
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "cheese": request.form['cheese'],
        "calories": request.form['calories'],
        "restaurant": request.form['restaurant']
    }
    Burger.create(data)
    return redirect("/")

@app.route("/burgers/<int:num>")
def one_burger(num):
    data = {
        "id": num
    }
    one_burger = Burger.get_one(data)
    return render_template("one_burger.html", burger = one_burger)

@app.route("/burgers/edit/<int:num>")
def edit_burger(num):
    data = {
        "id": num
    }
    one_burger = Burger.get_one(data)
    return render_template("edit_burger.html", burger = one_burger)

@app.route("/burgers/update", methods=["POST"])
def update_burger():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "cheese": request.form['cheese'],
        "calories": request.form['calories']
    }
    id = Burger.update(data)
    return redirect(f"/burgers/{id}")

@app.route("/burgers/delete/<int:num>")
def delete_burger(num):
    data = {
        "id": num
    }
    Burger.delete(data)
    return redirect("/")