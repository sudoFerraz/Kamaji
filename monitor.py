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
    rsi_price_6 = data['rsi_6']
    rsi_price_12 = data['rsi_12']
    macd_signal_line = data['macds']
    macd = data['macd']
    macd_histogram = data['macdh']
    open_delta_against_next2day = data['open_2_d']
    change_2days_ago = data['open_-2_r']
    last_bollinger_up = up_bollinger[-1]
    last_bollinger_low = low_bollinger[-1]
    last_close_price = close_price[-1]
    last_rsi_6 = rsi_price_6[-1]
    last_rsi_12 = rsi_price_12[-1]
    last_macd_signal_line = macd_signal_line[-1]
    last_macd = macd[-1]
    last_macd_histogram = macd_histogram[-1]
    last_open_delta_against_next2day = open_delta_against_next2day[-1]
    last_change_2days_ago = change_2days_ago[-1]
    print '[+] Ultimo Close', str(last_close_price)
    print '[+] Ultimo Teto Bollinger Band', str(last_bollinger_up)
    print '[+] Ultimo Chao Bollinger Band', last_bollinger_low
    print '[+] Ultimo RSI 6 dias', str(last_rsi_6)
    print '[+] Ultimo RSI 12 dias', str(last_rsi_12)
    print '[+] Ultimo Macd', str(last_macd)
    print '[+] Ultimo Macd Signal line', str(last_macd_signal_line)
    print '[+] Ultimo Macd Histogram', str(last_macd_histogram)
    print '[+] Ultimo Open Delta Proximos 2 dias', str(last_open_delta_against_next2day)
    print '[+] Ultima Porcentagem de mudanca 2 dias atras', str(last_change_2days_ago)
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
   # plt.plot(close_price)
    plt.plot(macd)
    plt.plot(macd_signal_line)
    plt.plot(macd_histogram)
    #print up_bollinger
    #print low_bollinger
    plt.savefig('testingstockdata.png')
        #print a
    time.sleep(60)
