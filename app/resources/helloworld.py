from flask import request
from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hello World!'}

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}, 201