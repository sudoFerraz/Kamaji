#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import RMSprop
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def neural_network_classify(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    
    classifier = Sequential()
    classifier.add(Dense(input_dim=len(x_train[0, :]), units=len(x_train[0, :]), activation='relu',
                         kernel_initializer='uniform'))
    classifier.add(Dense(units=2 * len(x_train[0, :]), activation='relu', kernel_initializer='uniform'))
    classifier.add(Dense(units=2 * len(x_train[0, :]), activation='relu', kernel_initializer='uniform'))
    classifier.add(Dense(units=len(x_train[0, :]), activation='relu', kernel_initializer='uniform'))
    classifier.add(Dense(units=1, activation='sigmoid', kernel_initializer='uniform'))

    optimizer = RMSprop(lr=0.00075)
    classifier.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    
    classifier.fit(x_train, y_train, batch_size=16, epochs=30, verbose=0)
    
    y_pred = classifier.predict(x_test, batch_size=16)
    y_pred = (y_pred > 0.5)
    
    return confusion_matrix(y_test, y_pred), classifier
