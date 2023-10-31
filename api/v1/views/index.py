#!/usr/bin/python3
"""This module defines API routes for status and statistics."""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """
    Status route that returns an 'OK' status message.

    Returns:
        JSON response with a 200 status code and a 'status' message.
    """
    data = {
        "status": "OK"
    }
    response = jsonify(data)
    response.status_code = 200
    return response

@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    Stats route that returns statistics about the data models.

    Returns:
        JSON response with a 200 status code and counts of various data models.
    """
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(data)
