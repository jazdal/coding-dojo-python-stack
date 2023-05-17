from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["fname"], 
        "last_name": request.form["lname"], 
        "birthday": request.form["bday"], 
        "region": request.form["region"], 
        "email": request.form["email"], 
        "password": pw_hash, 
        "os": request.form["os"]
    }
    user_id = User.create(data)
    session["user_id"] = user_id
    session["first_name"] = request.form["fname"]
    return redirect("/dashboard")

@app.route("/login", methods=['POST'])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email / Password", "password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email / Password", "password")
        return redirect("/")
    session["user_id"] = user_in_db.id
    session["first_name"] = user_in_db.first_name
    return redirect("/dashboard")

@app.route("/dashboard")
def welcome():
    if session:
        return render_template("welcome.html", user = session["first_name"])
    else:
        return redirect("/unauthorized")

@app.route("/logout")
def destroy_session():
    session.clear()
    return redirect("/")

@app.route("/unauthorized")
def display_error():
    return render_template("unauthorized.html")