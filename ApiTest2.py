import requests
import io
import os
import json
import re

def cleanhtml(raw_html):
    cleanr=re.compile('<.*?>')
    cleantext=re.sub(cleanr,'',raw_html)
    return cleantext


response = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/guessNutrition?title=Spaghetti+Aglio+et+Olio',
                    headers={'X-Mashape-Key':'ly4fmOXhOMmshQ6lS9Zw1IM6ksOAp1dHN0YjsnIfkxI0s7eY3F',
                             'Accept':'application/json'},)


nutrition=json.loads(response.content)

id= nutrition['recipesUsed']

response1 = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/'+str(id)+'/summary',
                    headers={'X-Mashape-Key':'ly4fmOXhOMmshQ6lS9Zw1IM6ksOAp1dHN0YjsnIfkxI0s7eY3F',
                             'Accept':'application/json'},)


recipe=json.loads(response1.content)
summary = recipe['summary']
summary=cleanhtml(summary)
print(summary)



