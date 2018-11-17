import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# from google.cloud import language
# from google.oath2 import service_account
credential_path='C:/Neutrinos/programs/food-server/food-server/creds.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# credentials = service_account.Credentials.from_service_account_file('C:/Neutrinos/programs/food-server/food-server')
# client = language.languageServiceClient(credentials=credentials)

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'sad/1.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)