from flask import Flask, request, jsonify
from flask_restful import Resource, Api

# initialize server app and api
app = Flask(__name__)
api = Api(app)

class FoodList(Resource):
    def get(self, emotion):
        return {"data": emotion}, 200


api.add_resource(FoodList, '/getFood/<string:emotion>')

if __name__ == '__main__':
    app.run(debug = True)