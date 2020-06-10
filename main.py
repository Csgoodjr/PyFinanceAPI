import os
import json
import time
import math
import argparse
from Finance import Finance
from Market import Market

# Main Program Driver
# Takes in commandline arguments
if __name__ == "__main__":
    tickers = ['TSLA','AAPL','MSFT']
    stocks = [Finance(i) for i in tickers]
    for stock in stocks:
        print(stock.getActualEPSTrend())
        print(stock.getAvgActualEPS())
        print(stock.getEstimatedEPSTrend())
        print(stock.getAvgEstimatedEPS())