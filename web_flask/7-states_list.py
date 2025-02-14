#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display HTML page with the states listed in alphabetical order
    """
    states = sorted(list(storage.all(state.State).values()),
                    key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
