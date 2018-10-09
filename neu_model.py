from keras .applications.vgg16 import VGG16
import numpy as np
from generator import get_images
import random
from keras.utils import to_categorical
import os
from keras.models import Sequential, Model
from keras.optimizers import SGD
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.regularizers import l2
from keras.initializers import RandomNormal, Zeros, Ones


X_train = list()
Y_train = list()
X_test = list()
Y_test = list()

import keras
import keras.models
import keras.layers
import keras.layers.convolutional
import keras.layers.core

base_model = VGG16(include_top=True, weights='imagenet')

model = Model(input=base_model.input, output=base_model.get_layer('fc2').output)

# model.compile(loss = 'categorical_crossentropy', optimizer =  SGD(lr = 0.01 , momentum = 0.9 ), metrics=['accuracy'] )

X_train, Y_train = get_images(X_train, Y_train)
os.chdir("..")

#features_Xtr = model.predict(X_train, verbose=1)
#np.save("Xtr",features_Xtr)

#print features_Xtr.shape

features_Xte = model.predict(X_train, verbose=1)
np.save("Xte",features_Xte)

#print features_Xte.shape

#np.save("Ytr", Y_train)
#dprint Y_train.shape

np.save("Yte", Y_train)
