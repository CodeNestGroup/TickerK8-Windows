#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QLineEdit,
    QScrollArea,
    QGridLayout
)
from PySide6.QtCore import (
    Qt,
    QTimer
)
from .Ui import *
from .Logic import *
#   --- Import Main modules ---
from ..ListObject.Structure import ListObjectW
from ..ListNews.Structure import ListNewsW
from ..NewsList.Structure import NewsListS

#   --- Class Main ---
class MainW(QWidget): 
    def __init__(self, parent):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
#           --- Set Class varaibles ---
        self.BackgroundConf = json.load(open(f'{self.Path}/assets/JSON/BackgroundConf.json', 'r', encoding='utf-8'))
#           --- Get functions from parent [ core ] ---
        self.GetNewsListF = parent.Database.GetNewsList
        self.GetNewsByIdF = parent.Database.GetNewsById
        self.UpdateNewsPopularityF = parent.Database.UpdateNewsPopularity
        self.AddObjectToListF = parent.Database.AddObjectToList
        self.DeleteObjectFromList = parent.Database.DeleteObjectFromList
        self.GetUserConfig = parent.Database.GetUserConfig
        self.LoggedUserId = parent.LoggedUserId
        self.SettingsOpenF = parent.SettingsOpen
        self.LoginOpenF = parent.LoginOpen
        ReloadConfig(self)
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NavW = QWidget(self)
        self.NavL = QGridLayout(self)
        self.NavDefaultB = QPushButton(self.NavW)
        self.NavListObjectB = QPushButton(self.NavW)
        self.NavObjectB = QPushButton(self.NavW)
        self.NavNewsB = QPushButton(self.NavW)
        self.NavSettingsB = QPushButton(self.NavW)
        self.NavLogoutB = QPushButton(self.NavW)
        self.OpenedW = None
        self.FooterW = QWidget(self)
        self.BackgroundT = QTimer(self)
#           --- Call functions ---
        MainUi(self)
        MainReloadStyle(self)
        MainRetranslate(self)
        self.MainPage()
        self.BackgroundPainter = lambda: BackgroundPainter(self)
        self.BackgroundT.timeout.connect(self.BackgroundPainter)
        self.BackgroundT.start(1000)
#           --- Connect  functions ---
        self.NavDefaultB.clicked.connect(self.MainPage)
        self.NavListObjectB.clicked.connect(self.ListPage)
        self.NavObjectB.clicked.connect(self.ObjectPage)
        self.NavNewsB.clicked.connect(self.NewsPage)
        self.NavSettingsB.clicked.connect(self.SettingsOpenF)
        self.NavLogoutB.clicked.connect(self.LoginOpenF)

    def ResetPage(self):
        if self.OpenedW:
            self.OpenedW.deleteLater()
            self.OpenedW = None

    def MainPage(self):
        self.ObjectW = None
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self)
        self.ListObjectW = ListObjectW(self, [1, 1, 1, 1, 1], SetupMainObject)
        # Object
        self.ListNewsW = ListNewsW(self)
#           --- Call functions ---
        MainPageUi(self)
#           --- Connect  functions ---

    def ListPage(self):
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self.OpenedW)
        self.ListObjectW = ListObjectW(self, [1, 1, 1, 1, 0], ListDeleteObject)
        self.AddObjectB = QPushButton(self.OpenedW)
#           --- Call functions ---
        ListPageUi(self)
        ListPageReloadStyle(self)
        ListPageRetranslate(self)
#           --- Connect  functions ---
        self.AddObjectB.clicked.connect(self.ListAddPage)

    def ListAddPage(self):
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self.OpenedW)
        self.ListAddBackgroundW = QWidget(self.OpenedW)
        self.ListAddBackgroundL = QGridLayout(self.ListAddBackgroundW)
        self.NameL = QLabel(self.ListAddBackgroundW)
        self.ListAddS = QScrollArea(self.ListAddBackgroundW)
        self.ListAddW = QWidget(self.ListAddS)
        self.ListAddL = QGridLayout(self.ListAddW)
        self.ExitB = QPushButton(self.OpenedW)
#           --- Call functions ---
        ListAddPageUi(self)
        ListAddPageReloadStyle(self)
        ListAddPageRetranslate(self)
        ListAddSetupList(self)
#           --- Connect  functions ---
        self.ExitB.clicked.connect(self.ListPage)

    def ListSearchPage(self):
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self.OpenedW)
        self.SearchW = QWidget(self.ListAddBackgroundW)
        self.SearchL = QGridLayout(self.SearchW)
        self.SearchE = QLineEdit(self.SearchW)
        self.SortType = 'stock'
        self.StockB = QPushButton(self.SearchW)
        self.MarketB = QPushButton(self.SearchW)
        self.CountryB = QPushButton(self.SearchW)
        self.ResultS = None
        self.ExitB = QPushButton(self.OpenedW)
#           --- Call functions ---
        ListSearchPageUi(self)
        ListSearchPageReloadStyle(self)
        ListSearchPageRetranslate(self)
        SetupResultS(self)
#           --- Connect  functions ---
        self.SearchE.textChanged.connect(lambda: SetupResultS(self))
        self.StockB.clicked.connect(lambda: SortTypeChange(self, 'stock'))
        self.MarketB.clicked.connect(lambda: SortTypeChange(self, 'market'))
        self.CountryB.clicked.connect(lambda: SortTypeChange(self, 'country'))
        self.ExitB.clicked.connect(self.ListAddPage)

    def ObjectPage(self):
        self.ObejctInfoS = None
        self.ObjectStatsS = None
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self.OpenedW)
        self.ListObjectW = ListObjectW(self, [0, 0, 1, 0, 1], SetupObject)
#           --- Call functions ---
        ObjectPageUi(self)
#           --- Connect  functions ---

    def NewsPage(self):
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self.OpenedW)
        self.OpenedW.NewsReadS = None
        self.NewsStockB = QPushButton(self.OpenedW)
        self.NewsMarketB = QPushButton(self.OpenedW)
        self.NewsCountryB = QPushButton(self.OpenedW)
        self.NewsWorldB = QPushButton(self.OpenedW)
#           --- Call functions ---
        NewsPageUi(self)
        NewsPageRetranslate(self)
        NewsListS(self, self.GetNewsListF('stock', GetIdByTypeInLists(self.ObjectList, 'stock'), self.Language))
#           --- Connect  functions ---
        self.NewsStockB.clicked.connect(lambda: NewsListS(self, self.GetNewsListF('stock', GetIdByTypeInLists(self.ObjectList, 'stock'), self.Language)))
        self.NewsMarketB.clicked.connect(lambda: NewsListS(self, self.GetNewsListF('market', GetIdByTypeInLists(self.ObjectList, 'market'), self.Language)))
        self.NewsCountryB.clicked.connect(lambda: NewsListS(self, self.GetNewsListF('country', GetIdByTypeInLists(self.ObjectList, 'country'), self.Language)))
        self.NewsWorldB.clicked.connect(lambda: NewsListS(self, self.GetNewsListF('world', [1, 2, 3, 4, 5, 6, 7], self.Language)))