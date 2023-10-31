#!/usr/bin/python3
""" handling routes for state"""

from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def getState():
    """retrieving all states"""
    state_list = []
    state = storage.all("State")
    for data in state.values():
        state_list.append(data.to_dict())


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def createState():
    """creating state"""
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, 'Not a JSON')
    if "name" not in state_json:
        abort(400, 'Missing name')
    state = State(**state_json)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def getStateById(state_id):
    """retrieving state by id"""
    obj = storage.get("State", str(state_id))

    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def updateState(state_id):
    """updating state by id"""
    state_json = request.get_json(silent=True)
    if state_json is None:
        abort(400, 'Not a JSON')
    obj = storage.get("State", str(state_id))
    if obj is None:
        abort(404)
    for key, val in state_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(obj, key, val)
    obj.save()
    return jsonify(obj.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def deleteState(state_id):
    """deleting state by Id"""
    obj = storage.get("State", str(state_id))

    if obj is None:
        abort(404)

    storage.delete(obj)
    storage.save()

    return jsonify({})
