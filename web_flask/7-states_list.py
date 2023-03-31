#!/usr/bin/python3
"""
Start a Flask web application
listening on 0.0.0.0 port: 5000
- route:'/states_list' display a html page
with the states inside DB listed
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/')
@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """Put his template on rout"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def close_session(exception):
    """Close current SQLalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
