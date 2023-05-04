from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def reroute():
    return redirect('/users')

@app.route('/users')
def all_users():
    return render_template('index.html', all_users = User.read_all())

@app.route('/users/<id>')
def one_user(id):
    data = {"id": id}
    return render_template('oneuser.html', user = User.read_one(data))

@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('newuser.html')
    else:
        User.create(request.form)
        all_users = User.read_all()
        user_id = [user.id for user in all_users]
        id_num = user_id[len(user_id) - 1]
        return redirect(f'/users/{id_num}')

@app.route('/users/edit/<id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'GET':
        data = {"id": id}
        return render_template('edituser.html', user = User.read_one(data))
    else:
        data = {
            "id": id, 
            "fname": request.form["fname"], 
            "lname": request.form["lname"], 
            "email": request.form["email"]
        }
        User.update(data)
        one_user = User.read_one(data)
        return redirect(f'/users/{one_user.id}')

@app.route('/users/destroy/<id>')
def delete_user(id):
    data = {"id": id}
    User.destroy(data)
    return redirect('/users')