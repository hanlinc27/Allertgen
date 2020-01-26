

"""
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceToken.json"
#FOLDER_PATH = r'C:\Macintosh HD\Users\wenlang\GitHub\AllertGen\VisionAPI'
def detect_labels(gs://cloud-samples-data/vision/label/setagaya.jpeg):
    
	from google.cloud.vision import vision
	import os, io
	import pandas as pd
	client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message)) 


"""
import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceToken.json"

client = vision.ImageAnnotatorClient()

FILE_NAME = 'menu5.jpg'
#menu photos needs to be accessible with the .py file
FOLDER_PATH = r'/Users/wenlang/GitHub/AllertGen/VisionAPI/Menu Photos'

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
	content = image_file.read()


image = vision.types.Image(content=content)
response = client.text_detection(image=image)

df = pd.DataFrame(columns=['locale', 'description'])
texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])