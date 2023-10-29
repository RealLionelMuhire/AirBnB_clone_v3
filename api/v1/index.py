#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonfy

@app_views.route('status', methods=['GET'], strict_slashes=False)
def get_status():
    return jsonfy({"status"}: {"OK"})
