import webbrowser
from Finance import Finance

# Stock Sub Class
# Gets Ticker Profile
# Gets Quote Profile

class Stock(Finance):

    def __init__(self,ticker):
        Finance.__init__(self)
        self.ticker = ticker
        self.profile = self.loadData(self._api+'company/profile/'+ticker)
        self.quote = self.loadData(self._api+'quote/'+ticker)

    # Get the company profile
    def getProfile(self):
        return self.profile

    # Get an element from the profile
    def getProfileElement(self,elem):
        try:
            if elem == "symbol":
                return self.profile['symbol']
            else:
                return self.profile['profile'][elem]
        except:
            return "The element you are searching for could not be found!"

    # Launch the company's website in your browser
    def visitWebsite(self):
        webbrowser.open(self.profile['profile']['website'])

    # Print out the company profile information (pretty)
    def getProfilePretty(self):
        print(f"{self.profile['profile']['companyName']} ({self.profile['symbol']})")
        print(f"CEO:            {self.profile['profile']['ceo']}")
        print(f"Industry:       {self.profile['profile']['industry']}")
        print(f"Market Cap:     ${self.formatUSD(self.profile['profile']['mktCap'])}")
        print(f"Average Volume: {self.formatVal(self.profile['profile']['volAvg'])}")
        return 

    # Get the current quote
    def getQuote(self):
        return self.quote

    # Get an element from the quote
    def getQuoteElement(self,elem):
        try:
            return self.quote[elem]
        except:
            return "The element you are searching for could not be found!"
