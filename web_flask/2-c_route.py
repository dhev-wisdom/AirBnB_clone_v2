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
    """C is what igain..."""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
