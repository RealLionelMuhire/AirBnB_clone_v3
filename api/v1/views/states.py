#!/usr/bin/python3
""" handling routes for state"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route("/states", methods=["GET"], strict_slashes=False)
def getState():
    """retrieving all states"""
    if state_id is None:

        states = storage.all(State)
        state_list = [state.to_dict() for state in states.values()]
        return jsonify(state_list)
    else:
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        return jsonify(state.to_dict())

@app_views.route("/states", methods=["POST"], strict_slashes=False)
def createState():
    """creating state"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def updateState(state_id):
    """updating state by id"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    state = storage.get(State, state_id)
    if state is None:
        abort(404)

    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())

@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def deleteState(state_id):
    """deleting state by Id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200
