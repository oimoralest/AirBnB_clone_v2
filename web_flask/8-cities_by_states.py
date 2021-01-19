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


@app.route('/cities_by_states', strict_slashes=False)
def renderStateCities():
    """Renders an HTML template with all the states and cities

    Args:
        states (dict): dictionary with states information

    Returns:
        string: HTML template
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')