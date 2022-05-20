from flask_restful import Api
from flask import Blueprint
from api.resources.shortner import Links

api_bp = Blueprint('api',__name__)
api = Api(api_bp)

api.add_resource(Links, '/link')