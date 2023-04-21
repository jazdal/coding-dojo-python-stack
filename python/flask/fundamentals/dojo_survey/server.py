from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dojo_survey'

@app.route('/')                 
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_info():
    session['username'] = request.form['username']
    print(session['username'])

    session['location'] = request.form['location']
    print(session['location'])

    session['language'] = request.form['language']
    print(session['language'])

    session['snack'] = request.form.getlist('snack')
    print(*session['snack'])

    session['comments'] = request.form['comments']
    print(session['comments'])

    return redirect('/result')

@app.route('/result')
def show_info():
    return render_template('result.html', username = session['username'], location = session['location'], language = session['language'], snacks = session['snack'], comments = session['comments'])

if __name__ == "__main__":      
    app.run(debug = True)