from random import randint, choice
from datetime import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'one_piece'

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    
    if 'messages' not in session:
        session['messages'] = []
    
    if 'moves' not in session:
        session['moves'] = 0
    
    print("Number of moves:", session['moves'])
    print("Total gold:", session['total_gold'])

    return render_template('index.html', total_gold = session['total_gold'], messages = session['messages'], moves = session['moves'])

@app.route('/process_money', methods=['POST'])
def compute_golds():
    building_value = {
        'farm': (10, 20), 
        'cave': (5, 10), 
        'house': (2, 5), 
        'casino': (0, 50)}
    
    if request.form['building'] == 'casino':
        session['moves'] += 1
        gold = randint(building_value['casino'][0], building_value['casino'][1])
        operator = choice(('addition', 'subtraction'))

        if operator == 'addition':
            session['total_gold'] += gold
            session['messages'].append(f'Earned {gold} golds from the casino! ({datetime.now().strftime("%Y/%m/%d %I:%M %p").lower()})')
        else:
            session['total_gold'] -= gold
            session['messages'].append(f'Entered a casino and lost {gold} golds... Ouch. ({datetime.now().strftime("%Y/%m/%d %I:%M %p").lower()})')
        
    else:
        place = request.form['building']
        session['moves'] += 1
        gold = randint(building_value[request.form['building']][0], building_value[request.form['building']][1])
        session['total_gold'] += gold
        session['messages'].append(f'Earned {gold} golds from the {place}! ({datetime.now().strftime("%Y/%m/%d %I:%M %p").lower()})')

    return redirect('/')

@app.route('/reset')
def delete_cookies():
    session.clear()
    return redirect('/')

if __name__ == "__main__":      
    app.run(debug = True)