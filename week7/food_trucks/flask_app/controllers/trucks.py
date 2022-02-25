from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.Truck import Truck

@app.route("/trucks/new")
def new_truck():
    return render_template("new_truck.html")

@app.route("/trucks/create", methods=["POST"])
def create_truck():
    if not Truck.validate(request.form):
        return redirect("/trucks/new")
    data = {
        "name": request.form['name'],
        "type": request.form['type'],
        "user_id": session["user_id"]
    }
    Truck.create(data)
    return redirect("/dashboard")

@app.route("/trucks/<int:id>")
def view_truck(id):
    Truck.read_truck_with_likes({"id": id})
    return render_template("view_truck.html", truck = Truck.read_truck_with_likes({"id": id}))

@app.route("/trucks/delete/<int:id>")
def delete_truck(id):
    Truck.delete({"id": id})
    return redirect("/dashboard")

@app.route("/trucks/edit/<int:id>")
def edit_truck(id):
    return render_template("edit_truck.html", truck = Truck.read_by_id({"id": id}))

@app.route("/trucks/update", methods=["POST"])
def update_truck():
    if not Truck.validate(request.form):
        return redirect(f"/trucks/edit/{request.form['id']}")
    Truck.update(request.form)
    return redirect("/dashboard")

@app.route("/trucks/like/<int:id>")
def like_truck(id):
    # Go to db, add truck id and user id to like table.
    data = {
        "truck_id": id,
        "user_id": session["user_id"]
    }
    Truck.like_truck(data)
    return redirect("/dashboard")