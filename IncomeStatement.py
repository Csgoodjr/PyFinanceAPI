# Income Statement (FINNHUB API)
# This is an abstraction of the income statement that is gathered from the Finnhub API
# Creates a custom data tupe that allows the user to objectify data

# Utilizes the Adapter Pattern -- By creating a static Income Statement  class from API

# Object: IncomeStatement

class IncomeStatement:

    def __init__(self, ic):
        self.incomeStatement = {}
        for item in ic:
            self.incomeStatement[item['concept']] = item['value']
        self.__dict__ = self.incomeStatement
