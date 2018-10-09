from keras.applications.inception_v3 import InceptionV3
from keras .applications.vgg16 import VGG16
import numpy as np
import random
from keras.utils import to_categorical
import os
from keras.models import Sequential, Model
from keras.optimizers import SGD
from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.models import load_model
from keras.layers import Input
from keras.regularizers import l2
from keras.initializers import RandomNormal, Zeros, Ones
import cv2
from sklearn.externals import joblib
import os

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

model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
"""for layer in model.layers:
    print layer.name
"""
clf=joblib.load("extra_tree.pkl")

def imagefromvideos(filename):
    import subprocess as sp
    cmd='ffmpeg -i ' + filename + ' -ss 00:00:10 -r 1 -s 224x224 -f image2 /home/madhura/Madhu/TensorBros/temp/%d.jpeg'
    sp.call(cmd,shell=True)


def generate_features(img):
    #print "testing here"
    features = model.predict(img.reshape((1, 224, 224, 3)), verbose=1)
    #print "testing done"
    return features

def get_proba(img):
    #img = cv2.resize(img, (224, 224))
    #print img.shape
    features = generate_features(np.array(img))
    predict_proba = clf.predict(features)
    return predict_proba

def get_result(video_path):
    imagefromvideos(video_path + '.mp4')
    image_dir = "/home/madhura/Madhu/TensorBros/temp"
    # print ("hfh")
    # for f in os.listdir(image_dir):
    #     print ("fdsfaaaaaaaaa")
    #     if f[-5:] == ".jpeg" or f[-4:] == ".JPG":
    #         print("fdsf")
    # print 'hi1'
    image_files = [image_dir + "/" + f for f in os.listdir(image_dir) if f[-5:] == ".jpeg" or f[-4:] == ".JPG"]
    #os.chdir(image_dir)
    # print 'hi'
    op = np.array([0]*np.array(image_files).shape)
    print np.array(image_files).shape
    for image_file in image_files:
        img = cv2.imread(image_file, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print 'hi2'
        op[get_proba(img)] = op[get_proba(img)] + 1

    op = np.array(op);
    i = np.argmax(op);
    print "cat=", i


    for the_file in os.listdir(image_dir):
        file_path = os.path.join(image_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    return 'python success'
