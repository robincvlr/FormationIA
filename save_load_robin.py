#SAVE

# fragment of learn.py
# whole file can be found in repository
# links below
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
model = Sequential()
model.add(...)
 
# layers omitted for clarity
 
model.compile(...)
model.fit(...)
 
# here we actually save trained model
model.save('model.h5')

#LOAD

# predict.py
import argparse
import sys
import os
import glob
import numpy as np
 
from keras.models import load_model as load_keras_model
from keras.preprocessing.image import img_to_array, load_img
 
# disable TF debugging info
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
 
# our saved model file
# may be refactored to be taken from command line
model_filename = 'model.h5'
class_to_name = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]
 
 
def get_filenames():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='*', default=['**/*.*'])
    args = parser.parse_args()
 
    for pattern in args.filename:
        # here we recursively look for input
        # files using provided glob patterns
        for filename in glob.iglob('data/' + pattern, recursive=True):
            yield filename
 
 
def load_model():
    if os.path.exists(model_filename):
        return load_keras_model(model_filename)
    else:
        print("File {} not found!".format(model_filename))
        exit()
 
 
def load_image(filename):
    img_arr = img_to_array(load_img(filename))
    return np.asarray([img_arr])
 
 
def predict(image, model):
    result = np.argmax(model.predict(image))
    return class_to_name[result]
 
 
if __name__ == '__main__':
    filenames = get_filenames()
    keras_model = load_model()
    for filename in filenames:
        image = load_image(filename)
        image_class = predict(image, keras_model)
        print("{:30}   {}".format(filename, image_class))