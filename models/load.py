from keras.models import model_from_json
import tensorflow as tf


def get_loaded_model(json_path, weights_path):
    # Loading model from JSON
    json_file = open(json_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # Loading weights into new model
    loaded_model.load_weights(weights_path)

    # Compiling loaded model
    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return loaded_model


def init():
    # Loading and compiling model
    json_model, weights_model = './models/model_cnn_4.json', './models/model_cnn_4.h5'
    model = get_loaded_model(json_model, weights_model)

    graph = tf.get_default_graph()
    return model, graph
