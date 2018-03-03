import numpy as np
import plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *


import pandas_datareader.data as web
from datetime import datetime



dataset = [1,5,7,2,6,7,8,2,5,2,6,8,2,6,13]

def movingavarage(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas


#df = web.DataReader("USDBRL=X", 'google', datetime(2007, 10, 1), datetime(2009, 4, 1))

df = web.DataReader('BRL=X', 'yahoo')

print df

trace = go.Candlestick(x=df.index, open=df.Open, high=df.High, low=df.Low, close=df.Close)

data = [trace]
py.offline.plot(data, filename='simple_candlestick')
#py.plot(data, filename='lol')

