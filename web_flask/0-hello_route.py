#!/usr/bin/python3
"""My first flask module"""
rom flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Say hello"""
    strict_slashes = False
    return "Hello HBNB!"


app.run(host='0.0.0.0', port=5000)
