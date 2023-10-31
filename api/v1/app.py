#!/usr/bin/python3
"""
This script creates a Flask web application and defines routes and error handling.

It registers the app_views blueprint for API routes, handles teardown operations, and includes a custom 404 error handler.

Usage:
    Run this script to start the Flask web application.

Environment Variables:
    HBNB_API_HOST: Host IP address to listen on (default: 0.0.0.0)
    HBNB_API_PORT: Port to run the web application (default: 5000)
"""

from flask import Flask, jsonify
from api.v1.views import app_views
from os import getenv
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
    data = {
        "error": "Not found"
    }
    response = jsonify(data)
    response.status_code = 404
    return response

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"), threaded=True)
