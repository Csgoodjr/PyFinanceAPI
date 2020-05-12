from Finance import Finance

class Stock(Finance):

    def __init__(self,ticker):
        Finance.__init__(self)
        self.ticker = ticker

    def getProfile(self):
        endpoint = self._api + "profile/" + self.ticker
        return self.loadData(endpoint)

    def getQuote(self):
        endpoint = self._api + "quote/" + self.ticker
        return self.loadData(endpoint)
        

if __name__ == "__main__":
    aapl = Stock("AAPL")
    print(aapl.getQuote())
