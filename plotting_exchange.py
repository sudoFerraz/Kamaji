import unicodecsv
import matplotlib.pyplot as plt

with open('brlusd.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    forex_historical = list(reader)

daily_price = []


for day in forex_historical:
    daily_price.append(day['Adj Close'])

print daily_price

plt.hist(daily_price)
