from SimplyURL.api.resources.shortner import Redirector
from flask_restful import Api
from flask import Blueprint
from api.resources.shortner import LinkShortner

api_bp = Blueprint('api',__name__)
api = Api(api_bp)

api.add_resource(LinkShortner, '/linkshortner')
api.add_resource(Redirector, '/')