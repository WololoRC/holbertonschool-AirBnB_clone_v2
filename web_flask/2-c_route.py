#!/usr/bin/python3
"""
Starts a web application
- listening on 0.0.0.0 port 5000
- '/' display: 'Hello HBNB!'
- '/hbnb' display: 'HBNB'
- 'C/<text>'display: C followed by the value of the text variable'
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
    return f"C {escape(text).replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
