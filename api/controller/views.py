try:
    from api.resources.shortner import Redirector
    from flask_restful import Api
    from flask import Blueprint, current_app, jsonify
    from marshmallow import ValidationError
    from api.resources.shortner import LinkShortner, LinkShortnerResponseSchema, LinkShortnerRequestSchema
    from api.extensions import apispec
except Exception as e:
    print("Error: {} ".format(e))


blueprint = Blueprint("api",__name__)
api = Api(blueprint)

api.add_resource(LinkShortner, '/linkshortner')
api.add_resource(Redirector, '/s/<string:shortenedId>')

@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("LinkShortnerResponseSchema", schema=LinkShortnerResponseSchema)
    apispec.spec.components.schema("LinkShortnerRequestSchema", schema=LinkShortnerRequestSchema)
    apispec.spec.path(view=LinkShortner, app=current_app)
    apispec.spec.path(view=Redirector, app=current_app)

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(e):
    """Return json error for marshmallow validation errors.
    This will avoid having to try/catch ValidationErrors in all endpoints, returning
    correct JSON response with associated HTTP 400 Status (https://tools.ietf.org/html/rfc7231#section-6.5.1)
    """
    return jsonify(e.messages), 400