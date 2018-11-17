import io
import os
import base64

# Import the flask server resources
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

credential_path='C:/Neutrinos/programs/food-server/food-server/creds.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Initialize server app and api
app = Flask(__name__)
api = Api(app)

# Instantiates a client for google's vision api
client = vision.ImageAnnotatorClient()

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

# class FoodInfo(Resource):
#     def post(self):
#         f = request.files['file']
#         #read image file string data
#         # filestr = request.files['file'].read()
#         # #convert string data to numpy array
#         # npimg = numpy.fromstring(filestr, numpy.uint8)
#         # # convert numpy array to image
#         # img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
#         filename = images.save(f)
#         self.image_filename = filename
#         self.image_url = images.url(filename)

#         content = f.read()
#         # print(content)
#         # image = types.Image(content=content)
#         # # Performs label detection on the image file
#         # response = client.label_detection(image=image)
#         # labels = response.label_annotations
#         # return {"data": labels}
#         return 200


api.add_resource(Recommend, '/recommend/<string:emotion>')
api.add_resource(GetRestaurant, '/getRestaurant')
api.add_resource(GetMenu, '/getMenu')
#api.add_resource(FoodInfo, '/foodInfo')

if __name__ == '__main__':
    app.run(debug = True)