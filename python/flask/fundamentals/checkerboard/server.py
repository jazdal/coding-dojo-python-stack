from flask import Flask, render_template
app = Flask(__name__)           

@app.route('/')                 
def draw_checkerboard():
    return render_template('index.html', height = 8, width = 8, color1 = "black", color2 = "red")

@app.route('/<int:num1>')
def draw_checkerboard_one(num1):
    return render_template('index.html', height = num1, width = 8, color1 = "black", color2 = "red")

@app.route('/<int:num1>/<int:num2>')
def draw_checkerboard_two(num1, num2):
    return render_template('index.html', height = num1, width = num2, color1 = "black", color2 = "red")

@app.route('/<int:num1>/<int:num2>/<string:col1>/<string:col2>')
def draw_ninja_checkerboard(num1, num2, col1, col2):
    return render_template('index.html', height = num1, width = num2, color1 = col1, color2 = col2)

if __name__ == "__main__":      
    app.run(debug = True)
