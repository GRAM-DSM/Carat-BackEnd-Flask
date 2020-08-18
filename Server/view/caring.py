from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from Server.model import caring

class Caring(Resource):

    @jwt_required
    def post(self):
        pass




