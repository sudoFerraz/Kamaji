import csv
import datetime as dt
from pandas_datareader import data, wb
import stockstats
from stockstats import StockDataFrame
import pandas as pd
import unicodecsv

start_date = dt.datetime(1995, 1, 1)
dat = data.DataReader('USDBRL=X', 'yahoo')
dat.to_csv('brlusd.csv', mode='w', header=True)

with open('brlusd.csv', 'rb') as f:
	reader = unicodecsv.DictReader(f)
	forex_historical = list(reader)

adjusted_csv = []

for day in forex_historical:
	for k, item in day.items():
		if k == 'Volume':
			del day[k]
	adjusted_csv.append(day)

with open('adjusted_brlusd.csv', 'w') as csvfile:
	fieldnames = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for day in adjusted_csv:
		writer.writerow(day)



#usdbrl = StockDataFrame.retype(pd.read_csv('brlusd.csv'))
#usdbrl['macd']
