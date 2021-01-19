#!/usr/bin/python3
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
