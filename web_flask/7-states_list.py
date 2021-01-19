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


@app.route('/states_list', strict_slashes=False)
def renderStates():
    """Renders an HTML template with all the states

    Args:
        states (dict): dictionary with states information

    Returns:
        string: HTML template
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run('0.0.0.0', port='5000')
