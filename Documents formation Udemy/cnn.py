# Convolutional Neural Network 

# Part 1 - Building the CNN 

from keras.models import Sequential # Initialiser les couches du réseau de neurones 
from keras.layers import Convolution2D # Convolution 
from keras.layers import MaxPooling2D # Pooling step 
from keras.layers import Flatten # Convert Pool into vectors (connexions) 
from keras.layers import Dense # Add the fully connected layers 

# initialising the CNN 
classifier = Sequential()

# Step 1  - convolution 
# Paramètres de la matrice de détection, couleurs, taille, etc 
classifier.add(Convolution2D(32, 3, 3, input_shape=(64, 64, 3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2))) 

# Step 1  - convolution 
# Paramètres de la matrice de détection, couleurs, taille, etc 
classifier.add(Convolution2D(32, 3, 3, activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2))) 
 
# Step 3 - Flattening 
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu')) 
classifier.add(Dense(output_dim = 1, activation = 'sigmoid')) 

# Compilation of the CNN 
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images 
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        train_generator,
        steps_per_epoch=200,
        epochs=5,
        validation_data=validation_generator,
        validation_steps=200)

#Save the learning 
#classifier.save('sauvegarde.tfl')

#serialise model to json
classifier_json = classifier.to_json()
with open('model.json', "w") as json_file :
    json_file.write(classifier_json)
    
# serialize weights to HDF5
classifier.save_weights("model.h5")
print("Classifier save on disk")

# Load json and create model
from keras.models import model_from_json
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

#load weights into new model
loaded_model.load_weights('model.h5')
print("Loaded model from disk")

#Making a prediction 

import numpy as np
from keras.preprocessing import image

# Load the image with keras 
# arg : path / target_size same as the test_set
test_image = image.load_img('dataset/single_prediction/ok.jpg', target_size=(64, 64))
# passer l'image en tableau
test_image = image.img_to_array(test_image)

#test method
#mauvais format, il faut ajouter une dimension au test 
test_image = np.expand_dims(test_image, axis = 0)
classifier.predict(test_image)

#Correspondance 
result  = classifier.predict(test_image)

# 1 est un chat ou un chien ???
train_generator.class_indices

if result [0][0] == 1: 
    prediction='dog'
else:
    predition='cat'

