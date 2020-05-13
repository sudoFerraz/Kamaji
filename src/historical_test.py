import datetime as dt
from pandas_datareader import data, wb

start_date = dt.datetime(1980, 1, 1)
dat = data.DataReader('googl', 'yahoo', start_date, dt.datetime.today())
dat.to_csv('googl.csv', mode='w', header=True)