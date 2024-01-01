#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from models import storage, state, city
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """
    Display HTML page with the states and their corresponding cities
    listed in alphabetical order
    """
    states = storage.all(state.State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')