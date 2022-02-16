from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.burger import Burger

@app.route("/burgers/delete/<int:id>")
def delete_burger(id):
    data = {
        "id": id
    }
    Burger.delete(data)
    return redirect("/")

@app.route("/burgers/edit/<int:id>")
def edit_burger(id):
    data = {
        "id": id
    }
    this_burger = Burger.read_one(data)
    return render_template("edit_burger.html", burger = this_burger)

@app.route("/burgers/update", methods=["POST"])
def update_burger():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat']
    }
    Burger.update(data)
    return redirect("/")
