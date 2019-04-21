
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types



os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --save /home/pi/Desktop/image.jpg')

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    '/home/pi/Desktop/image.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
prediction = ""
for label in labels:
	prediction = label.description.split("\n")[0]
	break 
print(prediction)
prediction_var = 0 

if prediction == "water": 
	prediction_var = 0
elif  prediction == "metal": 
	prediction_var = 0
elif prediction == "water bottle": 
	prediction_var = 0
elif prediction == "newspaper":
	prediction_var = 0
elif prediction == "plastic": 
	prediction_var = 0 
elif prediction == "cup": 
	prediction_var = 0 
elif prediction ==  "bagel": 
	predicition_var = 1
elif prediction == "brown": 
	prediction_var = 1 
elif prediction == "chicken": 
	prediction_var = 1 
elif prediction == "pen": 
	prediction_var = 1 
elif prediction == "pencil": 
	prediction_Var = 1
print(prediction_var) 


	

 

