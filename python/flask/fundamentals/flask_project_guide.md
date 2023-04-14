# FLASK PROJECT GUIDE
### Personal Notes by: Jasper Dalawangbayan

This is a small guide I created for creating a Flask project template for web development, based on my learnings in the *Coding Dojo Python Web Development* Bootcamp.

1. *If you haven't done so yet:* install the virtual environment tool using pip. Typing the following command in the terminal will globally install the virtual environment tool *pipenv*, so you only need to do this ONCE for all your Flask projects, and never again:

    pip install pipenv

2. Create a folder for your Flask project.

3. Inside your Flask project folder, create the following subfolders:
    - templates
    - static

4. Navigate into your Flask project folder in the terminal. Then type the following command in the terminal to install Flask (you need to do this for every Flask project you create):

    pipenv install flask

You can confirm that Flask is installed after you see two files created in your Flask project folder: *Pipfile* and *Pipfile.lock*. Pipfile contains the packages installed, whereas Pipfile.lock contains the specific details on what version is being used.

5. Inside the *templates* subfolder, create an *index.html* file with the following boilerplate code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
    <title>Document Title</title>
</head>
<body>
    <!-- The rest of your HTML code goes here -->
</body>
</html>
```

6. Inside the *static* subfolder, create a *style.css* file with the following CSS reset code:

```css
* {
    padding: 0;
    margin: 0;
    vertical-align: top;
    box-sizing: border-box;
}

/* The rest of your CSS settings go here */
```

7. Inside your Flask project subfolder, create a *server.py* file:

```python
from flask import Flask, render_template
app = Flask(__name__)           

# the following sample code block needs to be created for every route:
@app.route('/')                 
def sample_function(optional_parameter):
    return render_template('index.html', argument = optional_parameter)

if __name__ == "__main__":      
    app.run(debug = True)
```

8. To run the Flask project, navigate to the Flask project folder in the terminal and type the following commands:

    pipenv shell
    python server.py

9. To test that your project is working, open the web browser and go to *localhost:5000*, and type in any specific routes you made in your code.

10. To stop the server / virtual environment from running, press *Ctrl-C*, then type *exit* in the terminal.