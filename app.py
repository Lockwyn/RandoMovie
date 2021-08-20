from flask import Flask
from flask_restful import Resource, Api
import randomMovie as rm
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return rm.recommend()


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)