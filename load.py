import numpy as np
import keras.models
# import keras.models import model_from_json

def init():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    # loaded_model = model_from_json(loaded_model_json)

