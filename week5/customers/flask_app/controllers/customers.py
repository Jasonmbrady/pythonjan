from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.customer import Customer

@app.route("/")
def index():
    customer_list = Customer.read_all()
    return render_template("index.html", all_customers=customer_list)