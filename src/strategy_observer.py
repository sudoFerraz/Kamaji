import model
import auxiliary
import time
import numpy as np
import pandas_datareader.data  as web
from time import sleep
from datetime import datetime
import stockstats
import pandas as pd
from stockstats import StockDataFrame
import datetime as dt
#import matplotlib.pyplot as plt
from pyfiglet import Figlet
from prettytable import PrettyTable
table = PrettyTable()
df = pd.DataFrame()

f = Figlet(font='epic')
print f.renderText('Strategy')

os_tools = auxiliary.ostools()
session = os_tools.db_connection()
user_handler = auxiliary.user_handler()
data_handler = auxiliary.data_handler()
signal_handler = auxiliary.signal_handler()
notification_handler = auxiliary.notification_handler()
invoice_handler = auxiliary.invoice_handler()
indicator_handler = auxiliary.indicator_handler()


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



def strategy_observer():

    bollinger_up_signal =  signal_handler.get_signal_by_indicator(session, bollinger_up_indicator.id)
    bollinger_low_signal = signal_handler.get_signal_by_indicator(session, bollinger_low_indicator.id)
    macd_histogram_signal = signal_handler.get_signal_by_indicator(session, macd_histogram_indicator.id)
    rsi6_signal = signal_handler.get_signal_by_indicator(session, rsi6_indicator.id)
    macd_signal = signal_handler.get_signal_by_indicator(session, macd_indicator.id)

    #bollinger up signal calculation
    if bollinger_up_signal:
        if close_price_indicator.value < bollinger_up_indicator.value:
            signal_handler.delete_signal(session, bollinger_up_signal.id)
        elif close_price_indicator.value >= bollinger_up_indicator.value:
            bollinger_up_signal = signal_handler.update_signal(session, bollinger_up_signal.id, close_price_indicator.value - bollinger_up_indicator.value)
    else:
        if close_price_indicator.value >= bollinger_up_indicator.value:
            bollinger_up_signal = signal_handler.create_signal(session, bollinger_up_indicator.id, close_price_indicator.value - bollinger_up_indicator.value)

    #bollinger low signal calculation
    if bollinger_low_signal:
        if close_price_indicator.value > bollinger_low_indicator.value:
            signal_handler.delete_signal(session, bollinger_low_signal.id)
        elif close_price_indicator.value <= bollingeR_low_indicator.value:
            bollinger_low_signal =signal_handler.update_signal(session, bollinger_low_signal.id, close_price_indicator.value - bollinger_low_indicator.value)
    else:
        if close_price_indicator <= bollinger_low_indicator.value:
            bollinger_low_signal = signal_handler.create_signal(session, bollinger_low_indicator.id, close_price_indicator.value - bollinger_low_indicator.value)

    #macd histogram signal calculation
    if macd_histogram_signal:
        if macd_histogram_indicator.value < 0:
            signal_handler.delete_signal(session, macd_histogram_signal.id)
        elif macd_histogram_indicator.value > 0:
            macd_histogram_signal = signal_handler.update_signal(session, macd_histogram_signal.id, macd_histogram_indicator.value)
    else:
        if macd_histogram_indicator.value > 0:
            macd_histogram_signal = signal_handler.create_signal(session, macd_histogram_indicator.id, macd_histogram_indicator.value)

    #macd cross signal calculation
    if macd_signal:
        if macd_indicator.value > macd_signal_line_indicator.value:
            macd_signal = signal_handler.update_signal(session, macd_signal.id, macd_indicator.value - macd_signal_line_indicator.value)
        elif macd_indicator.value < macd_signal_line_indicator.value:
            signal_handler.delete_signal(session, macd_signal.id)
    else:
        if macd_indicator.value > macd_signal_line_indicator.value:
            macd_signal = signal_handler.create_signal(session, macd_indicator.id, macd_indicator.value - macd_signal_line_indicator.value)

    #rsi cross signal calculation
    if rsi6_signal:
        if rsi6_indicator.value > rsi12_indicator.value:
            rsi6_signal = signal_handler.update_signal(session, rsi6_signal.id, rsi6_indicator.value - rsi12_indicator.value)
        elif rsi6_indicator.value < rsi12_indicator.value:
            signal_handler.delete_signal(session, rsi6_signal.id)
    else:
        if rsi6_indicator.value > rsi12_indicator.value:
            rsi6_signal = signal_handler.create_signal(session, rsi6_indicator.id, rsi6_indicator.value - rsi12_indicator.value)

    return
