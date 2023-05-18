from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_app.models.message2 import Message2

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect("/")
    new_user = {
        "first_name": request.form["first_name"], 
        "last_name": request.form["last_name"], 
        "email": request.form["email"], 
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
    id = User.create(new_user)

    if not id:
        flash("Email already taken.", "register")
        return redirect("/")
    session["user_id"] = id
    return redirect("/wall")

@app.route("/login", methods=["POST"])
def login():
    data = {"email": request.form["email"]}
    user = User.get_by_email(data)

    if (not user) or (not bcrypt.check_password_hash(user.password, request.form["password"])):
        flash("Invalid Email / Password", "login")
        return redirect("/")
    session["user_id"] = user.id
    return redirect("/wall")

@app.route("/wall")
def dashboard():
    if "user_id" not in session:
        return redirect("/unauthorized")
    data = {"id": session["user_id"]}
    return render_template("dashboard.html", user = User.get_one(data), users = User.get_all(), messages = Message.get_user_messages(data), sent_messages = Message2.get_sent_messages(data))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/unauthorized")
def unauthorized():
    return render_template("unauthorized.html")