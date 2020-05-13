from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.tools import yahoofinance

#yahoofinance.download_daily_bars('orcl', 2000, 'orcl-2000.csv')



class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(MyStrategy, self).__init__(feed)
        self.__instrument = instrument

    def onBars(self, bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())

# Load the yahoo feed from the CSV file
feed = yahoofeed.Feed()
feed.addBarsFromCSV("brlusd", "brlusd.csv")

# Evaluate the strategy with the feed's bars.
myStrategy = MyStrategy(feed, "brlusd")
myStrategy.run()