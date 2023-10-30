#!/usr/bin/python3
""" handling routes for state"""

from flask import jsonify, request, abort
from ap1.v1.views import app_views
from models import storage
from models.state import State
