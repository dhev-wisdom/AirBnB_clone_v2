#!/usr/bin/python3
"""Flask web application"""

from flask import Flask


app = Flask(__name__)


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
def python_is_what(text='is_cool'):
    """Python is what again..."""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
