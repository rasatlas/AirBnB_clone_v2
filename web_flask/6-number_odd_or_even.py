#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from flask import render_template
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
def python_text(text="is cool"):
    """
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        - /python/<text>: display “Python ”, followed by the value of the
        text variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    """
    string = text.replace('_', ' ')
    return f"Python {string}"


@app.route("/number/<int:n>")
def is_a_number(n):
    """
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        - /number/<n>: display “n is a number”, only if n is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def n_is_a_number(n):
    """
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        - /number_template/<n>: display a HTML page only if n is an integer:
        - H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        - /number_odd_or_even/<n>: display a HTML page only if n is an integer
        - H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
