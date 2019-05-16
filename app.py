from flask import Flask, render_template, request

import numpy as np
from keras.preprocessing import image
import sys
import os
import random
import json
sys.path.append(os.path.abspath('./models'))

from models.load import *

# Init flask app
app = Flask(__name__)

global model, graph
model, graph = init()

global img_path, img_src_template
img_path, img_src_template = './static/img/cells', '%s/%s'

global img_height, img_width
img_height, img_width = 128, 128

global class_mapper
class_mapper = {0: 'Parasitized', 1: 'Uninfected'}


def load_image(img_src_path, img_height, img_width):
    img = image.load_img(img_src_path, target_size=(img_height, img_width))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    return img_tensor


@app.route('/change-image', methods=['POST'])
def change():
    image_src, random_img_class = get_random_image()
    return json.dumps({'img_src': image_src, 'img_class': random_img_class})


def get_random_image():
    img_classes = os.listdir(img_path)
    random_class_index = int(random.random() * len(img_classes))
    random_img_class = img_classes[random_class_index]

    images = os.listdir('%s/%s' % (img_path, random_img_class))
    random_image_index = int(random.random() * len(images))

    return '%s/%s/%s' % (img_path, random_img_class, images[random_image_index]), random_img_class


@app.route('/predict', methods=['POST'])
def predict():
    # Getting image path from request
    img_src = request.get_data()
    # print(img_src)

    # load a single image
    new_image = load_image(img_src, img_height, img_width)
    # check prediction
    with graph.as_default():
        pred = model.predict(new_image)
        # print(pred)
        predicted_class = 1 if pred[0][0] > 0.5 else 0
        return class_mapper[predicted_class]


@app.route('/')
def index():
    number_of_images = 4
    images = {}
    for i in range(number_of_images):
        img_src, random_img_class = get_random_image()
        images.update({img_src: random_img_class})
    # print(images)
    return render_template('index.html', images=images)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)


