from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)        
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')                 
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print(f'Got post info')
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html', username = session['username'], useremail = session['useremail'])

if __name__ == "__main__":      
    app.run(debug = True)
