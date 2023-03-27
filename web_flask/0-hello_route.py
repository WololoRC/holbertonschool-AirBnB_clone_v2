#!/usr/bin/python3
"""
Starts a web application
- listening on 0.0.0.0 port 5000
- '/' displays Hello HBN
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Say hello"""
    strict_slashes = False
    return "Hello HBNB!"


app.run(host='0.0.0.0', port=5000)
