import cv2
import os
from random import shuffle
import numpy

image_dir = "/home/Madhu/TensorBros/New/Test"
categories = ['Cookery', 'Dance', 'Sports']

X_train = list()
Y_train = list()
X_t = list()
Y_t = list()

def get_images(X_train, Y_train):
    os.chdir(image_dir)
    for category in categories:
        image_files = [image_dir + "/" + category + "/" + f for f in os.listdir(image_dir + "/" + category) if f[-4:] == ".jpg" or f[-4:] == ".JPG"]
        os.chdir(category)
        print category
        for image_file in image_files:
            img = cv2.imread(image_file, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgs = list()
            imgs.append(img)

            for img1 in imgs:
                # print img1.shape
                    X_t.append(img1)
                    Y_t.append(categories.index(category))
        os.chdir("..")
    print numpy.array(X_t).shape

    return numpy.array(X_t), numpy.array(Y_t)

#X_train, Y_train = get_images(X_train, Y_train)
print numpy.array(Y_train).shape
