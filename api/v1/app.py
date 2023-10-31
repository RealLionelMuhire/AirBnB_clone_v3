#!/usr/bin/python3
"""
script to creates Flask web application and defines routes error

It registers API routes, handles teardown, includes 404 error handler.

Usage:
    Run this script to start the Flask web application.

Environment Variables:
    HBNB_API_HOST: Host IP address to listen on (default: 0.0.0.0)
    HBNB_API_PORT: Port to run the web application (default: 5000)
"""

from flask import Flask, jsonify
from api.v1.views import app_views
import os
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Close the storage session after each request.
    """
    storage.close()


@app.errorhandler(404)
def errorhandler404(exception):
    """
    Custom 404 error handler that returns a JSON response.

    Returns:
        JSON response with a 404 status code and an error message.
    """
    return jsonify(error='Not found'), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
