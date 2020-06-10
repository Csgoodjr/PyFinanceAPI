import os
import time
import finnhub
import requests
import datetime as dt
from finnhub import ApiException

configuration = finnhub.Configuration(
    api_key = {
        'token': 'brg4n17rh5rc8dj2rt20'
    }
)

# Market Class
# Provides insight into the market as a whole
# Finds Ticker Symbols
# Finds IPOs

class Market:

    def __init__(self):
        self.api = finnhub.DefaultApi(finnhub.ApiClient(configuration))

    def getIPO(self):
        try: 
            res = self.api.ipo_calendar("2020-03-15","2020-03-30")
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res

