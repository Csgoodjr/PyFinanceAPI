# EPS (FINNHUB API)
# This is an abstraction of the EPS that is gathered from the Finnhub API
# Creates a custom data type that allows user to objectify data

# Utilizes the Adapter Pattern -- By creating a static EPS class from any API

# Define level of certainty
CERTAINTY = 4

# Object: EPS
#   actual
#   estimate
#   period
#   symbol

class EPS:

    def __init__(self,eps):
        self.__dict__ = eps

    def __str__(self):
        return f"""
        Company EPS for {self.symbol} for {self.period}
        Actual: {round(self.actual,CERTAINTY)}
        Estimate: {round(self.estimate,CERTAINTY)}
        Difference: {round(self.actual-self.estimate,CERTAINTY)}
        """

    # EPS Getters
    def getActual(self):
        return round(self.actual, CERTAINTY)

    def getEstimate(self):
        return round(self.estimate, CERTAINTY)

    def getPeriod(self):
        return self.period

    def getDifference(self):
        return round(self.actual-self.period, CERTAINTY)

    def getSymbol(self):
        return self.symbol
