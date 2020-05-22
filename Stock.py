from Finance import Finance

# Stock Sub Class
# Gets Ticker Profile
# Gets Quote Profile

class Stock(Finance):

    # Init the Stock Object
    # Sends the api request for the profile and quote of the ticker
    def __init__(self,ticker):
        Finance.__init__(self,ticker)
        self.data = self.loadData('company/profile/')
        self.quote = self.loadData('quote/')[0]
        self.profile = self.data['profile']
        self.symbol = self.data['symbol']

    # Get the company profile
    def getProfile(self):
        return self.profile

    # Get an element from the profile
    def getProfileElement(self, elem):
        try:
            return self.profile[elem]
        except:
            return "The element you are searching for could not be found!"

    # Get the current quote
    def getQuote(self):
        return self.quote

    # Get an element from the quote
    def getQuoteElement(self, elem):
        try:
            return self.quote[elem]
        except:
            return "The element you are searching for could not be found!"

    # Get the current stock price
    def getCurrentPrice(self):
        return self.quote['price']

    # Get the latest dividends
    def getDividends(self):
        return self.profile['lastDiv']

    # Get the current marketcap
    def getMarketCap(self):
        return self.quote['marketCap']

    # Get the current stock volume
    def getVolume(self):
        return self.quote['volume']

    # Get the average stock volume
    def getAverageVolume(self):
        return self.quote['avgVolume']

    # Get the daily low stock price
    def getDailyLow(self):
        return self.quote['dayLow']

    # Get the daily high stock price
    def getDailyHigh(self):
        return self.quote['dayHigh']

    # Get the current day's stock price change (points)
    def getChanges(self):
        return self.quote['changes']

    # Get the current day's stock price change (percent)
    def getChangePercent(self):
        return self.quote['changesPercentage']

    # Get the yearly low stock price
    def getYearlyLow(self):
        return self.quote['yearLow']

    # Get the yearly high stock price
    def getYearlyHigh(self):
        return self.quote['yearHigh']

    # Get the company's name
    def getCompanyName(self):
        return self.profile['companyName']

    # Get the exchange that the stock is traded on
    def getExchange(self):
        return self.profile['exchange']

    # Get the stock symbol
    def getTicker(self):
        return self.symbol

    # Print out the company profile information (pretty)
    def getBriefing(self):
        print(f"{self.profile['companyName']} ({self.symbol})")
        print(f"CEO:            {self.profile['ceo']}")
        print(f"Industry:       {self.profile['industry']}")
        print(f"Market Cap:     ${self.formatUSD(self.profile['mktCap'])}")
        print(f"Average Volume: {self.formatVal(self.profile['volAvg'])}")
        return 