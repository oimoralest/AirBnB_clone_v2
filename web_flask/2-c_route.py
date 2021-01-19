"""This script starts a flask web application
"""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
