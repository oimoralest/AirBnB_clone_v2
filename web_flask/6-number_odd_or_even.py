#!/usr/bin/python3
"""This script starts a flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHbtn():
    """This function returns a content for the specified route

    Returns:
        string: content to return
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbtn():
    """This function returns a content for the specified route

    Returns:
        string: content to return
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variableText(text=''):
    """This function returns a content for the specified route

    Args:
        text (str, optional): Input text. Defaults to ''.

    Returns:
        string: content to return
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonIs(text=''):
    """This function returns a content for the specified route

    Args:
        text (str, optional): Input text. Defaults to 'is cool'.

    Returns:
        string: content to return
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def displayInt(n):
    """This function returns a content for the specified route only if n is an
    integer

    Args:
        n (int): Input integer

    Returns:
        string: content to return
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def displayTemplate(n):
    """This function returns an HTML template only if n is an integer

    Args:
        n (int): Input integer

    Returns:
        string: HTML template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def displayEvenOrOdd(n):
    """This function returns an HTML template only if n is an integer

    Args:
        n (int): Input integer

    Returns:
        string: HTML template
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
