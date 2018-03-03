#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def svm_classify(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    classifier = SVC(kernel='rbf', random_state=0)

    classifier.fit(x_train, y_train.values.ravel())
    y_pred = classifier.predict(x_test)

    return confusion_matrix(y_test, y_pred), classifier
