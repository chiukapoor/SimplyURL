from distutils.log import debug
from flask import Flask
from api.controller.views import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config')
    app.register_blueprint(api_bp)
    return app