# FULL-STACK WEB DEVELOPMENT PROJECT SETUP GUIDE
### Notes by: Jasper Dalawangbayan

This is my personal guide / walkthrough for setting-up a full-stack (frontend to backend) project template for web development, based on my learnings in the **Coding Dojo Python Stack Web Development** Bootcamp.

### Technologies:
The following programming languages and libraries are going to be used for this type of project development, and requires previous knowledge and experience in their use:
- HTML5 (Frontend structure)
- CSS3 (Frontend formatting)
- JavaScript (Frontend scripting)
- Bootstrap (CSS and JS framework for frontend)
- Python (Backend scripting)
- Flask with Jinja (Web application framework for Python)
- MySQL (Backend relational database system)
- PyMySQL (Interface for connecting to a MySQL database server from Python)

### Recommended Tools:
Download and install these tools first prior to starting a project. As a pre-requisite, you need to be familiar with the use of these tools beforehand. If not, it is recommended that you first go through the documentation / tutorials / trainings on their usage as they won't be covered here:

- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) - Latest Version: v.1.78.1
- [Python](https://www.python.org/downloads/) - Latest Version: v.3.11.3
- [Boostrap](https://getbootstrap.com/docs/5.3/getting-started/download/) - Latest Version: v.5.3.0-alpha3
- [MySQL Community Server (including MySQL Workbench)](https://dev.mysql.com/downloads/mysql/) - Latest Version: v.8.0.33

### Sample Project: Books

### Steps:

**Part I: Backend**
1. *In case you haven't done yet:* Install the virtual environment tool *pipenv* using pip. Typing the following command in the terminal will globally install *pipenv*, so you only need to do this ONCE for all your projects, and never again:

    pip install pipenv

2. Create a folder for your project.
    > books

3. Create a *schema* folder inside your project.
    > books
        > schema

4. Using MySQL, create a schema and ERD for your project. Afterwards, forward-engineer the schema. Save your MySQL schema/ERD into the *schema* folder.
    > books
        > schema
            > books_schema.mwb
            > books_schema.sql

5. Navigate into your project folder in the terminal. Then type the following command in the terminal to install PyMySQL, Flask, and Flask-Bcrypt (you need to do this for every new project you create):

    ...\project_name> pipenv install PyMySQL flask flask-bcrypt

In order to successfully install everything, your project folder needs to be located in the same drive as your Python files and pipenv. Otherwise, you will get error messages, and the libraries won't be installed.

You can confirm that PyMySQL, Flask, and Flask-Brcypt are installed after you see two files created in your project folder: *Pipfile* and *Pipfile.lock*. Pipfile contains the packages installed, whereas Pipfile.lock contains the specific details on what version is being used.

Please note that if you are using Git, every time you clone your project repository into another folder / computer, you will need to reinstall PyMySQL, Flask, and Flask-Bcrypt even though the project folder already includes the *Pipfile* and *Pipfile.lock* files.

5. Inside your project folder, create a subfolder called *flask_app*:
    > books
        > flask_app
        > schema
            > books_schema.mwb
            > books_schema.sql
        > Pipfile
        > Pipfile.lock

6. Create a *__init__.py* file inside the *flask_app* subfolder:
    > books
        > flask_app
            > __init__.py
        > schema
            > books_schema.mwb
            > books_schema.sql
        > Pipfile
        > Pipfile.lock

Inside the *__init__.py* file, type the following Python code, and save:

```python (__init__.py)
from flask import Flask
app = Flask(__name__)
app.secret_key = "Put your secret key here"
```

7. Create the *config*, *controllers*, *models*, *static*, and *templates* subfolders inside the *flask_app* subfolder:
    > books
        > flask_app
            > config
            > controllers
            > models
            > static
            > templates
            > __init__.py
        > schema
            > books_schema.mwb
            > books_schema.sql
        > Pipfile
        > Pipfile.lock

8. Inside the *config* subfolder, create a *mysqlconnection.py* file, type the following Python code, and save (you may remove the comment lines in the actual project, they were just placed here as a guide to help you understand the code):

```python (mysqlconnection.py)
# a cursor is the object we use to interact with the database
import pymysql.cursors

# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(
            host = 'localhost', 
            user = 'root', 
            password = 'root', 
            db = db, 
            charset = 'utf8mb4', 
            cursorclass = pymysql.cursors.DictCursor, 
            autocommit = True
        )
        # establish the connection to the database
        self.connection = connection

    # the method to query the database
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f'Running Query: {query}')
                cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid

                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    return cursor.fetchall()

                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()

            except Exception as e:
                # if the query fails the method will return FALSE
                print(f'Something went wrong, {e}')
                return False
            
            finally:
                # close the connection
                self.connection.close()

# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
```

    > books
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
            > models
            > static
            > templates
            > __init__.py
        > schema
            > books_schema.mwb
            > books_schema.sql
        > Pipfile
        > Pipfile.lock

9. Inside the *models* subfolder, create .py files that are modeled after your SQL tables. This is where the CRUD (Create, Read, Update, Destroy) functions for the project will be set up:

```python (user.py)
from flask import flash
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from MySQL database
class User:
    db = "users_schema"
    def __init__(self , data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.confirm_password = data["confirm_password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # class method to retrieve all users from the database (READ)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.db).query_db(query)

        # Create an empty list to append our instances of users, and iterate over the db results and create instances of users with cls.
        return [cls(user) for user in results]

    # class method to retrieve one user from the database (READ)
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    # class method to add a user to the database (CREATE)
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db(query, data)
    
    # class method to update a user in the database (UPDATE)
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
    
    # class method to delete a user from the database (DESTROY)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)
```

    > project_name
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
            > models
                > user.py
            > static
            > templates
            > __init__.py
        > Pipfile
        > Pipfile.lock

10. Inside the *controllers* subfolder, create a .py file named after the object that needs to be controlled in a plural form. As an example, *users.py*. Type the following Python code, and save:

```python (users.py)
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User

# The following sample code blocks need to be created for every route. You may include optional parameters and arguments into the functions as necessary:
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

```

    > project_name
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
                > users.py
            > models
                > user.py
            > static
            > templates
            > __init__.py
        > Pipfile
        > Pipfile.lock

11. Inside your project folder, create a *server.py* file, and type the following Python code and save:

```python (server.py)
from flask_app import app
from flask_app.controllers import users

# This code block enables automatic reloading of the server whenever you make changes to your code while the server is running:
if __name__ == "__main__":      
    app.run(debug=True)
```

    > project_name
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
                > users.py
            > models
                > user.py
            > static
            > templates
            > __init__.py
        > Pipfile
        > Pipfile.lock
        > server.py

**Part II: Frontend**
12. Inside the *static* subfolder, create the *css*, *img*, and *js* subfolders. These are where you will place any additional assets (CSS settings, JS scripts, images, etc.) that you will be using in your project.
    > project_name
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
                > users.py
            > models
                > user.py
            > static
                > css
                > img
                > js
            > templates
            > __init__.py
        > Pipfile
        > Pipfile.lock
        > server.py

13. Go to the [Bootstrap website](https://getbootstrap.com/docs/5.3/getting-started/download/), download and unzip the Compiled CSS and JS package, and copy the *bootstrap.js* file into the *static/js* subfolder. (Optional: You may also create your own *style.css* and *script.js* files if you need to add additional CSS settings and JS scripts for your project. Put the respective files in their allocated folders). 
    > project_name
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
                > users.py
            > models
                > user.py
            > static
                > css
                    > style.css
                > img
                > js
                    > bootstrap.js
                    > script.js
            > templates
            > __init__.py
        > Pipfile
        > Pipfile.lock
        > server.py

14. Inside the *templates* subfolder, create a starting page *index.html* file with the following code, which you can later modify with the rest of your HTML and Jinja code. During the rest of your project development, you may create additional HTML files as necessary, and also put them in the *templates* subfolder.

```html (index.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <p class="mb-4 fs-1 fw-bold">All Users</p>
        <table class="table table-bordered table-striped shadow">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Created At</th>
                    <th class="text-center">Actions</th>
                </tr>
            </thead>
            <tbody class="table-group-divider">
                {% for one_user in all_users %}
                <tr>
                    <td>{{ one_user.id }}</td>
                    <td>{{ one_user.first_name }}</td>
                    <td>{{ one_user.last_name }}</td>
                    <td>{{ one_user.email }}</td>
                    <td>{{ one_user.created_at.strftime("%B %d, %Y") }}</td>
                    <td class="d-flex align-items-center justify-content-evenly">
                        <a href="/users/{{ one_user.id }}">Show</a>
                        <a href="/users/edit/{{ one_user.id }}">Edit</a>
                        <a href="/users/destroy/{{ one_user.id }}">Delete</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        <br>
        <a class="fs-4" href="/users/new">Add a New User</a>
    </div>
    <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

```html (newuser.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <div class="d-flex align-items-center justify-content-between">
            <p class="fs-1 fw-bold">Add a New User</p>
            <a class="fs-3" href="/users">Home</a>
        </div>
        <form action="/users/new" method="POST">
            <label for="first_name" class="form-label">First Name:</label>
            <input type="text" class="mb-3 form-control" name="fname" placeholder="First name here">
            <label for="last_name" class="form-label">Last Name:</label>
            <input type="text" class="mb-3 form-control" name="lname" placeholder="Last name here">
            <label for="email" class="form-label">Email:</label>
            <input type="text" class="mb-3 form-control" name="email" placeholder="Email address here">
            <input type="submit" class="btn btn-primary shadow" value="Create">
        </form>
    </div>
    <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

```html (oneuser.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Read (One)</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <div class="d-flex align-items-center justify-content-between">
            <p class="fs-1 fw-bold">User {{ user.id }}</p>
            <a class="fs-3" href="/users">Home</a>
        </div>
        <table class="table shadow">
            <tbody>
                <tr>
                    <th scope="row">Full Name:</th>
                    <td><span class="me-1">{{ user.first_name }}</span>{{ user.last_name }}</td>
                </tr>
                <tr>
                    <th scope="row">Email:</th>
                    <td>{{ user.email }}</td>
                </tr>
                <tr>
                    <th scope="row">Created On:</th>
                    <td>{{ user.created_at.strftime("%B %d, %Y") }}</td>
                </tr>
                <tr>
                    <th scope="row">Last Updated On:</th>
                    <td>{{ user.updated_at.strftime("%B %d, %Y at %I:%M %p") }}</td>
                </tr>
            </tbody>
        </table>
        <span class="fs-4"><a class="me-3" href="/users/edit/{{ user.id }}">Edit</a> | <a class="ms-3" href="/users/destroy/{{ user.id }}">Delete</a></span>
    </div>
    <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

```html (edituser.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <div class="d-flex align-items-center justify-content-between">
            <p class="fs-1 fw-bold">Edit User {{ user.id }}</p>
            <a class="fs-3" href="/users">Home</a>
        </div>
        <form action="/users/edit/{{ user.id }}" method="POST">
            <label for="first_name" class="form-label">First Name:</label>
            <input type="text" class="mb-3 form-control" name="fname" placeholder="First name here" value="{{ user.first_name }}">
            <label for="last_name" class="form-label">Last Name:</label>
            <input type="text" class="mb-3 form-control" name="lname" placeholder="Last name here" value="{{ user.last_name }}">
            <label for="email" class="form-label">Email:</label>
            <input type="text" class="mb-3 form-control" name="email" placeholder="Email address here" value="{{ user.email }}">
            <div class="d-flex align-items-center">
                <input type="submit" class="me-5 btn btn-primary shadow" value="Update">
                <a class="fs-4" href="/users/{{ user.id }}">Show User</a>
            </div>
        </form>
    </div>
    <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

    > project_name
        > flask_app
            > config
                > mysqlconnection.py
            > controllers
                > users.py
            > models
                > user.py
            > static
                > css
                    > bootstrap.css
                    > style.css
                > img
                > js
                    > bootstrap.js
                    > script.js
            > templates
                > edituser.html
                > index.html
                > newuser.html
                > oneuser.html
            > __init__.py
        > Pipfile
        > Pipfile.lock
        > server.py

**Part III: Running the Project**
15. To run the Flask project, navigate to the Flask project folder in the terminal and type the following commands:

    pipenv shell
    python server.py

16. To test that your project is working, open the web browser and go to *localhost:5000*, and type in and test any specific routes you made in your code.

17. To stop the server / virtual environment from running, press *Ctrl-C*, then type *exit* in the terminal.