from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.show import Show

@app.route("/shows/new")
def new_show():
    return render_template("new_show.html")

@app.route("/shows/create", methods=["POST"])
def create_show():
    data = {
        "band_name": request.form['band_name'],
        "date": request.form['date'],
        "description": request.form['description'],
        "user_id": session['uid']
    }
    Show.create(data)
    return redirect("/dashboard")

@app.route("/shows/edit/<int:id>")
def edit_show(id):
    show_to_edit = Show.read_by_id({"id": id})
    return render_template("edit_show.html", show = show_to_edit)

@app.route("/shows/update", methods=["POST"])
def update_show():
    data = {
        "id": request.form['id'],
        "band_name": request.form['band_name'],
        "date": request.form['date'],
        "description": request.form['description'],
        "user_id": request.form["user_id"]
    }
    Show.update(data)
    return redirect("/dashboard")

@app.route("/shows/delete/<int:id>")
def delete_show(id):
    Show.delete({"id": id})
    return redirect("/dashboard")

@app.route("/shows/<int:id>")
def view_show(id):
    this_show = Show.read_by_id({"id": id})
    return render_template("view_show.html", show=this_show)