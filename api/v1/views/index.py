#!/usr/bin/python3
"""index in views """

from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """status route"""
    data = {
            "status": "OK"
            }
    response = jsonify(data)
    response.status_code = 200

    return response
