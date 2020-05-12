from Finance import Finance

# Statements Sub Class
# Gets Income Statements
# Gets Balance Sheets
# Gets Cash Flow Statements
class Statements(Finance):

    def __init__(self,ticker):
        Finance.__init__(self)
        self.ticker = ticker

    # Ticker/Company Identifier Getter
    def getTicker(self):
        return self.ticker

    # Ticker/Company Identifier Setter
    def setTicker(self,ticker):
        self.ticker = ticker

    # Income Statement 
    def getIncomeStatement(self):
        endpoint = self._api + "income-statement/" + self.ticker
        return self.loadData(endpoint)

    # Income Statement by Quarter
    def getIncomeStatementByQuarter(self,quarter):
        endpoint = self._api + "income-statement/" + self.ticker + "?period=" + quarter
        return self.loadData(endpoint)

    # Balance Sheet
    def getBalanceSheet(self):
        endpoint = self._api + "balance-sheet-statement/" + self.ticker
        return self.loadData(endpoint)

    # Balance Sheet by Quarter
    def getBalanceSheetByQuarter(self,quarter):
        endpoint = self._api + "balance-sheet-statement/" + self.ticker + "?period=" + quarter
        return self.loadData(endpoint)

    # Cash Flow Statement
    def getCashFlowStatement(self):
        endpoint = self._api + "cash-flow-statement/" + self.ticker
        return self.loadData(endpoint)

    # Cash Flow Statement by Quarter
    def getCashFlowStatementByQuarter(self,quarter):
        endpoint = self._api + "cash-flow-statement/" + self.ticker + "?period=" + quarter
        return self.loadData(endpoint)

