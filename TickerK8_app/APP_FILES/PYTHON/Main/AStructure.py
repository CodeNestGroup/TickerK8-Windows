#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QLineEdit,
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *
from ListObject.AStructure import ListObjectW
from ListNews.AStructure import ListNewsW
from NewsList.AStructure import NewsListS

#   --- Class ---
class MainW(QWidget): 
    def __init__(self, parent):
        super().__init__(parent)
        self.Path = parent.main_path
        self.GetNewsListD = parent.database.GetNewsList
        self.GetNewsById = parent.database.GetNewsById
        self.UpdateNewsPopularity = parent.database.UpdateNewsPopularity
        self.AddObjectToList = parent.database.AddObjectToList
        self.DeleteObjectFromList = parent.database.DeleteObjectFromList
        self.GetUserConfig = parent.database.GetUserConfig
        self.LoggedUserId = parent.logged_user_id
        ReloadConfig(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.BacgroundConf = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Main/CBackgroundConf.json', 'r', encoding='utf-8'))
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
        self.WidgetBackgroundPainter = lambda: WidgetBackgroundPainter(self)
        self.BackgroundT.timeout.connect(self.WidgetBackgroundPainter)
        self.BackgroundT.start(1)
#           --- Connect  functions ---
        self.NavDefaultB.clicked.connect(self.MainPage)
        self.NavListObjectB.clicked.connect(self.ListPage)
        self.NavObjectB.clicked.connect(self.ObjectPage)
        self.NavNewsB.clicked.connect(self.NewsPage)

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
        self.ListObjectW = ListObjectW(self.OpenedW, self, [1, 1, 1, 1, 1], SetupMainObject)
        self.ListNewsW = ListNewsW(self.OpenedW, self)
#           --- Call functions ---
        MainPageUi(self)
#           --- Connect  functions ---

    def ListPage(self):
#           --- Create objects ---
        self.ResetPage()
        self.OpenedW = QWidget(self)
        self.OpenedL = QGridLayout(self.OpenedW)
        self.ListObjectW = ListObjectW(self.OpenedW, self, [1, 1, 1, 1, 0], ListDeleteObject)
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
        self.ListObjectW = ListObjectW(self.OpenedW, self, [0, 0, 1, 0, 1], SetupObject)
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
        NewsListS(self, self.GetNewsListD('stock', GetIdByTypeInLists(self.ObjectList, 'stock'), self.Language))
#           --- Connect  functions ---
        self.NewsStockB.clicked.connect(lambda: NewsListS(self, self.GetNewsListD('stock', GetIdByTypeInLists(self.ObjectList, 'stock'), self.Language)))
        self.NewsMarketB.clicked.connect(lambda: NewsListS(self, self.GetNewsListD('market', GetIdByTypeInLists(self.ObjectList, 'market'), self.Language)))
        self.NewsCountryB.clicked.connect(lambda: NewsListS(self, self.GetNewsListD('country', GetIdByTypeInLists(self.ObjectList, 'country'), self.Language)))
        self.NewsWorldB.clicked.connect(lambda: NewsListS(self, self.GetNewsListD('world', [1, 2, 3, 4, 5, 6, 7], self.Language)))