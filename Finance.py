import os
import json
import requests
from urllib.request import urlopen

# Finance Base Class
# Handles the core API Link
# Handles loading data 

class Finance:

    def __init__(self,ticker):
        self._api = "https://financialmodelingprep.com/api/v3/"
        self._apiKey = os.environ.get("APIKEY")
        self._ticker = ticker

    def formatVal(self,value):
        return format(float(value), ",.0f")

    def formatUSD(self,value):
        return format(float(value), ",.2f")

    # Loads data from the given endpoint
    # Handles improper endpoints
    # Return JSON
    def loadData(self, endpoint):
        endpoint = self._api + endpoint + self._ticker + "?apikey="+self._apiKey
        try:
            return json.loads(urlopen(endpoint).read().decode('utf-8'))
        except:
            return "There was an error trying to load your information!"
