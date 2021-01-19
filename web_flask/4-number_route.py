#!/usr/bin/python3
"""This script starts a flask web application
"""
from flask import Flask
from flask.helpers import stream_with_context
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHbtn():
    """This function return a content for the specified route

    Returns:
        string: content to return
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbtn():
    """This function return a content for the specified route

    Returns:
        string: content to return
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variableText(text=''):
    """This function return a content for the specified route

    Args:
        text (str, optional): Input text. Defaults to ''.

    Returns:
        string: content to return
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonIs(text=''):
    """This function return a content for the specified route

    Args:
        text (str, optional): Input text. Defaults to 'is cool'.

    Returns:
        string: content to return
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def displayInt(n):
    """This function return a content for the specified route only if n is
    int

    Args:
        n (int): Input integer

    Returns:
        string: content to return
    """
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
