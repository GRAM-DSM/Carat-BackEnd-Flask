from flask import request
from flask_restful import Resource

from Server.view import check_json
from Server.controller.auth import sign_up


class Auth(Resource):

    @check_json({
        "name": str,
        "email": str,
        "password": str
    })
    def post(self):
        name = request.json['name']
        email = request.json["email"]
        password = request.json["password"]

        return sign_up(name, email, password)


class Login(Resource):

    @check_json({
        "email": str,
        "password": str
    })
    def post(self):

        email = request.json['email']
        password = request.json['password']

        return
