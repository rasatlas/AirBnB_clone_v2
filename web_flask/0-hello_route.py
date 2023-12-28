#!/usr/bin/python3
"""Script that starts a Flask web application"""

def hello():
    """
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    """
    return "Hello HBNB!"
