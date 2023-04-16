# FLASK AND BOOTSTRAP PROJECT SETUP GUIDE
### Personal Notes by: Jasper Dalawangbayan

This is a simple guide I made for creating a Flask project template with the Bootstrap library for web development, based on my learnings in the *Coding Dojo Python Web Development* Bootcamp.

### Recommended Tools:
- Visual Studio Code (VS Code)
- The latest version of Python

1. *If you haven't done so yet:* Install the virtual environment tool (pipenv) using pip. Typing the following command in the terminal will globally install the virtual environment tool *pipenv*, so you only need to do this ONCE for all your Flask projects, and never again:

    pip install pipenv

2. Create a folder for your Flask project.

3. Inside your Flask project folder, create the following subfolders:
    - templates
    - static

4. Inside the static subfolder, create the following subfolders. This is where you will place any additional assets (CSS settings, JS scripts, images, etc.) that you will use in your project accordingly:
    - css
    - img
    - js

5. Navigate into your Flask project folder in the terminal. Then type the following command in the terminal to install Flask (you need to do this for every Flask project you create):

    pipenv install flask

You can confirm that Flask is installed after you see two files created in your Flask project folder: *Pipfile* and *Pipfile.lock*. Pipfile contains the packages installed, whereas Pipfile.lock contains the specific details on what version is being used.

6. Inside the *templates* subfolder, create an *index.html* file with the following boilerplate code, which you can later modify. This already includes the CDN (Content Delivery Network) links to the Bootstrap CSS and JS settings that will allow the use of Bootstrap features in the project:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
        <title>Document Title</title>
    </head>
    <body>
        <!--Your HTML code goes here-->
            <!--For using images in your HTML, follow the format below-->
            <img src="{{ url_for('static', filename='img/my_img.png') }}" alt="my_img">

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
        <script type="text/javascript" src="{{ url_for('static', filename='js/script.js') }}"></script>
    </body>
</html>
```

7. Inside your Flask project folder, create a *server.py* file, and include the following code:

```python
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # modify your secret key accordingly         

# The following sample code blocks need to be created for every route. You may include optional parameters and arguments into the functions as necessary:
@app.route('/')                 
def index():
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

8. To run the Flask project, navigate to the Flask project folder in the terminal and type the following commands:

    pipenv shell
    python server.py

9. To test that your project is working, open the web browser and go to *localhost:5000*, and type in any specific routes you made in your code.

10. To stop the server / virtual environment from running, press *Ctrl-C*, then type *exit* in the terminal.