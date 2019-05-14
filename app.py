from flask import Flask, render_template, request

from scipy.misc import imsave, imread, imresize
import numpy as np
# import keras.models
import re
import sys
import os
import random
# sys.path.append(os.path.abspath('./model'))

# from load import *

# Init flask app
app = Flask(__name__)

global model, graph
# model, graph = init()

global img_path, img_src_template
img_path, img_src_template = './static/img/cells', '.%s/%s'


@app.route('/change-image', methods=['POST'])
def change():
    img_files = os.listdir(img_path)
    random_filename = img_files[int(random.random() * len(img_files))]

    return img_src_template % (img_path, random_filename)


@app.route('/')
def index():
    img_files = os.listdir(img_path)
    random.shuffle(img_files)
    images = [img_src_template % (img_path, filename) for filename in img_files[:4]]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)


