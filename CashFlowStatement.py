# Cash Flow Statement (FINNHUB API)
# This is an abstraction of the cash flow statement that is gathered from the Finnhub API
# Creates a custom data tupe that allows the user to objectify data

# Utilizes the Adapter Pattern -- By creating a static Cash Flow Statement class from API

# Object: CashFlowStatement


class CashFlowStatement:

    def __init__(self, cf):
        self.cashFlow = {}
        for item in cf:
            self.cashFlow[item['concept']] = item['value']
        self.__dict__ = self.cashFlow
