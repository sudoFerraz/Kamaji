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
df = pd.DataFrame()



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
    bollinger_up_mean = indicator_handler.get_indicator_by_name(session, 'bollinger_up_mean')
    bollinger_up_std = indicator_handler.get_indicator_by_name(session, 'bollinger_up_std')
    bollinger_up_standardized = indicator_handler.get_indicator_by_name(session, 'bollinger_up_standardized')
    bollinger_low_indicator = indicator_handler.get_indicator_by_name(session, 'bollinger_low')
    bollinger_low_mean = indicator_handler.get_indicator_by_name(session, 'bollinger_low_mean')
    bollinger_low_std = indicator_handler.get_indicator_by_name(session, 'bollinger_low_std')
    bollinger_low_standardized = indicator_handler.get_indicator_by_name(session, 'bollinger_low_standardized')
    bollinger_indicator = indicator_handler.get_indicator_by_name(session, 'bollinger')
    bollinger_mean = indicator_handler.get_indicator_by_name(session, 'bollinger_mean')
    bollinger_std = indicator_handler.get_indicator_by_name(session, 'bollinger_std')
    bollinger_standardized = indicator_handler.get_indicator_by_name(session, 'bollinger_standardized')
    close_price_indicator = indicator_handler.get_indicator_by_name(session, 'close_price')
    close_price_mean = indicator_handler.get_indicator_by_name(session, 'close_mean')
    close_price_std = indicator_handler.get_indicator_by_name(session, 'close_std')
    close_price_standardized = indicator_handler.get_indicator_by_name(session, 'close_standardized')
    rsi6_indicator = indicator_handler.get_indicator_by_name(session, 'rsi6')
    rsi6_mean = indicator_handler.get_indicator_by_name(session, 'rsi6_mean')
    rsi6_std = indicator_handler.get_indicator_by_name(session, 'rsi6_std')
    rsi6_standardized = indicator_handler.get_indicator_by_name(session, 'rsi6_standardized')
    rsi12_indicator = indicator_handler.get_indicator_by_name(session, 'rsi12')
    rsi12_mean = indicator_handler.get_indicator_by_name(session, 'rsi12_mean')
    rsi12_std = indicator_handler.get_indicator_by_name(session, 'rsi12_std')
    rsi12_standardized = indicator_handler.get_indicator_by_name(session, 'rsi12_standardized')
    macd_indicator = indicator_handler.get_indicator_by_name(session, 'macd')
    macd_mean = indicator_handler.get_indicator_by_name(session, 'macd_mean')
    macd_std = indicator_handler.get_indicator_by_name(session, 'macd_std')
    macd_standardized = indicator_handler.get_indicator_by_name(session, 'macd_standardized')
    macd_histogram_indicator = indicator_handler.get_indicator_by_name(session, 'macd_histogram')
    macd_histogram_mean = indicator_handler.get_indicator_by_name(session, 'macd_histogram_mean')
    macd_histogram_std = indicator_handler.get_indicator_by_name(session, 'macd_histogram_std')
    macd_histogram_standardized = indicator_handler.get_indicator_by_name(session, 'macd_histogram_standardized')
    macd_signal_line_indicator = indicator_handler.get_indicator_by_name(session, 'macd_signal_line')
    macd_signal_line_mean = indicator_handler.get_indicator_by_name(session, 'macd_signal_line_mean')
    macd_signal_line_std = indicator_handler.get_indicator_by_name(session, 'macd_signal_line_std')
    macd_signal_line_standardized = indicator_handler.get_indicator_by_name(session, 'macd_signal_line_standardized')
    change_2days_ago_indicator = indicator_handler.get_indicator_by_name(session, 'change_2days_ago')
    change_2days_ago_mean = indicator_handler.get_indicator_by_name(session, 'change_2days_ago_mean')
    change_2days_ago_std = indicator_handler.get_indicator_by_name(session, 'change_2days_ago_std')
    change_2days_ago_standardized = indicator_handler.get_indicator_by_name(session, 'change_2days_ago_standardized')
    bollinger_up_signal = False
    bollinger_low_signal = False
    rsi_signal = False
    macd_signal_line_signal = False
    macd_histogram_signal = False
    macd_signal = False
    rsi12_signal = False
    rsi6_signal = False
    change_2days_ago_signal = False

    indicadores_dataframe = []



