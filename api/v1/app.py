#!/usr/bin/python3
"""
app module
"""
from flask import Flask
from models import storage
from flask import jsonify
from os import getenv
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def resource_not_found(error):
    """ not found url"""
    return (jsonify(error="Not found"), 404)


@app.teardown_appcontext
def off_sesssion(_):
    """pending"""
    storage.close()

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host, port, threaded=True)
