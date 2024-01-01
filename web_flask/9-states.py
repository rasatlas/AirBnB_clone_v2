#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from models import storage, state
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def list_states(state_id=''):
    """
    Display HTML page with the states sorted alphabetically
    If state with a matching id as the passed id is found, list
    all cities linked to the state with same id.
    If no matching id is found display: Not found!
    """
    states = storage.all(state.State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
