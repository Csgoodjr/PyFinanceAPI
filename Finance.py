import os
import time

# Import Financial API
from FinAPI import FinAPI
from finnhub.rest import ApiException

# Import Plotting
import matplotlib.pyplot as plt
import numpy

# Custom Object Imports
from Profile import Profile
from EPS import EPS
from Financials import Financials
from BalanceSheet import BalanceSheet
from IncomeStatement import IncomeStatement
from CashFlowStatement import CashFlowStatement

# Finance Base Class
class Finance:

    def __init__(self,ticker):
        self.api = FinAPI().getInstance()
        self.ticker = ticker
        self.eps = self.getEPS()
        self.profile = self.getProfile()
        self.financials = self.getAnnualFinancials()

    """ Formatting Methods """
    def formatVal(self,value):
        return format(float(value), ",.0f")

    def formatUSD(self,value):
        return format(float(value), ",.2f")

    # Returns the average of a list of values
    def listAverage(self,l) -> float:
        return sum(l)/len(l)

    """ Data Acquisition """
    # Returns a dictionary of the company profile
    def getProfile(self) -> Profile:
        try:
            res = Profile(self.api.company_profile2(symbol=self.ticker).to_dict())
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res

    # Returns a list of the 4 most recent quarters of EPS data
    def getEPS(self) -> list:
        try: 
            res = [EPS(mark.to_dict()) for mark in self.api.company_earnings(self.ticker)]
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return res

    # Returns a list of financial statements as objects
    # Overall Financials -> Balance Sheet, Income Statement, and Cash Flow Statement
    def getAnnualFinancials(self) -> list:
        try:
            fin = []
            res = self.api.financials_reported(symbol=self.ticker).to_dict()['data']
            for rep in res:
                fin.append(Financials(rep))
        except ApiException as e:
            print(f"Exception when calling DefaultAPI {e}")
        finally:
            return fin

    """ Analytics """
    # Creates an average of the actual EPS values
    def getAvgActualEPS(self) -> float:
        return self.listAverage(self.getActualEPSTrend())

    # Creates an average of the estimated EPS values
    def getAvgEstimatedEPS(self) -> float:
        return self.listAverage(self.getEstimatedEPSTrend())

    # Creates a list of the actual EPS values
    def getActualEPSTrend(self) -> list:
        return [e.actual for e in self.eps]

    def plotActualEPSTrend(self):
        trend = self.getEstimatedEPSTrend()
        self.plotTrend(range(0, len(trend)), trend, 'green',"Actual EPS Trend", "Recent Quarters", "Actual EPS")

    # Creates a list of the estimated EPS values
    def getEstimatedEPSTrend(self) -> list:
        return [e.estimate for e in self.eps]

    def plotEstimatedEPSTrend(self):
        trend = self.getEstimatedEPSTrend()
        self.plotTrend(range(0,len(trend)),trend,'orange',"Estimated EPS Trend","Recent Quarters","Estimated EPS")

    def plotTrend(self,x,y,color,title,xlabel,ylabel):
        plt.plot(x, y, '-ok', c=color)
        plt.title(f"{title} for {self.ticker}")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

# Test the Finance Object
if __name__ == "__main__":
    stock = Finance("AAPL")
    print("STOCK PROFILE:")
    print(stock.profile)
    print("EPS:")
    for eps in stock.eps:
        print(eps)
    print(f"Average Actual EPS: {stock.getAvgActualEPS()}")
    print(f"Average Estimated EPS: {stock.getAvgEstimatedEPS()}")
    print("FINANCIALS:")
    for fin in stock.getAnnualFinancials():
        print(fin)
    stock.plotEstimatedEPSTrend()
    stock.plotActualEPSTrend()
