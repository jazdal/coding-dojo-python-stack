from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def reroute():
    return redirect('/dojos')

@app.route('/dojos', methods=['GET', 'POST'])
def new_dojo():
    if request.method == 'GET':
        return render_template('dojos.html', dojos = Dojo.get_all())
    else:
        Dojo.create(request.form)
        return redirect('/')

@app.route('/dojos/<int:id>')
def show_ninjas_from_dojo(id):
    data = {"id": id}
    return render_template('ninjas_in_dojos.html', dojos = Dojo.get_ninjas_from_dojo(data), one_dojo = Dojo.get_one(data))

@app.route('/ninjas', methods=['GET', 'POST'])
def new_ninja():
    if request.method == 'GET':
        return render_template('ninja_form.html', dojos = Dojo.get_all())
    else:
        Ninja.create(request.form)
        return redirect(f"/dojos/{request.form['dojo_id']}")