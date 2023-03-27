#!/usr/bin/python3
"""
Starts a web application
- listening on 0.0.0.0 port 5000
- '/' display: 'Hello HBNB!'
- '/hbnb' display: 'HBNB'
- '/C/<text>'display: C <text_variable>
- '/python/<text>' display: python <text_variable>
- '/number/<int:n>' if n == int display '<n> is a number'
- '/number_template/<int:n>' if n == int => template with <n> in <BODY>
"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Template if is a number"""
    return render_template('5-number.html', n=n)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
