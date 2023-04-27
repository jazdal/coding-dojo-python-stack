from flask import Flask, render_template, request, redirect, session
from users import User

app = Flask(__name__)
app.secret_key = 'users_cr'

@app.route('/')
def reroute():
    return redirect('/users')

@app.route('/users')
def all_users():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users = users)

@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('newuser.html')
    
    else:
        data = {
            "fname": request.form["fname"], 
            "lname": request.form["lname"], 
            "email": request.form["email"]
        }
        User.save(data)
        return redirect('/users')

if __name__ == "__main__":
    app.run(debug = True)