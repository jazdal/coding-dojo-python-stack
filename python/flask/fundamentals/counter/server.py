from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    
    if 'add_one' not in session:
        session['add_one'] = 1
    
    if 'add_two' not in session:
        session['add_two'] = 0
    
    if 'add_any' not in session:
        session['add_any'] = 0
    
    count = session['add_one'] + session['add_two'] + session['add_any']
    return render_template('index.html', visits = session['visits'], counter = count)

@app.route('/destroy_session')
def reset_cookie():
    session.clear()
    return redirect('/')

@app.route('/add1')
def add_one():
    if 'add_one' in session:
        session['add_one'] += 1
    else:
        session['add_one'] = 1
    return redirect('/')

@app.route('/add')
def add_two():
    if 'add_two' in session:
        session['add_two'] += 2
    else:
        session['add_two'] = 2
    return redirect('/')

@app.route('/add_more', methods=['POST'])
def increment():
    if 'add_any' in session:
        session['add_any'] += int(request.form['add_any'])
    else:
        session['add_any'] = int(request.form['add_any'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)