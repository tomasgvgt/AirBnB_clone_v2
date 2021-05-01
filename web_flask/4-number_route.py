#!/usr/bin/python3
"""
* script that starts a Flask web application
* Your web application must be listening on 0.0.0.0, port 5000
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ” followed by the value of the text variable
  (replace underscore _ symbols with a space )
* /python/(<text>): display “Python ”, followed by the value of the variable
  (replace underscore _ symbols with a space )
* You must use the option strict_slashes=False in your route definition
* /number/<n>: display “n is a number” only if n is an integer
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """display “Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """display HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_message(text):
    """display C + text"""
    text = text.replace("_", " ")
    return ("C " + text)


@app.route('/python/', strict_slashes=False, defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_message(text):
    text = text.replace("_", " ")
    return ("Python " + text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_message(n):
    return ("%d is a number" % n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
