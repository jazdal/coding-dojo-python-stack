from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.restaurant import Restaurant
from flask_app.models.burger import Burger

@app.route('/')
def show():
    return render_template('index.html', all_restaurants = Restaurant.show_all())

@app.route('/burgers/<id>')
def show_burgers(id):
    data = {"id": id}
    return render_template('burgers.html', burgers = Burger.show_burgers_from_restaurants(data), restaurant = Restaurant.show_one(data))

@app.route('/new_restaurant')
def restaurant_form():
    return render_template('new_restaurant.html')

@app.route('/new_burger')
def burger_form():
    return render_template('new_burger.html', all_restaurants = Restaurant.show_all())

@app.route('/new/restaurant', methods=['POST'])
def add_restaurant():
    Restaurant.create(request.form)
    return redirect('/')

@app.route('/new/burger', methods=['POST'])
def add_burger():
    Burger.create(request.form)
    print(request.form)
    return redirect('/')

@app.route('/burgers/destroy/<id>')
def delete_burger(id):
    data = {"id": id}
    Burger.destroy(data)
    print(id)
    return redirect('/')