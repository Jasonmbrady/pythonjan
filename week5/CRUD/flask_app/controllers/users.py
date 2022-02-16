from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.User import User

@app.route('/')
def index():
    return "Please use /users to see all users or /users/new to create a new user"

@app.route('/users')
def read_all():
    # Call the database, get a list of all users, pass them to HTML to display in a table.
    list = User.get_all()
    return render_template("read_all.html", user_list = list)

@app.route('/users/new')
def new_user():
    return render_template("create.html")

@app.route('/create_user', methods = ["POST"])
def create_user():
    data = {
        "f_name": request.form['f_name'],
        "l_name": request.form["l_name"],
        "email": request.form['email']
    }
    User.create(data)
    return redirect("/users")

@app.route('/users/<int:num>')
def read_one(num):
    data = {
        "id": num
    }
    this_user = User.get_one(data)
    return render_template("read_one.html", user = this_user)

@app.route("/edit_user/<int:num>")
def edit_user(num):
    data = {
        "id": num
    }
    this_user = User.get_one(data)
    return render_template("edit_user.html", user = this_user)

@app.route("/update_user", methods=["POST"])
def update_user():
    data = {
        "id": request.form['id'],
        "f_name": request.form['f_name'],
        "l_name": request.form["l_name"],
        "email": request.form['email']
    }
    id = User.update(data)
    return redirect(f"/users/{id}")

@app.route("/delete/<int:num>")
def delete_user(num):
    data = {
        "id": num
    }
    User.delete(data)
    return redirect("/users")