#!/usr/bin/python3
"""Script that starts a Flask web application"""

from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def list_states():
    """
    - Script that lists states
    - You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage)
    => from models import storage and storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call in this method storage.close()
    - Routes:
        - /states_list: display a HTML page: (inside the tag BODY)
        - H1 tag: “States”
        - UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
        - LI tag: description of one State: <state.id>: <B><state.name></B>
    """
    states = sorted(list(storage.all("State").values()), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
