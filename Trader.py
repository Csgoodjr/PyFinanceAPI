import time
import datetime
import calendar
import alpaca_trade_api as tradeapi

# Init the API
api = tradeapi.REST(
    "PKCIQ38U41GOZT0FRQYA",
    "n90ucKx/BbFEok4S/enLUT4PDIlIwizGO9qDz0Aw",
    "https://paper-api.alpaca.markets"
)

class Trader:

    def __init__(self):
        self.account = api.get_account()

    def getCurrentBuyingPower(self):
        return float(self.account.buying_power)

    def submitMarketOrder(self,symbol,qty,orderType="buy",timeInForce='est'):
        if self.getCurrentBuyingPower() < 0:
            return "Negative Account Balance Warning!"
        api.submit_order(symbol=symbol, qty=qty, side=orderType, type='market', time_in_force=timeInForce)

    def submitLimitOrder(self,symbol,qty,orderType="buy",limitPrice=0,timeInForce='est'):
        if self.getCurrentBuyingPower() < 0:
            return "Negative Account Balance Warning!"
        api.submit_order(symbol=symbol, qty=qty, side=orderType, type='limit', time_in_force=timeInForce,limit_price=limitPrice)

    
# Get instance of account
account = api.get_account()

# Make sure trading isn't blocked
if account.trading_blocked:
    print("Restricted from trading")

# Get buying power
print(f'{account.buying_power} is available as buying power')

def submitMarketOrder(symbol,quantity,orderType="buy"):
    if float(account.buying_power) < 0:
        return "You don't have enough buying power!"
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side=orderType,
        type='market',
        time_in_force='gtc'
    )
    return f"Your purchase of {quantity} shares in {symbol} was successful!"

def submitLimitOrder(symbol,quantity,limitPrice,orderType="buy"):
    if float(account.buying_power) < 0:
        return "You don't have enough buying power!"
    api.submit_order(
        symbol=symbol,
        qty=quantity,
        side=orderType,
        type='limit',
        time_in_force='gtc',
        limit_price=limitPrice
    )
    return f"Your purchase of {quantity} shares at ${limitPrice} in {symbol} was successful!"

if __name__ == "__main__":
    #print(submitMarketOrder("AAPL",5))
    assets = api.list_assets(status='active')
    nasdaq = [a for a in assets if (a.exchange == 'NASDAQ' and a.tradable)]
    nyse = [a for a in assets if (a.exchange == 'NYSE' and a.tradable)]
    print(f"Number of NASDAQ Assets: {len(nasdaq)}")
    print(f"Number of NYSE Assets: {len(nyse)}")
    aapl = api.get_barset('AAPL','day',limit=1)
    print(aapl['AAPL'][0].t)
