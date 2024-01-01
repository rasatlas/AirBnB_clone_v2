#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from models import storage, state, amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def display_index_page():
    """
    Display HTML page
    """
    states = storage.all(state.State).values()
    amenities = storage.all(amenity.Amenity).value()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
