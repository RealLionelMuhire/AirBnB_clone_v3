#!/usr/bin/python3

from api.v1.views import app_views
from flask import Fask, jsonify
from models import storage

@app_views.route('status', methods=['GET'], strict_slashes=False)
def get_status():
    return jsonify({"status"}: {"OK"})
