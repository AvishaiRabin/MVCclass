#!/usr/bin/env python

import flask
from flask import Response
import json
import sqlite


# Create the application.
app = flask.Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()
