#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PySide6.QtCore import (
    Qt
)
from .Ui import *
from .Logic import *

#   --- Class ObjectInfo ---
class ObjectInfoS(QScrollArea): 
    def __init__(self, parent, t, i):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ Main ] ---
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
#           --- Set Class varaibles ---
#           --- Get functions from parent [ core ] ---
#           --- Call func ---
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
        self.IconL = QLabel(self.WidgetW)
        self.NameL = QLabel(self.WidgetW)
        self.IsoL = QLabel(self.WidgetW)
        self.ContinentL = QLabel(self.WidgetW)
        self.SubRegion = QLabel(self.WidgetW)
#           --- Info ---
        self.InfoW = QWidget(self)
        self.InfoL = QGridLayout(self.InfoW)
        self.InfoTitleL = QLabel(self.InfoW)
        self.CurrencyCodeNameL = QLabel(self.InfoW)
        self.CurrencyCodeValueL = QLabel(self.InfoW)
        self.CurrencyNameNameL = QLabel(self.InfoW)
        self.CurrencyNameValueL = QLabel(self.InfoW)
        self.CapitalCityNameL = QLabel(self.InfoW)
        self.CapitalCityValueL = QLabel(self.InfoW)
        self.TimezoneNameL = QLabel(self.InfoW)
        self.TimezoneValueL = QLabel(self.InfoW)
#           --- Stock Exchange Metadata ---
        self.ExchangeNameNameL = QLabel(self.InfoW)
        self.ExchangeNameValueL = QLabel(self.InfoW)
        self.ExchangeCodeMicNameL = QLabel(self.InfoW)
        self.ExchangeCodeMicValueL = QLabel(self.InfoW)
        self.ExchangeCountryNameL = QLabel(self.InfoW)
        self.ExchangeCountryValueL = QLabel(self.InfoW)
        self.ExchangeTimezoneNameL = QLabel(self.InfoW)
        self.ExchangeTimezoneValueL = QLabel(self.InfoW)
        self.TradingHoursNameL = QLabel(self.InfoW)
        self.TradingHoursValueL = QLabel(self.InfoW)
        self.CurrencyNameL = QLabel(self.InfoW)
        self.CurrencyValueL = QLabel(self.InfoW)
#           --- Call functions ---
        CountryUi(self)
        CountryReloadStyle(self)
        CountryRetranslate(self)
#           --- Connect functions ---

    def Market(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
        self.IconL = QLabel(self.WidgetW)
        self.TickerL = QLabel(self.WidgetW)
        self.NameL = QLabel(self.WidgetW)
        self.MicCodeL = QLabel(self.WidgetW)
        self.OperatingMicL = QLabel(self.WidgetW)
        self.CountryL = QLabel(self.WidgetW)
#           --- Info ---
        self.InfoW = QWidget(self.WidgetW)
        self.InfoL = QGridLayout(self.InfoW)
        self.InfoTitleL = QLabel(self.InfoW)
        self.FoundedYearNameL = QLabel(self.InfoW)
        self.FoundedYearValueL = QLabel(self.InfoW)
        self.CityNameL = QLabel(self.InfoW)
        self.CityValueL = QLabel(self.InfoW)
        self.TimezoneNameL = QLabel(self.InfoW)
        self.TimezoneValueL = QLabel(self.InfoW)
        self.CurrencyNameL = QLabel(self.InfoW)
        self.CurrencyValueL = QLabel(self.InfoW)
        self.WebsiteNameL = QLabel(self.InfoW)
        self.WebsiteValueL = QLabel(self.InfoW)
        self.MarketTypesNameL = QLabel(self.InfoW)
        self.MarketTypesValueL = QLabel(self.InfoW)
#           --- Trading session ---
        self.TradingSessionTitleL = QLabel(self.InfoW)
        self.PreMarketNameL = QLabel(self.InfoW)
        self.PreMarketValueL = QLabel(self.InfoW)
        self.OpenNameL = QLabel(self.InfoW)
        self.OpenValueL = QLabel(self.InfoW)
        self.CloseNameL = QLabel(self.InfoW)
        self.CloseValueL = QLabel(self.InfoW)
#           --- Calendar ---
        self.CalendarTitleL = QLabel(self.InfoW)
        self.FreeDaysNameL = QLabel(self.InfoW)
        self.FreeDaysValueL = QLabel(self.InfoW)
#           --- Exchange structure & regulation ---
        self.ExchangeStructureTitleL = QLabel(self.InfoW)
        self.InstrumentTypesNameL = QLabel(self.InfoW)
        self.InstrumentTypesValueL = QLabel(self.InfoW)
        self.MarketSegmentsNameL = QLabel(self.InfoW)
        self.MarketSegmentsValueL = QLabel(self.InfoW)
        self.RegulatorsNameL = QLabel(self.InfoW)
        self.RegulatorsValueL = QLabel(self.InfoW)
        self.TradingSystemsNameL = QLabel(self.InfoW)
        self.TradingSystemsValueL = QLabel(self.InfoW)
#           --- Call functions ---
        MarketUi(self)
        MarketReloadStyle(self)
        MarketRetranslate(self)
#           --- Connect functions ---


    def Stock(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
        self.IconL = QLabel(self.WidgetW)
        self.TickerL = QLabel(self.WidgetW)
        self.NameL = QLabel(self.WidgetW)
        self.MarketL = QLabel(self.WidgetW)
        self.CountryL = QLabel(self.WidgetW)
        self.InfoW = QWidget(self.WidgetW)
        self.InfoL = QGridLayout(self.InfoW)
        self.InfoTitleL = QLabel(self.InfoW)
        self.ActivityNameL = QLabel(self.InfoW)
        self.ActivityValueL = QLabel(self.InfoW)
        self.IndustryNameL = QLabel(self.InfoW)
        self.IndustryValueL = QLabel(self.InfoW)
        self.DateEstablishNameL = QLabel(self.InfoW)
        self.DateEstablishValueL = QLabel(self.InfoW)
        self.EmployesNameL = QLabel(self.InfoW)
        self.EmployesValueL = QLabel(self.InfoW)
        self.WebNameL = QLabel(self.InfoW)
        self.WebValueL = QLabel(self.InfoW)
        self.AdresNameL = QLabel(self.InfoW)
        self.AdresValueL = QLabel(self.InfoW)
        self.ManagmentTitleL = QLabel(self.InfoW)
        self.CEONameL = QLabel(self.InfoW)
        self.CEOValueL = QLabel(self.InfoW)
        self.CFONameL = QLabel(self.InfoW)
        self.CFOValueL = QLabel(self.InfoW)
        self.ManagmentNameL = QLabel(self.InfoW)
        self.ManagmentValueL = QLabel(self.InfoW)
        self.SupervisoryBoardNameL = QLabel(self.InfoW)
        self.SupervisoryBoardValueL = QLabel(self.InfoW)
#           --- Call functions ---
        StockUi(self)
        StockReloadStyle(self)
        StockRetranslate(self)
#           --- Connect functions ---
