import model
import auxiliary
import monitor
import strategy_observer
import time
from time import sleep
import numpy as np
import pandas_datareader.data as web
from datetime import datetime
import stockstats
import pandas as pd
from stockstats import StockDataFrame
import datetime as dt
#import matplotlib.pyplot as plt
from pyfiglet import Figlet
from prettytable import PrettyTable
table = PrettyTable()


while True:
    try:
        monitor.monitor()
    except:
        pass
    try:
        strategy_observer.strategy_observer()
    except:
        pass
    f = Figlet(font='epic')
    print f.renderText('Kamaji')

    os_tools = auxiliary.ostools()
    session = os_tools.db_connection()
    user_handler = auxiliary.user_handler()
    indicator_handler = auxiliary.indicator_handler()
    signal_handler = auxiliary.signal_handler()
    invoice_handler = auxiliary.invoice_handler()


    start_date = dt.datetime(1995, 1, 1)
    try:
        df = web.DataReader('BRL=X', 'yahoo')
        df.to_csv('brlusd.csv', mode='w', header=True)
    except:
        pass
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
    data.to_csv('all_indicators.csv', mode='w', header=True)

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

    bollinger_up_signal =  signal_handler.get_signal_by_indicator(session, bollinger_up_indicator.id)
    bollinger_low_signal = signal_handler.get_signal_by_indicator(session, bollinger_low_indicator.id)
    macd_histogram_signal = signal_handler.get_signal_by_indicator(session, macd_histogram_indicator.id)
    rsi6_signal = signal_handler.get_signal_by_indicator(session, rsi6_indicator.id)
    macd_signal = signal_handler.get_signal_by_indicator(session, macd_indicator.id)

   # print "[+][+] Status do mercado no momento [+][+]"
   # print "\n"
   # t = PrettyTable()
   # t.add_column("Close", [close_price_indicator.value])
   # t.add_column("Change 2 dias", [change_2days_ago_indicator.value])
   # print t
   # print "\n"
   # print "[+] Indicadores Ativos [+]"
   # print "\n"
   # print '[+] Ultimo Teto Bollinger Band ' + str(bollinger_up_indicator.value)
   # print '[+] Ultimo Chao Bollinger Band ' + str(bollinger_low_indicator.value)
   # print "[+] Ultimo EMA Bollinger Band " + str(bollinger_indicator.value)
   # print '[+] Ultimo RSI 6 dias ' + str(rsi6_indicator.value)
   # print '[+] Ultimo RSI 12 dias ' +  str(rsi12_indicator.value)
   # print '[+] Ultimo Macd ' + str(macd_indicator.value)
   # print '[+] Ultimo Macd Signal line ' + str(macd_signal_line_indicator.value)
   # print '[+] Ultimo Macd Histogram ' + str(macd_histogram_indicator.value)
   # print "[+] Ultimo SMA 20 dias ", str(close_20_sma[-1])
   # print "[+] Ultimo MSTD 20 dias ", str(close_20_mstd[-1])
   # print "[+] Ultimo EMA 12 dias ", str(close_12_ema[-1])
   # print "[+] Ultimo EMA 26 dias ", str(close_26_ema[-1])
   # print "\n"
   # print "\n"
   # print "********************************************************************"
   # print "\n"
   # print "\n"
   # print "[+] Sinais Ativos [+]"
   # print "\n"
   # table = PrettyTable(["Signal name", "Active", "Relevancia", "Fora do padrao"])
   # table.align["Signal name"] = "1"
   # table.padding_width = 1
   # if bollinger_up_signal:
   #     table.add_row(["Bollinger Band UB", "True", bollinger_up_signal.accuracy, bollinger_up_standardized.value])
   # else:
   #     table.add_row(["Bollinger Band UB", "False", "0", "-"])
   # if bollinger_low_signal:
   #     table.add_row(["Bollinger Band LB", "True", bollinger_low_signal.accuracy, bollinger_low_standardized.value])
   # else:
   #     table.add_row(["Bollinger Band LB", "False", "0", "-"])
   # if macd_histogram_signal:
   #     table.add_row(["MACD Histogram", "True", macd_histogram_signal.accuracy, macd_histogram_standardized.value])
   # else:
   #     table.add_row(["MACD Histogram", "False", "0", "-"])
   # if macd_signal:
   #     table.add_row(["MACD Cross", "True", macd_signal.accuracy, macd_standardized.value])
   # else:
   #     table.add_row(["MACD Cross", "False", "0", "-"])
   # if rsi6_signal:
   #     table.add_row(["Relative Strength Index", "True", rsi6_signal.accuracy, rsi6_standardized.value])
   # else:
   #     table.add_row(["Relative Strength Index", "False", "0", "-"])
#
#    if bollinger_low_signal and macd_histogram_signal and macd_signal and rsi6_signal:
#        buy = Figlet(font='contessa')
#        print buy.renderText('TENDENCIA DE SUBIDA CONSERVADORA')
#    elif bollinger_up_signal:
#        buy = Figlet(font='contessa')
#        print buy.renderText('TENDENCIA DE CORRECAO PARA BAIXO')
#    elif macd_histogram_signal and macd_signal and rsi6_signal:
#        buy = Figlet(font='contessa')
#        print buy.renderText('TENDENCIA DE SUBIDA ARRISCADA')
#    else:
#        hold = Figlet(font='mini')
#        print hold.renderText('TENDENCIA DE RISCO RELATIVO ALTO')
#    print "\n"
#    print table
    sleep(60)
