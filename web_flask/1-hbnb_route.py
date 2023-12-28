#!/usr/bin/python3
"""Script that starts Flask web application"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def root_hello():
    """
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_hello():
    """
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /hbnb: display “HBNB”
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
