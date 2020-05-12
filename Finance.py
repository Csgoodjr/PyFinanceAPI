import json
from urllib.request import urlopen

class Finance:

    def __init__(self):
        self._api = "https://financialmodelingprep.com/api/v3/"

    def loadData(self, endpoint):
        return json.loads(urlopen(endpoint).read().decode('utf-8'))
