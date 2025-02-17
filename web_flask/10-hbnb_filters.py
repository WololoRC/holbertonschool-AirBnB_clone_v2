#!/usr/bin/python3
"""
Start a Flask web application
listening on 0.0.0.0 port: 5000
- route:'/hbnb_filters' display index html
of our late clone.'
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/')
@app.route('/hbnb_filters', strict_slashes=False)
def filters_route():
    """Render template on our filters rout"""
    return render_template(
            '10-hbnb_filters.html',
            states=storage.all(State), amenities=storage.all(Amenity))


@app.teardown_appcontext
def close_session(exception):
    """Close current SQLalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
