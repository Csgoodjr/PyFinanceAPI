from Finance import Finance
from urllib.request import urlopen

class Statements(Finance):

    def __init__(self,ticker):
        Finance.__init__(self)
        self.ticker = ticker

    def getTicker(self):
        return self.ticker

    def setTicker(self,ticker):
        self.ticker = ticker

    def getIncomeStatement(self):
        endpoint = self._api + "income-statement/" + self.ticker
        return self.loadData(endpoint)

    def getIncomeStatementByQuarter(self,quarter):
        endpoint = self._api + "income-statement/" + self.ticker + "?period=" + quarter
        return self.loadData(endpoint)

    def getBalanceSheet(self):
        endpoint = self._api + "balance-sheet-statement/" + self.ticker
        return self.loadData(endpoint)

    def getBalanceSheetByQuarter(self,quarter):
        endpoint = self._api + "balance-sheet-statement/" + self.ticker + "?period=" + quarter
        return self.loadData(endpoint)

    def getCashFlowStatement(self):
        endpoint = self._api + "cash-flow-statement/" + self.ticker
        return self.loadData(endpoint)

    def getCashFlowStatementByQuarter(self,quarter):
        endpoint = self._api + "cash-flow-statement/" + self.ticker + "?period=" + quarter
        return self.loadData(endpoint)

