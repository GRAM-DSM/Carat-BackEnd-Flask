from flask import Flask
from flask_restful import Api

def create_app():

    _app = Flask(__name__)

    api = Api(_app)

    from Server.view.auth import Auth
    api.add_resource(Auth, '/user')

    return _app
