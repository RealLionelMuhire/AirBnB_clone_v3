#!/usr/bin/python3
"""This module defines API routes for status and statistics."""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
    #response.status_code = 200
    return response


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """
    Stats route that returns statistics about the data models.

    Returns:
        JSON response with a 200 status code and counts of various data models.
    """
    data = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User
    }
    for key, value in data.items():
        data[key] = storage.count(value)
    return jsonify(data)
