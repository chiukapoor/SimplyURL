try:
    from flask import Flask
    from api.extensions import apispec
    from api.controller.views import blueprint
except Exception as e:
    print("Error: {} ".format(e))

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config')
    apispec.init_app(app)
    app.register_blueprint(blueprint)
    return app