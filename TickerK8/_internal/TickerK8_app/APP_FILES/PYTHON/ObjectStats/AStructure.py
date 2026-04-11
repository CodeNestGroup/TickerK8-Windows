#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class ObjectStatsS(QScrollArea): 
    def __init__(self, parent, s, t, i):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language
        if t == 'country':
                self.Country()
        elif t == 'market':
                self.Market()
        elif t == 'stock':
                self.Stock()

    def Country(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
#           --- Macroeconomic data ---
        self.MacroeconomicDataTitlel = QLabel(self.WidgetW)
        self.GDPUsdNameL = QLabel(self.WidgetW)
        self.GDPUsdValueL = QLabel(self.WidgetW)
        self.GDPCountryCurrencyNameL = QLabel(self.WidgetW)
        self.GDPCountryCurrencyValueL = QLabel(self.WidgetW)
        self.GDPPerCapitaUsdNameL = QLabel(self.WidgetW)
        self.GDPPerCapitaUsdValueL = QLabel(self.WidgetW)
        self.GDPPerCapitaCountryCurrencyNameL = QLabel(self.WidgetW)
        self.GDPPerCapitaCountryCurrencyValueL = QLabel(self.WidgetW)
        self.InflationCpiNameL = QLabel(self.WidgetW)
        self.InflationCpiValueL = QLabel(self.WidgetW)
        self.IntrestRateNameL = QLabel(self.WidgetW)
        self.IntrestRateValueL = QLabel(self.WidgetW)
        self.UnemploymentRateNameL = QLabel(self.WidgetW)
        self.UnemploymentRateValueL = QLabel(self.WidgetW)
        self.PublicDebtGdpRatioNameL = QLabel(self.WidgetW)
        self.PublicDebtGdpRatioValueL = QLabel(self.WidgetW)
        self.PopulationNameL = QLabel(self.WidgetW)
        self.PopulationValueL = QLabel(self.WidgetW)
#           --- Call functions ---
        CountryUi(self)
        CountryReloadStyle(self)
        CountryRetranslate(self)
#           --- Connect functions ---

    def Market(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
#           --- Market statistics
        self.MarketStatisticsTitleL = QLabel(self.WidgetW)
        self.ListedCompaniesMainNameL = QLabel(self.WidgetW)
        self.ListedCompaniesMainValueL = QLabel(self.WidgetW)
        self.ListedCompaniesSecondaryNameL = QLabel(self.WidgetW)
        self.ListedCompaniesSecondaryValueL = QLabel(self.WidgetW)
        self.TotalListedNameL = QLabel(self.WidgetW)
        self.TotalListedValueL = QLabel(self.WidgetW)
        self.DailyTradingVolNameL = QLabel(self.WidgetW)
        self.DailyTradingVolValueL = QLabel(self.WidgetW)
        self.DailyTradingValNameL = QLabel(self.WidgetW)
        self.DailyTradingValValueL = QLabel(self.WidgetW)
        self.DailyTransactionCountNameL = QLabel(self.WidgetW)
        self.DailyTransactionCountValueL = QLabel(self.WidgetW)
#            --- Sector trading data ---
        self.SectorTradingDataTitleL = QLabel(self.WidgetW)
        self.FinancialSectorVolNameL = QLabel(self.WidgetW)
        self.FinancialSectorVolValueL = QLabel(self.WidgetW)
        self.TechnologySectorVolNameL = QLabel(self.WidgetW)
        self.TechnologySectorVolValueL = QLabel(self.WidgetW)
        self.EnergySectorVolNameL = QLabel(self.WidgetW)
        self.EnergySectorVolValueL = QLabel(self.WidgetW)
        self.IndustrialSectorVolNameL = QLabel(self.WidgetW)
        self.IndustrialSectorVolValueL = QLabel(self.WidgetW)
        self.ConsumerSectorVolNameL = QLabel(self.WidgetW)
        self.ConsumerSectorVolValueL = QLabel(self.WidgetW)
#           --- Call functions ---
        MarketUi(self)
        MarketReloadStyle(self)
        MarketRetranslate(self)
#           --- Connect functions ---

    def Stock(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
#           --- Fundamental Data ---
        self.FundamentalDataTitleL = QLabel(self.WidgetW)
        self.IndicatorsSubTitleL = QLabel(self.WidgetW)
        self.MarketCapNameL = QLabel(self.WidgetW)
        self.MarketCapValueL = QLabel(self.WidgetW)
        self.PENameL = QLabel(self.WidgetW)
        self.PEValueL = QLabel(self.WidgetW)
        self.ForwardPENameL = QLabel(self.WidgetW)
        self.ForwardPEValueL = QLabel(self.WidgetW)
        self.PEGNameL = QLabel(self.WidgetW)
        self.PEGValueL = QLabel(self.WidgetW)
        self.PBNameL = QLabel(self.WidgetW)
        self.PBValueL = QLabel(self.WidgetW)
        self.PSNameL = QLabel(self.WidgetW)
        self.PSValueL = QLabel(self.WidgetW)
#           --- Profitability --- 
        self.ProfitabilitySubTitleL = QLabel(self.WidgetW)
        self.ROENameL = QLabel(self.WidgetW)
        self.ROEValueL = QLabel(self.WidgetW)
        self.ROANameL = QLabel(self.WidgetW)
        self.ROAValueL = QLabel(self.WidgetW)
        self.ROINameL = QLabel(self.WidgetW)
        self.ROIValueL = QLabel(self.WidgetW)
        self.NetMarginNameL = QLabel(self.WidgetW)
        self.NetMarginValueL = QLabel(self.WidgetW)
        self.OperatingMarginNameL = QLabel(self.WidgetW)
        self.OperatingMarginValueL = QLabel(self.WidgetW)
        self.GrossMarginNameL = QLabel(self.WidgetW)
        self.GrossMarginValueL = QLabel(self.WidgetW)
#           --- Balance --- 
        self.BalanceSubTitleL = QLabel(self.WidgetW)
        self.AssetsNameL = QLabel(self.WidgetW)
        self.AssetsValueL = QLabel(self.WidgetW)
        self.LiabilitiesNameL = QLabel(self.WidgetW)
        self.LiabilitiesValueL = QLabel(self.WidgetW)
        self.EquityNameL = QLabel(self.WidgetW)
        self.EquityValueL = QLabel(self.WidgetW)
        self.CashNameL = QLabel(self.WidgetW)
        self.CashValueL = QLabel(self.WidgetW)
        self.DebtNameL = QLabel(self.WidgetW)
        self.DebtValueL = QLabel(self.WidgetW)
#           --- Financial Reports ---
        self.FinancialReportsTitleL = QLabel(self.WidgetW)
        self.IncomeStatementSubTitleL = QLabel(self.WidgetW)
        self.RevenueNameL = QLabel(self.WidgetW)
        self.RevenueValueL = QLabel(self.WidgetW)
        self.GrossProfitNameL = QLabel(self.WidgetW)
        self.GrossProfitValueL = QLabel(self.WidgetW)
        self.OperatingIncomeNameL = QLabel(self.WidgetW)
        self.OperatingIncomeValueL = QLabel(self.WidgetW)
        self.NetIncomeNameL = QLabel(self.WidgetW)
        self.NetIncomeValueL = QLabel(self.WidgetW)
        self.EPSIncomeNameL = QLabel(self.WidgetW)
        self.EPSIncomeValueL = QLabel(self.WidgetW)
#           --- Balance Sheet ---
        self.BalanceSheetSubTitleL = QLabel(self.WidgetW)
        self.TotalAssetsNameL = QLabel(self.WidgetW)
        self.TotalAssetsValueL = QLabel(self.WidgetW)
        self.TotalLiabilitiesNameL = QLabel(self.WidgetW)
        self.TotalLiabilitiesValueL = QLabel(self.WidgetW)
        self.ShareholderEqulityNameL = QLabel(self.WidgetW)
        self.ShareholderEqulityValueL = QLabel(self.WidgetW)
#           --- Cash Flow --- 
        self.CashFlowSubTitleL = QLabel(self.WidgetW)
        self.OperatingCashFlowNameL = QLabel(self.WidgetW)
        self.OperatingCashFlowValueL = QLabel(self.WidgetW)
        self.InvestingCashFlowNameL = QLabel(self.WidgetW)
        self.InvestingCashFlowValueL = QLabel(self.WidgetW)
        self.FinancingCashFlowNameL = QLabel(self.WidgetW)
        self.FinancingCashFlowValueL = QLabel(self.WidgetW)
        self.FreeCashFlowNameL = QLabel(self.WidgetW)
        self.FreeCashFlowValueL = QLabel(self.WidgetW)
#           --- Dividend Data ---
        self.DividendDataSubTitleL = QLabel(self.WidgetW)
        self.DividendYieldNameL = QLabel(self.WidgetW)
        self.DividendYieldValueL = QLabel(self.WidgetW)
        self.DividendPerShareNameL = QLabel(self.WidgetW)
        self.DividendPerShareValueL = QLabel(self.WidgetW)
        self.PayoutRatioNameL = QLabel(self.WidgetW)
        self.PayoutRatioValueL = QLabel(self.WidgetW)
        self.DividendHistoryNameL = QLabel(self.WidgetW)
        self.DividendHistoryValueL = QLabel(self.WidgetW)
        self.ExDividendNameL = QLabel(self.WidgetW)
        self.ExDividendValueL = QLabel(self.WidgetW)
        self.PaymentDateNameL = QLabel(self.WidgetW)
        self.PaymentDateValueL = QLabel(self.WidgetW)
#           --- Corporation Data ---
        self.CorporationDataTitleL = QLabel(self.WidgetW)
        self.CorporateActionsSubTitleL = QLabel(self.WidgetW)
        self.StockSplitNameL = QLabel(self.WidgetW)
        self.StockSplitValueL = QLabel(self.WidgetW)
        self.ReverseSplitNameL = QLabel(self.WidgetW)
        self.ReverseSplitValueL = QLabel(self.WidgetW)
        self.MergersNameL = QLabel(self.WidgetW)
        self.MergersValueL = QLabel(self.WidgetW)
        self.AcquisitionsNameL = QLabel(self.WidgetW)
        self.AcquisitionsValueL = QLabel(self.WidgetW)
        self.BuyBacksNameL = QLabel(self.WidgetW)
        self.BuyBacksValueL = QLabel(self.WidgetW)
#           --- Events ---
        self.EventsSubTitleL = QLabel(self.WidgetW)
        self.EarningsDateNameL = QLabel(self.WidgetW)
        self.EarningsDateValueL = QLabel(self.WidgetW)
        self.AGMNameL = QLabel(self.WidgetW)
        self.AGMValueL = QLabel(self.WidgetW)
        self.InvestorDayNameL = QLabel(self.WidgetW)
        self.InvestorDayValueL = QLabel(self.WidgetW)
#           --- Ownership Data ---
        self.OwnershipDataTitleL = QLabel(self.WidgetW)
        self.ShareholdingSubTitleL = QLabel(self.WidgetW)
        self.InstitutionalOwnershipNameL = QLabel(self.WidgetW)
        self.InstitutionalOwnershipValueL = QLabel(self.WidgetW)
        self.InsiderOwnershipNameL = QLabel(self.WidgetW)
        self.InsiderOwnershipValueL = QLabel(self.WidgetW)
        self.TopShareholdersNameL = QLabel(self.WidgetW)
        self.TopShareholdersValueL = QLabel(self.WidgetW)
#           --- Insider Trading ---
        self.InsiderTradingSubTitleL = QLabel(self.WidgetW)
        self.InsiderBuysNameL = QLabel(self.WidgetW)
        self.InsiderBuysValueL = QLabel(self.WidgetW)
        self.InsiderSellsNameL = QLabel(self.WidgetW)
        self.InsiderSellsValueL = QLabel(self.WidgetW)
#           --- Analitical Data ---
        self.AnaliticalDataTitleL = QLabel(self.WidgetW)
        self.MovingAveragesNameL = QLabel(self.WidgetW)
        self.MovingAveragesValueL = QLabel(self.WidgetW)
        self.RSINameL = QLabel(self.WidgetW)
        self.RSIValueL = QLabel(self.WidgetW)
        self.MACDNameL = QLabel(self.WidgetW)
        self.MACDValueL = QLabel(self.WidgetW)
        self.BollingerBandsNameL = QLabel(self.WidgetW)
        self.BollingerBandsValueL = QLabel(self.WidgetW)
        self.MomentumNameL = QLabel(self.WidgetW)
        self.MomentumValueL = QLabel(self.WidgetW)
        self.VolatillityNameL = QLabel(self.WidgetW)
        self.VolatillityValueL = QLabel(self.WidgetW)
#           --- ESG Data ---
        self.ESGDataTitleL = QLabel(self.WidgetW)
        self.ESGScoreNameL = QLabel(self.WidgetW)
        self.ESGScoreValueL = QLabel(self.WidgetW)
        self.EnvironmentalScoreNameL = QLabel(self.WidgetW)
        self.EnvironmentalScoreValueL = QLabel(self.WidgetW)
        self.GovernanceScoreNameL = QLabel(self.WidgetW)
        self.GovernanceScoreValueL = QLabel(self.WidgetW)
#           --- Call functions ---
        StockUi(self)
        StockReloadStyle(self)
        StockRetranslate(self)
#           --- Connect functions ---
