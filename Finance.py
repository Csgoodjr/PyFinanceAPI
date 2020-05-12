import json
import requests
from urllib.request import urlopen

# Finance Base Class
# Handles the core API Link
# Handles loading data 

class Finance:

    def __init__(self):
        self._api = "https://financialmodelingprep.com/api/v3/"


    def formatVal(self,value):
        return format(float(value), ",.0f")

    def formatUSD(self,value):
        return format(float(value), ",.2f")

    # Loads data from the given endpoint
    # Handles improper endpoints
    # Return JSON
    def loadData(self, endpoint):
        try:
            return json.loads(urlopen(endpoint).read().decode('utf-8'))
        except:
            return "There was an error trying to load your information!"
