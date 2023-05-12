from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        if not Dojo.validate_dojo(request.form):
            return redirect("/")
        Dojo.create(request.form)
        return redirect("/results")

@app.route("/results")
def show_info():
    return render_template("results.html", dojos = Dojo.get_all())