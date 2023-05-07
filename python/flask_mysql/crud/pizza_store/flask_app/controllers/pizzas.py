from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.pizza import Pizza

@app.route("/")
def index():
    return render_template("index.html", pizzas = Pizza.get_all())