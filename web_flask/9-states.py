#!/usr/bin/python3
"""
Start a Flask web application
listening on 0.0.0.0 port: 5000
- route:'/cities_by_states' display a html page
with the state and cities relanted
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/')
@app.route('/states', strict_slashes=False)
def states_list_route():
    """All states template"""
    return render_template(
            '9-states.html', all_states=storage.all(State), states=None)


@app.route('/states/<a_id>', strict_slashes=False)
def citites_by_state_list_route(a_id):
    """States + id template"""
    states = storage.all(State).get(f"State.{a_id}")
    return render_template(
            '9-states.html', states=states, all_states=None)


@app.teardown_appcontext
def close_session(exception):
    """Close current SQLalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
