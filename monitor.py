import model
import auxiliary
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
from pyfiglet import Figlet
from prettytable import PrettyTable
table = PrettyTable()

f = Figlet(font='epic')
print f.renderText('Kamaji')






#start_date = dt.datetime(1995, 1, 1)
#dat = data.DataReader('USDBRL=X', 'yahoo')
#dat.to_csv('brlusd.csv', mode='w', header=True)
#stock = StockDataFrame.retype(pd.read_csv('usdbrl.csv')
os_tools = auxiliary.ostools()
session = os_tools.db_connection()
user_handler = auxiliary.user_handler()
data_handler = auxiliary.data_handler()
signal_handler = auxiliary.signal_handler()
notification_handler = auxiliary.notification_handler()
invoice_handler = auxiliary.invoice_handler()
action_handler = auxiliary.action_handler()
graph_storage = auxiliary.graph_storage()
indicator_handler = auxiliary.indicator_handler()







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
    close_20_sma = data['close_20_sma']
    close_20_mstd = data['close_20_mstd']
    boll = data['boll']
    close_12_ema = data['close_12_ema']
    close_26_ema = data['close_26_ema']
    last_close_price = close_price[-1]



    data.to_csv('brl_usd_indicators.csv', mode='w', header=True)

    bollinger_up_indicator = indicator_handler.get_indicator_by_name(session, 'bollinger_up')
    bollinger_low_indicator = indicator_handler.get_indicator_by_name(session, 'bollinger_low')
    close_price_indicator = indicator_handler.get_indicator_by_name(session, 'close_price')
    rsi6_indicator = indicator_handler.get_indicator_by_name(session, 'rsi6')
    rsi_12_indicator = indicator_handler.get_indicator_by_name(session, 'rsi12')
    macd_indicator = indicator_handler.get_indicator_by_name(session, 'macd')
    macd_histogram_indicator = indicator_handler.get_indicator_by_name(session, 'macd_histogram')
    macd_signal_line_indicator = indicator_handler.get_indicator_by_name(session, 'macd_signal_line')
    change_2days_ago_indicator = indicator_handler.get_indicator_by_name(session, 'change_2days_ago')
    bollinger_up_signal = False
    bollinger_low_signal = False
    rsi_signal = False
    macd_signal_line_signl = False
    macd_histogram_signal = False


    last_bollinger_up = up_bollinger[-1]
    try:
        bollinger_up_indicator
        indicator_handler.update_indicator(session, bollinger_up_indicator.id, last_bollinger_up)
    except:
        bollinger_up_indicator = indicator_handler.create_indicator(session, 'bollinger_up', last_bollinger_up)
    if last_bollinger_up < last_close_price:
        bollinger_up_signal = True
    table.add_column("Bollinger up indicator", [str(bollinger_up_signal)])


    last_bollinger_low = low_bollinger[-1]
    try:
        bollinger_low_indicator
        indicator_handler.update_indicator(session, bollinger_low_indicator.id, last_bollinger_low)
    except:
        bollinger_low_indicator = indicator_handler.create_indicator(session, 'bollinger_low', last_bollinger_low)
    if last_bollinger_low > last_close_price:
        bollinger_low_signal = True
    table.add_column("Bollinger low indicator", [str(bollinger_low_signal)])

    last_close_price = close_price[-1]
    try:
        close_price_indicator
        indicator_handler.update_indicator(session, close_price_indicator.id, last_close_price)
    except:
        close_price_indicator = indicator_handler.create_indicator(session, 'close_price', last_close_price)

    last_rsi_6 = rsi_price_6[-1]
    try:
        rsi6_indicator
        indicator_handler.update_indicator(session, rsi6_indicator.id, last_rsi_6)
    except:
        rsi6_indicator = indicator_handler.create_indicator(session, 'rsi6', last_rsi_6)



    last_rsi_12 = rsi_price_12[-1]
    try:
        rsi_12_indicator
        indicator_handler.update_indicator(session, rsi_12_indicator.id, last_rsi_12)
    except:
        rsi12_indicator = indicator_handler.create_indicator(session, 'rsi12', last_rsi_12)
    if last_rsi_6 > last_rsi_12:
        rsi_signal = True
    table.add_column("Rsi Indicator", [str(rsi_signal)])

    last_macd_signal_line = macd_signal_line[-1]
    try:
        macd_signal_line_indicator
        indicator_handler.update_indicator(session, macd_signal_line_indicator.id, last_macd_signal_line)
    except:
        macd_signal_line_indicator = indicator_handler.create_indicator(session, 'macd_signal_line', last_macd_signal_line)

    last_macd_histogram = macd_histogram[-1]
    try:
        macd_histogram_indicator
        indicator_handler.update_indicator(session, macd_histogram_indicator.id, last_macd_histogram)
    except:
        macd_histogram_indicator = indicator_handler.create_indicator(session, 'macd_histogram', last_macd_histogram)



    last_change_2days_ago = change_2days_ago[-1]
    try:
        change_2days_ago_indicator
        indicator_handler.update_indicator(session, change_2days_ago_indicator.id, last_change_2days_ago)
    except:
        change_2days_ago_indicator = indicator_handler.create_indicator(session, 'change_2days_ago', last_change_2days_ago)
    print "[+][+] Status do mercado no momento [+][+]"
    print "\n"
    t = PrettyTable()
    t.add_column("Close", [last_close_price])
    t.add_column("Change 2 dias", [last_change_2days_ago])
    print t
    print "\n"
    print "[+] Indicadores Ativos [+]"
    print "\n"

    print '[+] Ultimo Teto Bollinger Band', str(last_bollinger_up)
    print '[+] Ultimo Chao Bollinger Band', last_bollinger_low
    print "[+] Ultimo Desvio Padrao Bollinger Bands", str(boll[-1])
    print '[+] Ultimo RSI 6 dias', str(last_rsi_6)
    print '[+] Ultimo RSI 12 dias', str(last_rsi_12)
#    print '[+] Ultimo Macd', str(last_macd)
    print '[+] Ultimo Macd Signal line', str(last_macd_signal_line)
    print '[+] Ultimo Macd Histogram', str(last_macd_histogram)
    print "[+] Ultimo SMA 20 dias", str(close_20_sma[-1])
    print "[+] Ultimo MSTD 20 dias", str(close_20_mstd[-1])
    print "[+] Ultimo EMA 12 dias", str(close_12_ema[-1])
    print "[+] Ultimo EMA 26 dias", str(close_26_ema[-1])
    print "\n"
    print "\n"
    print "********************************************************************"
    print "\n"
    print "\n"
    print "[+] Sinais Ativos [+]"
    print "\n"
    print table
    if rsi_signal:
        print "[+] Sinal RSI 6D > 12D Ativo"
        print "[++] Distancia dos desvios padroes de %0.3f" % (last_rsi_6 - last_rsi_12)

    if bollinger_low_signal:
        print "[+] Sinal Bollinger Band Lower Band"
        print "[++] Distancia de %0.3f ate a borda inferior" % (last_bollinger_low - last_close_price)
    if bollinger_up_signal:
        print "[+] Sinal Bollinger Band Upper Band"
        print "[++] Distancia de %0.3f ate a borda superior" % (last_close_price - last_bollinger_up)

    print ""
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
