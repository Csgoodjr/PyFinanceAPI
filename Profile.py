# Profile (FINNHUB API)
# This is an abstraction of the profile that is gathered from the Finnhub API
# Creates a custom data type that allows the user to objectify data

# Utilizes the Adapter Pattern -- By creating a static Profile class from any API

# Object: Profile
#   country
#   currency
#   exchange
#   name
#   ipo
#   market_capitalization
#   share_outstanding
#   logo   
#   phone
#   finnhub_industry

class Profile:

    # Init the Profile with a Ticker Symbol (Defaulted to AAPL)
    def __init__(self,profile):
        self.__dict__ = profile

    # Prints the Profile in a readable format
    def __str__(self):
        return f"""
        Company Profile for {self.name}
        Country: {self.country}
        Currency: {self.currency}
        Exchange: {self.exchange}
        IPO: {self.ipo}
        MKTCP: {self.market_capitalization}
        Outstanding Shares: {self.share_outstanding}
        Industry: {self.finnhub_industry}
        """

    # Profile Getters
    def getCountry(self):
        return self.country

    def getCurrency(self):
        return self.currency

    def getExchange(self):
        return self.exchange

    def getName(self):
        return self.name

    def getIPO(self):
        return self.ipo

    def getMarketCap(self):
        return self.market_capitalization

    def getOutstandingShares(self):
        return self.share_outstanding

    def getLogo(self):
        return self.logo

    def getPhone(self):
        return self.phone

    def getIndustry(self):
        return self.finnhub_industry

