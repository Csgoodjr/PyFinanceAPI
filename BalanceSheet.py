# Balance Sheet (FINNHUB API)
# This is an abstraction of the balance sheet that is gathered from the Finnhub API
# Creates a custom data tupe that allows the user to objectify data

# Utilizes the Adapter Pattern -- By creating a static Balance Sheet class from API

# Object: BalanceSheet
#   MarketableSecuritiesCurrent
#   AccountsReceivableNetCurrent
#   InventoryNet
#   NontradeReceivablesCurrent
#   OtherAssetsCurrent
#   AssetsCurrent
#   MarketableSecuritiesNoncurrent
#   PropertyPlantAndEquipmentNet
#   OtherAssetsNoncurrent
#   AssetsNoncurrent
#   Assets
#   AccountsPayableCurrent
#   OtherLiabilitiesCurrent
#   ContractWithCustomerLiabilityCurrent
#   CommercialPaper
#   LongTermDebtCurrent
#   LiabilitiesCurrent
#   LongTermDebtNoncurrent
#   OtherLiabilitiesNoncurrent
#   LiabilitiesNoncurrent
#   Liabilities
#   CommitmentsAndContingencies **
#   CommonStocksIncludingAdditionalPaidInCapital
#   RetainedEarningsAccumulatedDeficit
#   AccumulatedOtherComprehensiveIncomeLossNetOfTax
#   StockholdersEquity
#   LiabilitiesAndStockholdersEquity

class BalanceSheet:

    def __init__(self,bs):
        self.balanceSheet = {}
        for item in bs:
            self.balanceSheet[item['concept']] = item['value']
        self.__dict__ = self.balanceSheet

    def formatUSD(self, value):
        return format(float(value), ",.2f")

    def __str__(self):
        return f"""
        Current Marketable Securities: ${self.formatUSD(self.MarketableSecuritiesCurrent)}
        Current New Accounts Receivable: ${self.formatUSD(self.AccountsReceivableNetCurrent)}
        Net Inventory: ${self.formatUSD(self.InventoryNet)}
        Current Non-trade Receivables: ${self.formatUSD(self.NontradeReceivablesCurrent)}
        Other Current Assets: ${self.formatUSD(self.OtherAssetsCurrent)}
        Total Current Assets: ${self.formatUSD(self.AssetsCurrent)}
        Marketable Securities: ${self.formatUSD(self.MarketableSecuritiesNoncurrent)}
        Net Property Plant and Equipment(PP&E): ${self.formatUSD(self.PropertyPlantAndEquipmentNet)}
        Other Noncurrent Assets: ${self.formatUSD(self.OtherAssetsNoncurrent)}
        Total Noncurrent Assets: ${self.formatUSD(self.AssetsNoncurrent)}
        Total Assets: ${self.formatUSD(self.Assets)}
        Current Accounts Payable: ${self.formatUSD(self.AccountsPayableCurrent)}
        Other Current Liabilities: ${self.formatUSD(self.OtherLiabilitiesCurrent)}
        Current Contracts with Customers: ${self.formatUSD(self.ContractWithCustomerLiabilityCurrent)}
        Commercial Paper: ${self.formatUSD(self.CommercialPaper)}
        Current Long Term Debt: ${self.formatUSD(self.LongTermDebtCurrent)}
        Total Current Liabilities: ${self.formatUSD(self.LiabilitiesCurrent)}
        Noncurrent Long Term Debt: ${self.formatUSD(self.LongTermDebtNoncurrent)}
        Other Noncurrent Liabilities: ${self.formatUSD(self.OtherLiabilitiesNoncurrent)}
        Total Noncurrent Liabilities: ${self.formatUSD(self.LiabilitiesNoncurrent)}
        Total Liabilities: ${self.formatUSD(self.Liabilities)}
        Common Stock: ${self.formatUSD(self.CommonStocksIncludingAdditionalPaidInCapital)}
        Retained Earnings: ${self.formatUSD(self.RetainedEarningsAccumulatedDeficit)}
        Other Accumulated Comprehensive Income: ${self.formatUSD(self.AccumulatedOtherComprehensiveIncomeLossNetOfTax)}
        Stakeholders' Equity: ${self.formatUSD(self.StockholdersEquity)}
        Total Liabilities and Stakeholders' Equity: ${self.formatUSD(self.LiabilitiesAndStockholdersEquity)}
        """

    def getMarketableSecuritiesCurrent():
        return self.MarketableSecuritiesCurrent

    def getAccountsReceivableNetCurrent():
        return self.AccountsReceivableNetCurrent

    def getInventoryNet():
        return self.InventoryNet

    def getNontradeReceivablesCurrent():
        return self.NontradeReceivablesCurrent

    def getOtherAssetsCurrent():
        return self.OtherAssetsCurrent

    def getAssetsCurrent():
        return self.AssetsCurrent

    def getMarketableSecuritiesNoncurrent():
        return self.MarketableSecuritiesNoncurrent

    def getPropertyPlantAndEquipmentNet():
        return self.PropertyPlantAndEquipmentNet

    def getOtherAssetsNoncurrent():
        return self.OtherAssetsNoncurrent

    def getAssetsNoncurrent():
        return self.AssetsNoncurrent

    def getAssets():
        return self.Assets

    def getAccountsPayableCurrent():
        return self.AccountsPayableCurrent

    def getOtherLiabilitiesCurrent():
        return self.OtherLiabilitiesCurrent

    def getContractWithCustomerLiabilityCurrent():
        return self.ContractWithCustomerLiabilityCurrent

    def getCommercialPaper():
        return self.CommercialPaper

    def getLongTermDebtCurrent():
        return self.LongTermDebtCurrent

    def getLiabilitiesCurrent():
        return self.LiabilitiesCurrent

    def getLongTermDebtNoncurrent():
        return self.LongTermDebtNoncurrent

    def getOtherLiabilitiesNoncurrent():
        return self.OtherLiabilitiesNoncurrent

    def getLiabilitiesNoncurrent():
        return self.LiabilitiesNoncurrent

    def getLiabilities():
        return self.Liabilities

    def getCommitmentsAndContingencies():
        return self.CommitmentsAndContingencies

    def getCommonStocksIncludingAdditionalPaidInCapital():
        return self.CommonStocksIncludingAdditionalPaidInCapital

    def getRetainedEarningsAccumulatedDeficit():
        return self.RetainedEarningsAccumulatedDeficit

    def getAccumulatedOtherComprehensiveIncomeLossNetOfTax():
        return self.AccumulatedOtherComprehensiveIncomeLossNetOfTax

    def getStockholdersEquity():
        return self.StockholdersEquity

    def getLiabilitiesAndStockholdersEquity():
        return self.LiabilitiesAndStockholdersEquity
