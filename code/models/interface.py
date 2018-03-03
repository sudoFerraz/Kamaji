#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import crandom_forest as crf
import neural_network as nn_model
import numpy as np
import pandas as pd
import rrandom_forest as rrf
import svm as svc
import svr as svr
from tqdm import tqdm


def fill_values(df):
    names = df.columns.get_values()

    bar = tqdm(total=len(names))
    for name in names:
        df[name].replace([np.inf, -np.inf], np.nan)
        df[name].fillna(method='ffill', inplace=True)
        df[name].fillna(method='bfill', inplace=True)
        bar.update(1)

    bar.close()

    return df


def model_and_accuracy(df, y, y_regress):
    pd.set_option('use_inf_as_na', True)
    df = fill_values(df)
    dict = {}

    x = df.iloc[:, range(len(df.columns.get_values()))].values

    dict['svr'] = svr.svm_regressor(x, y_regress)

    nn_cm, model = nn_model.neural_network_classify(x, y)
    dict['nn'] = (nn_cm[0, 0] + nn_cm[1, 1]) / (sum(nn_cm[0]) + sum(nn_cm[1])), model

    crf_cm, model = crf.random_forest_classify(x, y)
    dict['crf'] = (crf_cm[0, 0] + crf_cm[1, 1]) / (sum(crf_cm[0]) + sum(crf_cm[1])), model

    dict['rrf'] = rrf.random_forest_regressor(x, y_regress)

    svc_cm, model = svc.svm_classify(x, y)
    dict['svm'] = (svc_cm[0, 0] + svc_cm[1, 1]) / (sum(svc_cm[0]) + sum(svc_cm[1])), model

    return dict