#Inserindo e atualizando o banco de dados com os dados mais novos
    #Macd Signal
    last_macd = macd[-1]
    indicadores_dataframe.append(last_macd)
    try:
        macd_mean
        indicator_handler.update_indicator(session, macd_indicator.id, last_macd)
        indicator_handler.update_indicator(session, macd_mean.id, macd_mean)
        indicator_handler.update_indicator(session, macd_std.id)
    except:
        macd_indicator = indicator_handler.create_indicator(session, 'macd', last_macd)

    last_macd_signal_line = macd_signal_line[-1]
    indicadores_dataframe.append(last_macd_signal_line)
    try:
        macd_signal_line_indicator
        indicator_handler.update_indicator(session, macd_signal_line_indicator.id, last_macd_signal_line)
    except:
        macd_signal_line_indicator = indicator_handler.create_indicator(session, 'macd_signal_line', last_macd_signal_line)

    last_macd_histogram = macd_histogram[-1]
    indicadores_dataframe.append(last_macd_histogram)
    try:
        macd_histogram_indicator
        indicator_handler.update_indicator(session, macd_histogram_indicator.id, last_macd_histogram)
    except:
        macd_histogram_indicator = indicator_handler.create_indicator(session, 'macd_histogram', last_macd_histogram)


    last_bollinger= boll[-1]
    indicadores_dataframe.append(last_bollinger)
    try:
        bollinger_indicator
        indicator_handler.update_indicator(session, bollinger_indicator.id, last_bollinger)
    except:
        bollinger_indicator = indicator_handler.create_indicator(session, 'bollinger', last_bollinger)
    

    last_bollinger_up = up_bollinger[-1]
    indicadores_dataframe.append(last_bollinger_up)
    try:
        bollinger_up_indicator
        indicator_handler.update_indicator(session, bollinger_up_indicator.id, last_bollinger_up)
    except:
        bollinger_up_indicator = indicator_handler.create_indicator(session, 'bollinger_up', last_bollinger_up)
    if last_bollinger_up < last_close_price:
        bollinger_up_signal = True
    table.add_column("Bollinger up indicator", [str(bollinger_up_signal)])


    indicadores_dataframe.append(boll[-1])
    last_bollinger_low = low_bollinger[-1]
    indicadores_dataframe.append(last_bollinger_low)
    try:
        bollinger_low_indicator
        indicator_handler.update_indicator(session, bollinger_low_indicator.id, last_bollinger_low)
    except:
        bollinger_low_indicator = indicator_handler.create_indicator(session, 'bollinger_low', last_bollinger_low)
    if last_bollinger_low > last_close_price:
        bollinger_low_signal = True
    table.add_column("Bollinger low indicator", [str(bollinger_low_signal)])

    last_close_price = close_price[-1]
    indicadores_dataframe.append(last_close_price)
    try:
        close_price_indicator
        indicator_handler.update_indicator(session, close_price_indicator.id, last_close_price)
    except:
        close_price_indicator = indicator_handler.create_indicator(session, 'close_price', last_close_price)

    last_rsi_6 = rsi_price_6[-1]
    indicadores_dataframe.append(last_rsi_6)
    try:
        rsi6_indicator
        indicator_handler.update_indicator(session, rsi6_indicator.id, last_rsi_6)
    except:
        rsi6_indicator = indicator_handler.create_indicator(session, 'rsi6', last_rsi_6)



    last_rsi_12 = rsi_price_12[-1]
    indicadores_dataframe.append(last_rsi_12)
    try:
        rsi12_indicator
        indicator_handler.update_indicator(session, rsi12_indicator.id, last_rsi_12)
    except:
        rsi12_indicator = indicator_handler.create_indicator(session, 'rsi12', last_rsi_12)
    if last_rsi_6 > last_rsi_12:
        rsi_signal = True
    table.add_column("Rsi Indicator", [str(rsi_signal)])

    last_change_2days_ago = change_2days_ago[-1]
    indicadores_dataframe.append(last_change_2days_ago)
    try:
        change_2days_ago_indicator
        indicator_handler.update_indicator(session, change_2days_ago_indicator.id, last_change_2days_ago)
    except:
        change_2days_ago_indicator = indicator_handler.create_indicator(session, 'change_2days_ago', last_change_2days_ago)




