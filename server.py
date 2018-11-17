from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

# initialize server app and api
app = Flask(__name__)
api = Api(app)

class Recommend(Resource):
    def get(self, emotion):
        with open(emotion + '/' + emotion + '.json') as f:
            data = json.load(f)
            return data, 200
        return {"data": emotion, "error":"could not load data"}, 400

class GetMenu(Resource):
    def get(self):
        main_course = []
        dessert = []
        drinks = []
        with open('angry/angry.json') as f:
            data = json.load(f)
            for d in data['data']:
                if d['category'] == "main course":
                    main_course.append(d)
                if d['category'] == "dessert":
                    dessert.append(d)
                if d['category'] == "drinks":
                    drinks.append(d)
        with open('happy/happy.json') as f:
            data = json.load(f)
            for d in data['data']:
                if d['category'] == "main course":
                    main_course.append(d)
                if d['category'] == "dessert":
                    dessert.append(d)
                if d['category'] == "drinks":
                    drinks.append(d)
        with open('sad/sad.json') as f:
            data = json.load(f)
            for d in data['data']:
                if d['category'] == "main course":
                    main_course.append(d)
                if d['category'] == "dessert":
                    dessert.append(d)
                if d['category'] == "drinks":
                    drinks.append(d)
        with open('fear/fear.json') as f:
            data = json.load(f)
            for d in data['data']:
                if d['category'] == "main course":
                    main_course.append(d)
                if d['category'] == "dessert":
                    dessert.append(d)
                if d['category'] == "drinks":
                    drinks.append(d)
        with open('disgust/disgust.json') as f:
            data = json.load(f)
            for d in data['data']:
                if d['category'] == "main course":
                    main_course.append(d)
                if d['category'] == "dessert":
                    dessert.append(d)
                if d['category'] == "drinks":
                    drinks.append(d)
        with open('neutral/neutral.json') as f:
            data = json.load(f)
            for d in data['data']:
                if d['category'] == "main course":
                    main_course.append(d)
                if d['category'] == "dessert":
                    dessert.append(d)
                if d['category'] == "drinks":
                    drinks.append(d)

        return {"main course": main_course, "dessert": dessert, "drinks": drinks}, 200


class GetRestaurant(Resource):
    def get(self):
        with open('restaurant.json') as f:
            data = json.load(f)
            return data, 200


api.add_resource(Recommend, '/recommend/<string:emotion>')
api.add_resource(GetRestaurant, '/getRestaurant')
api.add_resource(GetMenu, '/getMenu')

if __name__ == '__main__':
    app.run(debug = True)