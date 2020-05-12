import argparse
from Finance import Finance
from Stock import Stock
from Statements import Statements
from Ratios import Ratios

# Main Program Driver
# Takes in commandline arguments
if __name__ == "__main__":
    tickers = ['TSLA','AAPL','MSFT','SAP']
    stocks = [Stock(i) for i in tickers]
    for stock in stocks:
        stock.getProfilePretty()

    print(stocks[0].getProfileElement("website"))
    stocks[0].visitWebsite()