from flask import Flask, render_template
app = Flask(__name__)           

@app.route('/')                 
def index():
    return render_template('index.html', phrase = 'hello', times = 5)

@app.route('/success')
def success():
    return "success"

@app.route('/dojo')
def dojo():
    return f'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi, ' + str(name.title()) + '!'

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return f'username: {username}, id: {id}'

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return (str(word) + ' ') * int(num)

@app.route('/lists')
def render_lists():
    student_info = [
        {'name': 'Michael', 'age': 35}, 
        {'name': 'John', 'age': 30}, 
        {'name': 'Mark', 'age': 25}, 
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers = [3, 1, 5], students = student_info)

@app.route('/<path:invalid_route>')
def invalid_route(invalid_route):
    return f'Sorry! No response. Try again.'

if __name__ == "__main__":      
    app.run(debug = True)