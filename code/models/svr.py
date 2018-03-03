#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR


def svm_regressor(x, y):
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    x = sc_x.fit_transform(x)
    y = sc_y.fit_transform(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    regressor = SVR(kernel='rbf')

    regressor.fit(x_train, y_train.ravel())
    y_pred = regressor.predict(x_test)

    return mean_squared_error(y_test, y_pred), regressor
