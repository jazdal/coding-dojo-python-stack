from flask_app import app
from flask import render_template
from flask_app.models import customer

@app.route("/customers")
def show_customers():
    customers = customer.Customer.get_all()
    return render_template("customers.html", customer_list = customers)