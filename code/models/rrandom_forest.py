#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def random_forest_regressor(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
    
    sc_X = StandardScaler()
    x_train = sc_X.fit_transform(x_train)
    x_test = sc_X.transform(x_test)
    sc_y = StandardScaler()
    y_train = sc_y.fit_transform(y_train)
    y_test = sc_y.fit_transform(y_test)

    regressor = RandomForestRegressor(n_estimators = 100, criterion='mse', random_state = 42)
    
    regressor.fit(x_train, y_train.ravel())
    y_pred = regressor.predict(x_test)
    
    return mean_squared_error(y_test, y_pred), regressor
