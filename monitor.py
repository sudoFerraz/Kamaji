#import model.py
#import dbmodel.py
import time
import numpy as np
import plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import pandas_datareader.data as web
from datetime import datetime
from forex_python.converter import CurrencyRates
import stockstats
import pandas as pd
from stockstats import StockDataFrame
import datetime as dt
import matplotlib.pyplot as plt







#start_date = dt.datetime(1995, 1, 1)
#dat = data.DataReader('USDBRL=X', 'yahoo')
#dat.to_csv('brlusd.csv', mode='w', header=True)
#stock = StockDataFrame.retype(pd.read_csv('usdbrl.csv')

while True:
    start_date = dt.datetime(1995, 1, 1)
    df = web.DataReader('BRL=X', 'yahoo')
    df.to_csv('brlusd.csv', mode='w', header=True)
    data = StockDataFrame.retype(pd.read_csv('brlusd.csv'))
    close_price = data['close']
    up_bollinger = data['boll_ub']
    low_bollinger = data['boll_lb']
    last_bollinger_up = up_bollinger[-1]
    last_bollinger_low = low_bollinger[-1]
    last_close_price = close_price[-1]
    print last_bollinger_up
    print last_bollinger_low
    print last_close_price
    #print data['macdh']
    #print data['boll_ub']
    #print data
    #print data['boll_lb']
    #print last_bollinger_up[-1]
    #trace = go.Candlestick(x=data.index, open=data.open, high=data.high, low=data.low, close=data.close)
    #trace = go.Candlestick(x=data.index, close=data.macdh)
    #data = [trace]
    #py.offline.plot(data, filename='Updated_historical')
    #c = CurrencyRates()
    #a =  c.get_rate('USD', 'BRL')
    #x = np.arange(4)
    #plt.plot(up_bollinger)
    #plt.plot(low_bollinger)
    #plt.plot(close_price)
    #print up_bollinger
    #print low_bollinger
    #plt.savefig('testingstockdata.png')
        #print a
    time.sleep(60)
