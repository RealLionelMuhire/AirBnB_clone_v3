#!/usr/bin/python3
from flask import Flask, jsonify
from api.v1.views import app_views
import os
from models import storage


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.errorhandler(404)
def errorhandler404(exception):
    """handling 404 error"""
    data = {
        "error": "Not found"
    }
    response = jsonify(data)
    response.status_code = 404

    return response


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