#Calculando sinais para estrategia
    #padronizando e guardando os dados
    new_rsi6_array = data['rsi_6']
    new_rsi6_mean = new_rsi6_array.mean()
    new_rsi6_std = new_rsi6_array.std()
    new_rsi6_difference = last_rsi_6 - new_rsi6_mean
    new_rsi6_standardized = new_rsi6_difference / new_rsi6_std
    if rsi6_mean:
        indicator_handler.update_indicator(session, rsi6_mean.id, new_rsi6_mean)
        indicator_handler.update_indicator(session, rsi6_std.id, new_rsi6_std)
        indicator_handler.update_indicator(session, rsi6_standardized.id, new_rsi6_standardized)
    elif not rsi6_mean:
        indicator_handler.create_indicator(session, 'rsi6_mean', new_rsi6_mean)
        indicator_handler.create_indicator(session, 'rsi6_std', new_rsi6_std)
        indicator_handler.create_indicator(session, 'rsi6_standardized', new_rsi6_standardized)


    new_rsi12_array = data['rsi_12']


    boll_ub_array = data['boll_ub']
    boll_ub_std = boll_ub_array.std()
    boll_ub_mean = boll_ub_array.mean()
    boll_ub_difference = last_bollinger_up - boll_ub_mean
    boll_ub_standardized = boll_ub_difference / boll_ub_std
    if bollinger_up_mean:
        indicator_handler.update_indicator(session, bollinger_up_mean.id, boll_ub_mean)
        indicator_handler.update_indicator(session, bollinger_up_std.id, boll_ub_std)
        indicator_handler.update_indicator(session, bollinger_up_standardized.id, boll_ub_standardized)
    elif not bollinger_up_mean:
        indicator_handler.create_indicator(session, 'bollinger_up_mean', boll_ub_mean)
        indicator_handler.create_indicator(session, 'bollinger_up_std', boll_ub_std)
        indicator_handler.create_indicator(session, 'bollinger_up_standardized', boll_ub_standardized)
        
    

    boll_lb_array = data['boll_lb']
    boll_lb_std = boll_lb_array.std()
    boll_lb_mean = boll_lb_array.mean()
    boll_lb_difference = last_bollinger_low - boll_lb_mean
    boll_lb_standardized = boll_lb_difference / boll_lb_std
    if bollinger_low_mean:
        indicator_handler.update_indicator(session, bollinger_low_mean.id, boll_lb_mean)
        indicator_handler.update_indicator(session, bollinger_low_std.id, boll_lb_std)
        indicator_handler.update_indicator(session, bollinger_low_standardized.id, boll_lb_standardized)
    elif not bollinger_low_mean:
        indicator_handler.create_indicator(session, 'bollinger_low_mean', boll_lb_mean)
        indicator_handler.create_indicator(session, 'bollinger_low_std', boll_lb_std)
        indicator_handler.create_indicator(session, 'bollinger_low_standardized', boll_lb_standardized)

    boll_array = data['boll']
    boll_std = boll_array.std()
    boll_mean = boll_array.mean()
    boll_difference = last_bollinger - boll_mean
    boll_standardized = boll_difference / boll_std
    if bollinger_mean:
        indicator_handler.update_indicator(session, bollinger_mean.id, boll_mean)
        indicator_handler.update_indicator(session, bollinger_std.id, boll_std)
        indicator_handler.update_indicator(session, bollinger_standardized.id, boll_standardized)
    elif not bollinger_mean:
        indicator_handler.create_indicator(session, 'bollinger_mean', boll_mean)
        indicator_handler.create_indicator(session, 'bollinger_std', boll_std)
        indicator_handler.create_indicator(session, 'bollinger_standardized', boll_standardized)


    new_macd_array = data['macd']
    new_macd_std = new_macd_array.std()
    new_macd_mean = new_macd_array.mean()
    new_macd_difference = last_macd - new_macd_mean
    new_macd_standardized = new_macd_difference / new_macd_std
    if macd_mean:
        indicator_handler.update_indicator(session, macd_mean.id, new_macd_mean)
        indicator_handler.update_indicator(session, macd_std.id, new_macd_std)
        indicator_handler.update_indicator(session, macd_standardized.id, new_macd_standardized)
    elif not macd_mean:
        indicator_handler.create_indicator(session, 'macd_mean', new_macd_mean)
        indicator_handler.create_indicator(session, 'macd_std', new_macd_std)
        indicator_handler.create_indicator(session, 'macd_standardized', new_macd_standardized)

    new_macd_histogram_array = data['macdh']
    new_macd_histogram_std = new_macd_histogram_array.std()
    new_macd_histogram_mean = new_macd_histogram_array.mean()
    new_macd_histogram_difference = last_macd_histogram - new_macd_histogram_mean
    new_macd_histogram_standardized = new_macd_histogram_difference / new_macd_histogram_std
    if macd_histogram_mean:
        indicator_handler.update_indicator(session, macd_histogram_mean.id, new_macd_histogram_mean)
        indicator_handler.update_indicator(session, macd_histogram_std.id, new_macd_histogram_std)
        indicator_handler.update_indicator(session, macd_histogram_standardized.id, new_macd_standardized)
    elif not macd_histogram_mean:
        indicator_handler.create_indicator(session, 'macd_histogram_mean', new_macd_histogram_mean)
        indicator_handler.create_indicator(session, 'macd_histogram_std', new_macd_histogram_std)
        indicator_handler.create_indicator(session, 'macd_histogram_standardized', new_macd_histogram_standardized)
    
    new_macd_signal_line_array = data['macds']
    new_macd_signal_line_std = new_macd_signal_line_array.std()
    new_macd_signal_line_mean = new_macd_signal_line_array.mean()
    new_macd_signal_line_difference = last_macd_signal_line - new_macd_signal_line_mean
    new_macd_signal_line_standardized = new_macd_signal_line_difference / new_macd_signal_line_std
    if macd_signal_line_mean:
        indicator_handler.update_indicator(session, macd_signal_line_mean.id, new_macd_signal_line_mean)
        indicator_handler.update_indicator(session, macd_signal_line_std.id, new_macd_signal_line_std)
        indicator_handler.update_indicator(session, macd_signal_line_standardized.id, new_macd_signal_line_standardized)
    elif not macd_signal_line_mean:
        indicator_handler.create_indicator(session, 'macd_signal_line_mean', new_macd_signal_line_mean)
        indicator_handler.create_indicator(session, 'macd_signal_line_std', new_macd_signal_line_std)
        indicator_handler.create_indicator(session, 'macd_signal_line_standardized', new_macd_signal_line_standardized)


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
    
    



    #trace = go.Candlestick(x=data.index, open=data.open, high=data.high, low=data.low, close=data.close)
    #trace = go.Candlestick(x=data.index, close=data.macdh)
    #data = [trace]
    #py.offline.plot(data, filename='Updated_historical')
    plt.plot(macd)
    plt.plot(macd_signal_line)
    plt.plot(macd_histogram)
    plt.savefig('testingstockdata.png')
        #print a
    time.sleep(600)
