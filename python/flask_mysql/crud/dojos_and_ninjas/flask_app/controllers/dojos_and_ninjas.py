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
        Dojo.save(request.form)
        return redirect('/')

@app.route('/dojos/<int:id>')
def show_ninjas_from_dojo(id):
    data = {"id": id}
    return render_template('ninjas_in_dojos.html', ninjas = Dojo.get_ninjas_from_dojo(data), dojo = Dojo.get_one(data))

@app.route('/ninjas', methods=['GET', 'POST'])
def new_ninja():
    if request.method == 'GET':
        return render_template('ninja_form.html', dojos = Dojo.get_all())
    else:
        Ninja.save(request.form)
        dojos = Dojo.get_all()
        for dojo in dojos:
            if int(dojo.id) == int(request.form['dojo_id']):
                return redirect(f'/dojos/{int(dojo.id)}')
            else:
                return redirect('/')