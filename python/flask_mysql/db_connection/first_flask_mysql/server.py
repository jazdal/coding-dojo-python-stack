from flask import Flask, render_template, request, redirect, session

# import the class from friend.py
from friend import Friend

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # modify your secret key accordingly         

# The following sample code blocks need to be created for every route. You may include optional parameters and arguments into the functions as necessary:
@app.route('/')                 
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', all_friends = friends)

# The following code block is included if your project has a form for user input and registration:
@app.route('/users', methods=['POST'])
def create_user():
    print(f'Got post info')
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    # NEVER render a template on a POST request
    # Instead, redirect to either the index or another route:
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', username = session['username'], useremail = session['useremail'])

# This code block enables automatic reloading of the server whenever you make changes to your code while the server is running:
if __name__ == "__main__":      
    app.run(debug = True)