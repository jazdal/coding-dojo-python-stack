# PYTHON / FLASK / BOOTSTRAP / SQL FULL-STACK PROJECT SETUP GUIDE
### Personal Notes by: Jasper Dalawangbayan

This is a simple guide I made for creating a full-stack Python / Flask / Bootstrap / SQL project template for web development, based on my learnings in the *Coding Dojo Python Web Development* Bootcamp.

### Recommended Tools:
- Visual Studio Code (VS Code)
- The latest version of Python

1. *If you haven't done so yet:* Install the virtual environment tool *pipenv* using pip. Typing the following command in the terminal will globally install the virtual environment tool *pipenv*, so you only need to do this ONCE for all your projects, and never again:

    pip install pipenv

2. Create a folder for your project.

3. Inside your project folder, create the following subfolders:
    - templates
    - static

4. Inside the static subfolder, create the following subfolders. This is where you will place any additional assets (CSS settings, JS scripts, images, etc.) that you will use in your project accordingly:
    - css
    - img
    - js

5. Navigate into your project folder in the terminal. Then type the following command in the terminal to install Flask and PyMySQL (you need to do this for every new project you create):

    pipenv install PyMySQL flask

In order to successfully install PyMySQL and Flask, your project folder needs to be located in the same drive as your Python files and pipenv. Otherwise, you will get error messages, and PyMySQL and Flask won't be installed.

You can confirm that Flask is installed after you see two files created in your Flask project folder: *Pipfile* and *Pipfile.lock*. Pipfile contains the packages installed, whereas Pipfile.lock contains the specific details on what version is being used.

6. Inside the *templates* subfolder, create an *index.html* file with the following boilerplate code, which you can later modify. This already includes the CDN (Content Delivery Network) links to the Bootstrap CSS and JS settings that will allow the use of Bootstrap features in the project:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">
        <title>Document Title</title>
    </head>
    <body>
        <div>
            <!--Your HTML code goes here-->
                <!--For using images in your HTML, follow the format below-->
                <img src="{{ url_for('static', filename='img/my_img.png') }}" alt="my_img">
        </div>

        <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    </body>
</html>
```

7. Inside your project folder, create a *mysqlconnection.py* file, and include the following code:

```python
# a cursor is the object we use to interact with the database
import pymysql.cursors

# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost', 
                                    user = 'root', 
                                    password = 'root', 
                                    db = db, 
                                    charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor, autocommit = True)
        # establish the connection to the database
        self.connection = connection

    # the method to query the database
    def query_db(self, query, data = None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid

                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result

                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()

            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            
            finally:
                # close the connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

8. Inside your project folder, create a class that is modeled after your SQL table using Python OOP. Example code below *(friend.py)*:

```python
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"

        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)

        # Create an empty list to append our instances of friends
        friends = []

        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends 
    
    # class method to save our friend to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"

        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db(query, data)
```

9. Inside your project folder, create a *server.py* file, and include the following code:

```python
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
    return render_template('index.html')

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
```

10. To run the Flask project, navigate to the Flask project folder in the terminal and type the following commands:

    pipenv shell
    python server.py

11. To test that your project is working, open the web browser and go to *localhost:5000*, and type in any specific routes you made in your code.

12. To stop the server / virtual environment from running, press *Ctrl-C*, then type *exit* in the terminal.