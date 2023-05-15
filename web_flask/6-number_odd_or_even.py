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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/')
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


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def show_template_if(num):
    """n is a Number"""
    status_ = ''
    if num % 2 == 0:
        status_ = 'even'
    else:
        status_ = 'odd'

    return render_template('6-number_odd_or_even.html', number=num, status=status_)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
