from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import pizza
from flask_app.models import customer

@app.route("/")
def index():
    return render_template("index.html", pizzas = pizza.Pizza.get_all(), customers = customer.Customer.get_all())

@app.route("/process", methods=['POST'])
def process():
    data = {
        "pt": request.form['pizza_type'], 
        "pc": request.form['pizza_crust'], 
        "psz": request.form['pizza_size'], 
        "ps": request.form['pizza_sauce'], 
        "t": request.form['amount_of_toppings'], 
        "customer_id": request.form['customer_id']
    }
    if request.form["which_form"] == "create":
        pizza.Pizza.create(data)
    else:
        data['id'] = request.form['id']
        pizza.Pizza.update(data)
    return redirect("/")

@app.route("/pizzas/<int:id>")
def edit_form(id):
    return render_template("edit.html", id = id)

@app.route("/pizzas/delete/<int:id>")
def destroy_pizza(id):
    pizza.Pizza.delete({"id": id})
    return redirect("/")