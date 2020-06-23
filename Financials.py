# Financials (FINNHUB API)
# This is an abstraction of the Financials that are gathered form the Finnhub API
# Creates a custom data type that allows the user to objectify data

# Utilizes the Adapter Pattern and Builder Patter 
# - By creating a static Financials class from the API
# - By creating a Balance Sheet, Income Statement, and Cash Flow Statement

from BalanceSheet import BalanceSheet
from IncomeStatement import IncomeStatement
from CashFlowStatement import CashFlowStatement

# Object: Financials

class Financials:

    def __init__(self,fin):
        self.__dict__ = fin
        self.balanceSheet = BalanceSheet(self.report['bs'])
        self.incomeStatement = IncomeStatement(self.report['ic'])
        self.cashFlowStatement = CashFlowStatement(self.report['cf'])

    def __str__(self):
        return f"""
        Financial Statements for {self.symbol}
        CIK: {self.cik}
        Year: {self.year}
        Quarter: {self.quarter}
        Form: {self.form}
        Period: {self.startDate} - {self.endDate}
        Date Filed: {self.filedDate}
        """