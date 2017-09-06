# Artificial Neural Network

####################################### Data processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Encode la catégorie Pays
labelencoder_Geo = LabelEncoder()
X[:, 1] = labelencoder_Geo.fit_transform(X[:, 1])
# Encode la catégorie Sexe
labelencoder_Sexe = LabelEncoder()
X[:, 2] = labelencoder_Sexe.fit_transform(X[:, 2])
# Decoupe la colonne de categorie Pays en 3 colonne
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
# On peut supprimer une colonne des 3 colonne correspondant au pays
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling, pour avoir les valeurs dans le meme ordre de grandeurs (pour une comparaison efficace)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Importing Keras and packages 
import keras
from keras.models import Sequential
from keras.layers import Dense

####################################### Construction du reseau de neurone

#Initialising the ANN
classifier = Sequential()

#Adding the input layer and the first hidden layer
# output_dim = nb_entree + nb_sortie /2
# input_dim = 11 --> 11 variables independantes
# uniform --> initialise le poids des connections
# use the rectifier fonction en entrée et entre les differentes couches de neurones 
# (0 ou plusieurs valeurs possibles)
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
# output_dim = nb_entree + nb_sortie /2
# uniform --> initialise le poids des connections
# use the rectifier fonction en entrée et entre les differentes couches de neurones 
# (0 ou plusieurs valeurs possibles)
# Nombres input a initialisé que sur la premeiere couche
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

# Adding the output layer
# output layer --> 1 etat bianire
# Signal de sortie --> sigmoid activation (1 ou 0)
# Si plusieurs categories a plusieurs valeurs en sortie : output = nb valeurs 
# et activation = 'softmax'
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

####################################### Compiling the ANN

# optimizer : algorithme choisi pour trouver le model (le plus puissant)
# adam --> Stochastic Gradient Descent
# loss : Si deux valeurs en sortie (binairie outcome) : binary_crossentropy
#        Si plus de deux valeurs : categorical_crossentropy
# metrics : 
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

####################################### Training the ANN

# Fitting the ANN to the Training set
# x : matrice d'entrée d'apprentissage
# y : matrice de sortie d'apprentissage
# update the weights after each observation (Reinforcement Learning)
# update the weights after a batch of observations (Batch Learning) 

# In general: Larger batch sizes result in faster progress in training, 
# but don't always converge as fast. Smaller batch sizes train slower, 
# but can converge faster. It's definitely problem dependent.

# In general, the models improve with more epochs of training, to a point. 
# They'll start to plateau in accuracy as they converge. 
# Try something like 50 and plot number of epochs (x axis) vs. accuracy (y axis). 
# You'll see where it levels out.

classifier.fit(X_train, y_train, batch_size =10, epochs=100)

####################################### Making the prediction 

# Making the prediction and evaluating the model 
# Predicting the Test set results (En pourcentage)
y_pred = classifier.predict(X_test)

# Conversion en True ou False les prediction
# Si y_pred > 0.5 : True 
y_pred_binary = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred_binary)

good_prediction = cm[0, 0] + cm[1, 1]
bad_prediction = cm[1, 0] + cm[0, 1]

pourcentage_good_prediction = good_prediction * 100 / (good_prediction + bad_prediction)

####################################### Homework

dataset_to_pred = pd.read_csv('to_pred.csv')
X_to_pred = dataset_to_pred.iloc[:, 3:13].values

# Encode la catégorie Pays
X_to_pred[:, 1] = labelencoder_Geo.transform(X_to_pred[:, 1])
# Encode la catégorie Sexe
X_to_pred[:, 2] = labelencoder_Sexe.transform(X_to_pred[:, 2])
# Decoupe la colonne de categorie Pays en 3 colonne
X_to_pred = onehotencoder.transform(X_to_pred).toarray()
# On peut supprimer une colonne des 3 colonne correspondant au pays
X_to_pred = X_to_pred[:, 1:]

X_to_pred = sc.transform(X_to_pred)

pred = classifier.predict(X_to_pred)


