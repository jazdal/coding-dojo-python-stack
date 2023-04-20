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

    session['comments'] = request.form['comments']
    print(session['comments'])

    return redirect('/')

@app.route('/result')
def show_info():
    return render_template('show.html', username = session['username'], useremail = session['useremail'])

if __name__ == "__main__":      
    app.run(debug = True)