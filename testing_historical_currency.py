import datetime as dt
from pandas_datareader import data, wb

start_date = dt.datetime(1994, 1, 1)
dat = data.DataReader('usd', 'yahoo', start_date, dt.datetime.today())
dat.to_csv('usdbrl.csv', mode='w', header=True)
