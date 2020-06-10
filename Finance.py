import os
import time
import finnhub
from finnhub.rest import ApiException

configuration = finnhub.Configuration(
    api_key = {
        'token': 'brg4n17rh5rc8dj2rt20'
    }
)

# Finance Base Class
# Handles the core API Link
# Handles loading data 

class Finance:

    def __init__(self,ticker):
        self.api = finnhub.DefaultApi(finnhub.ApiClient(configuration))
        self.ticker = ticker
        self.eps = self.getEPS()
        self.profile = self.getProfile()

    def formatVal(self,value):
        return format(float(value), ",.0f")

    def formatUSD(self,value):
        return format(float(value), ",.2f")

    # Returns a list of elements from a list of dictionaries
    def listify(self,d,elem) -> list:
        l = []
        for e in d:
            l.append(e.to_dict()[elem])
        return l

    # Returns the average of a list of values
    def listAverage(self,l) -> float:
        return sum(l)/len(l)

    # Returns a dictionary of the company profile
    def getProfile(self) -> dict:
        try:
            res = self.api.company_profile2(symbol=self.ticker).to_dict()
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res

    # Returns a dict of the basic financial information based upon a metric
    # Metric can be of the value: "all","price","valuation" -> Default is "all"
    def getBasicFinancials(self,metric="all") -> dict:
        try: 
            res = self.api.company_basic_financials(self.ticker, metric).to_dict()
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res

    # Returns a list of the 4 most recent quarters of EPS data
    def getEPS(self) -> list:
        try: 
            res = self.api.company_earnings(self.ticker)
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res

    # Creates an average of the actual EPS values
    def getAvgActualEPS(self) -> float:
        eps_trend = self.listify(self.eps,'actual')
        return self.listAverage(eps_trend)

    # Creates an average of the estimated EPS values
    def getAvgEstimatedEPS(self) -> float:
        eps_trend = self.listify(self.eps,'estimate')
        return self.listAverage(eps_trend)

    # Creates a list of the actual EPS values
    def getActualEPSTrend(self) -> list:
        return self.listify(self.eps,'actual')

    # Creates a list of the estimated EPS values
    def getEstimatedEPSTrend(self) -> list:
        return self.listify(self.eps,'estimate')

    # Returns the recommended trends for this stock
    def getTrends(self) -> list:
        try:
            res = self.api.recommendation_trends(self.ticker)
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res


