from flask import Flask, render_template, request

from scipy.misc import imsave, imread, imresize
import numpy as np
# import keras.models
import re
import sys
import os
# sys.path.append(os.path.abspath('./model'))

# from load import *

# Init flask app
app = Flask(__name__)

global model, graph
# model, graph = init()


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)


