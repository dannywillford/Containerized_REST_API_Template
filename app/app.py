from flask import Flask, request
from flask_restful import Api

from resources.helloworld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)