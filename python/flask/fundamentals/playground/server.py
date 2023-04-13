from flask import Flask, render_template
app = Flask(__name__)           

@app.route('/play')                 
def draw_square():
    return render_template('index.html', times = 3, color = "lightskyblue")

@app.route('/play/<int:x>')
def draw_more_squares(x):
    return render_template('index.html', times = x, color = "lightskyblue")

@app.route('/play/<int:x>/<y>')
def draw_more_squares_with_colors(x, y):
    return render_template('index.html', times = x, color = str(y))

if __name__ == "__main__":      
    app.run(debug = True)