import requests
import io
import os
import json

title = 'burger'

response = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/guessNutrition/?title='+title,
                    headers={'X-Mashape-Key':'dyrT5by5J8mshgJDLgP35NrsrGctp19bsgKjsnFU5ehTZ6C0MI',
                             'Accept':'application/json'},)


print(response.content)
