import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'great_number_game' 

@app.route('/')                 
def index():
    if 'secret_num' not in session:
        session['secret_num'] = random.randint(1, 100)
    return render_template('index.html', secret_num = int(session['secret_num']))

@app.route('/guess', methods=['POST'])
def pick_number():
    session['guessed_num'] = request.form['guessed_num']
    if 'attempts' not in session:
        session['attempts'] = 1
    else:
        session['attempts'] += 1
    print("The secret number is:", session['secret_num'])
    print("The guessed number is:", session['guessed_num'])
    print("The number of attempts is:", session['attempts'])
    if session['attempts'] > 5:
        return redirect('/you_lose')
    return render_template('guess.html', guessed_num = int(session['guessed_num']), secret_num = int(session['secret_num']), attempts = int(session['attempts']))

@app.route('/you_lose')
def lose_the_game():
    return render_template('lose.html')

@app.route('/clear_session')
def clear_cookie():
    session.clear()
    return redirect('/')

if __name__ == "__main__":      
    app.run(debug = True)