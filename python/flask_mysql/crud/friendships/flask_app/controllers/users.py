from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect("/friendships")

@app.route("/friendships", methods=['GET', 'POST'])
def process_friendships():
    if request.method == 'GET':
        return render_template("friendships.html", friendships = User.get_friendships(), users = User.get_all())
    else:
        User.create(request.form)
        return redirect("/")

@app.route("/make_friends", methods=['POST'])
def make_friends():
    User.add_friend(request.form)
    return redirect("/")