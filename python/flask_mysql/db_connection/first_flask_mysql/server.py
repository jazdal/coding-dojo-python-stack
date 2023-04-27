from flask import Flask, render_template, request, redirect, session

# import the class from friend.py
from friend import Friend

app = Flask(__name__)
app.secret_key = 'friends are precious' # modify your secret key accordingly         

# The following sample code blocks need to be created for every route. You may include optional parameters and arguments into the functions as necessary:
@app.route('/')                 
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', all_friends = friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"], 
        "lname": request.form["lname"], 
        "occ": request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/show')
def show_user():
    return render_template('show.html', username = session['username'], useremail = session['useremail'])

# This code block enables automatic reloading of the server whenever you make changes to your code while the server is running:
if __name__ == "__main__":      
    app.run(debug = True)