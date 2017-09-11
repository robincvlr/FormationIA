# Convolutional Neural Network

# Building the CNN

# Importing the keras librairies and packages
from keras.models import Sequential # initilisation du reseau neurones (couches/entree/sortie)
from keras.layers import Convolution2D # Convolution 
from keras.layers import MaxPooling2D # Pooling step
from keras.layers import Flatten # Flatting 
from keras.layers import Dense # Connecter tous les neurones 

# Initialise le CNN
classifier = Sequential()

# Convolution Step 1
# 32 --> nombre filters : nombre matrice detection ?
# 3, 3 --> kernel_size
# input_shape --> 64, 64 --> plage de couleur et 3 channel car en couleur 1 si noir et blanc
# activation --> fonction d activation
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation= 'relu'))

# Pooling step
# pool_size= (2,2) --> reduit la matrice obtenu apres convolution sans perdre d info
classifier.add(MaxPooling2D(pool_size= (2,2)))

# Flattening step
# convertir la matrice de Pooling en verteur d entrée a une seule dimension
# Kares va gerer : pas besoin d entree
classifier.add(Flatten())

# Full connection : faire un reseau de neurone ANN 
# Make a hiiden layer
classifier.add(Dense(output_dim = 128, activation= 'relu'))
# Make the output layer
classifier.add(Dense(output_dim = 1, activation= 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the CNN to the images
# Image augmentation process
# Creer un jeux de donner avec plus d image (rotation/zoom/...)
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

# target_size --> dimension de l image definie plus haut
# class_mode --> binary car uniquement deux valeurs
training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=2000,
        epochs=25,
        validation_data=test_set,
        validation_steps=200)

