#!/usr/bin/python3
"""Script that starts a flask web application."""

from flask import Flask
from markupsafe import escape
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


@app.route("/c/<name>")
def c_concatenate(name):
    """
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    string = name.replace('_', ' ')
    return f"C {escape(string)}"


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>")
def python_text(text = "is cool"):
     """
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        - /python/<text>: display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    """
    string = text.replace('_', ' ')
    return f"Python {string}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
