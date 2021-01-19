#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def closeStorage(exception):
    """Closes a database/file connection"""
    storage.close()


@app.route('/states/', defaults={'id': ''}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def displayStates(id=''):
    """Display an HTML template

    Args:
        id (str, optional): Input id. Defaults to ''.

    Returns:
        string: HTML template
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
