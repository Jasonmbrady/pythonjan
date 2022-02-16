from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.restaurant import Restaurant


@app.route('/')
def index():
    all_restaurants = Restaurant.read_all()
    return render_template("index.html", all_rest = all_restaurants)

@app.route('/restaurants/create', methods=['POST'])
def create():
    data = {
        "name": request.form['name']
    }
    if Restaurant.validate_restaurant(data):
        Restaurant.create(data)
        return redirect("/")
    else:
        return redirect("/")

@app.route('/restaurant/<int:id>')
def read_one_with_burgers(id):
    data = {
        'id': id
    }
    this_rest = Restaurant.read_one_with_burgers(data)
    return render_template("restaurant.html", restaurant = this_rest)