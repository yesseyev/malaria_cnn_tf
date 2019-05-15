from flask import Flask, render_template, request

import numpy as np
from keras.preprocessing import image
import sys
import os
import random
sys.path.append(os.path.abspath('./models'))

from models.load import *

# Init flask app
app = Flask(__name__)

global model_1, graph_1, model_2, graph_2
model_1, graph_1 = init(model_id=1)
model_2, graph_2 = init(model_id=2)

global img_path, img_src_template
img_path, img_src_template = './static/img/cells', '%s/%s'

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
    img_files = os.listdir(img_path)
    random_filename = img_files[int(random.random() * len(img_files))]

    return img_src_template % (img_path, random_filename)


@app.route('/predict/<int:id>', methods=['POST'])
def predict(id=1):
    if id == 2:
        model, graph = model_2, graph_2
        img_height, img_width = 128, 128
    else:
        model, graph = model_1, graph_1
        img_height, img_width = 64, 64
    # Getting image path from request
    img_src = request.get_data()
    print(img_src)

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
    img_files = os.listdir(img_path)
    random.shuffle(img_files)
    images = [img_src_template % (img_path, filename) for filename in img_files[:4]]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)


