import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Flatten, Convolution2D, AveragePooling2D, Dropout
from keras.optimizers import Adam



filterAmount = 32
inputshape = (32,32,3) #32x32 image with 3 layers for example r(ed)g(green)b(lue)

def createLeNetModel():
    model = Sequential()
    model.add(Convolution2D(filters = filterAmount, input_shape = inputshape, kernel_size=(3,3), activation='relu', strides=(1, 1)))
    model.add(AveragePooling2D(pool_size=(2,2), strides=(2,2)))

    model.add(Dropout(0.5))

    model.add(Convolution2D(filters=filterAmount, kernel_size=(3,3), strides=(1, 1)))

    model.add(Dropout(0.5))

    model.add(AveragePooling2D(pool_size=(2, 2), strides=(2,2)))

    model.add(Flatten())

    model.add(Dense(units=filterAmount, activation='relu'))
    model.add(Dense(units=filterAmount, activation='relu'))
    model.add(Dense(activation='sigmoid'))

    model.compile(Adam(lr = 0.001))

    return model
