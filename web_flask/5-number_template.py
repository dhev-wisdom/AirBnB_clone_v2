#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/', strict_slashes=False)
def hello():
    """Home route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_what(text):
    """C is what again..."""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_is_what(text='is cool'):
    """Python is what again..."""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:num>', strict_slashes=False)
def show_number(num):
    """n is a Number"""
    if isinstance(num, int):
        return f"{num} is a number"


@app.route('/number_template/<int:num>', strict_slashes=False)
def show_template(num):
    """n is a Number"""
    return render_template('5-number.html', number=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
