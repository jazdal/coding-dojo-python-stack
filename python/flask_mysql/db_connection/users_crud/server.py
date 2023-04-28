from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)
app.secret_key = 'users_crud'

@app.route('/')
def reroute():
    return redirect('/users')

@app.route('/users')
def all_users():
    return render_template('index.html', all_users = User.get_all())

@app.route('/users/<id>')
def one_user(id):
    data = {"id": id}
    return render_template('oneuser.html', user = User.get_one(data))

@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('newuser.html')
    else:
        User.save(request.form)
        all_users = User.get_all()
        user_id = [user.id for user in all_users]
        id_num = user_id[len(user_id) - 1]
        return redirect(f'/users/{id_num}')

@app.route('/users/edit/<id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'GET':
        data = {"id": id}
        return render_template('edituser.html', user = User.get_one(data))
    else:
        data = {
            "id": id, 
            "fname": request.form["fname"], 
            "lname": request.form["lname"], 
            "email": request.form["email"]
        }
        User.update(data)
        one_user = User.get_one(data)
        return redirect(f'/users/{one_user.id}')

@app.route('/users/destroy/<id>')
def delete_user(id):
    data = {"id": id}
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug = True)