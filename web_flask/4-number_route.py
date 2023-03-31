#!/usr/bin/python3
"""
Starts a web application
- listening on 0.0.0.0 port 5000
- '/' display: 'Hello HBNB!'
- '/hbnb' display: 'HBNB'
- '/C/<text>'display: C <text_variable>
- '/python/<text>' display: python <text_variable>
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Say hello"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return "HBNB"


@app.route('/C/<text>', strict_slashes=False)
def C_is_fun(text):
    """As hell!"""
    return "C {}".format(escape(text).replace('_', ' '))


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Is Awesome!"""
    return "Python {}".format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Is a number?"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
