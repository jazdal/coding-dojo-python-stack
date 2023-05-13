from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.email import Email

@app.route("/", methods=['GET', 'POST'])
def submit_email():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        if not Email.validate_email(request.form):
            return redirect("/")
        Email.create(request.form)
        return redirect("/success")

@app.route("/success")
def display_emails():
    return render_template("emails.html", emails = Email.get_all(), last_email = Email.get_last())

@app.route("/delete/<id>")
def delete_email(id):
    data = {"id": id}
    Email.delete(data)
    return redirect("/success")