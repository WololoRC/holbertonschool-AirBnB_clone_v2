#!/usr/bin/python3
"""my first flask application"""
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    strict_slashes=False
    return "Hello HBNB!"

app.run(host='0.0.0.0', port=5000)