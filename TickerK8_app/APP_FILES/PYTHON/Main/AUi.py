#   --- Improt ---
import json
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)

def MainUi(self):
    self.setObjectName('MainW')
    self.NavW.setObjectName('NavW')
    self.NavDefaultB.setObjectName('NavDefaultB')
    self.NavListObjectB.setObjectName('NavListObjectB')
    self.NavObjectB.setObjectName('NavObjectB')
    self.NavNewsB.setObjectName('NavNewsB')
    self.NavSettingsB.setObjectName('NavSettingsB')
    self.NavLogoutB.setObjectName('NavLogoutB')
    self.FooterW.setObjectName('FooterW')
    self.NavDefaultB.setProperty('class', 'NavButton')
    self.NavListObjectB.setProperty('class', 'NavButton')
    self.NavObjectB.setProperty('class', 'NavButton')
    self.NavNewsB.setProperty('class', 'NavButton')
    self.NavSettingsB.setProperty('class', 'FuncButton')
    self.NavLogoutB.setProperty('class', 'FuncButton')
    self.Layout.addWidget(self.NavW, 0, 0, 10, 100)
    self.Layout.addWidget(self.FooterW, 90, 0, 10, 100)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.NavL.addWidget(self.NavDefaultB, 25, 28, 50, 8)
    self.NavL.addWidget(self.NavListObjectB, 25, 40, 50, 8)
    self.NavL.addWidget(self.NavObjectB, 25, 52, 50, 8)
    self.NavL.addWidget(self.NavNewsB, 25, 64, 50, 8)
    self.NavL.addWidget(self.NavSettingsB, 30, 92, 40, 2)
    self.NavL.addWidget(self.NavLogoutB, 30, 95, 40, 2)
    self.NavL.setSpacing(0)
    self.NavL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.NavL.setRowStretch(i, 1)
        self.NavL.setColumnStretch(i, 1)
    self.NavW.setLayout(self.NavL)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavDefaultB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavListObjectB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavObjectB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavNewsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavSettingsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NavLogoutB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.FooterW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def MainReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BMain.css', encoding='utf-8').read()
    c = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/B{t}.css', encoding='utf-8').read()
    self.setStyleSheet(m+c)
    self.NavSettingsB.setIcon(QIcon(LoadSvg(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/i_settings_{t}.svg', 256, 256)))
    self.NavSettingsB.setIconSize(self.NavSettingsB.size())
    self.NavLogoutB.setIcon(QIcon(LoadSvg(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/i_exit_{t}.svg', 256, 256)))
    self.NavLogoutB.setIconSize(self.NavLogoutB.size())

def MainRetranslate(self):
    t = json.load(open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/CMainTranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.NavDefaultB.setText(t['NavDefaultB'][l])
    self.NavListObjectB.setText(t['NavListObjectB'][l])
    self.NavObjectB.setText(t['NavObjectB'][l])
    self.NavNewsB.setText(t['NavNewsB'][l])

def MainPageUi(self):
    self.OpenedW.setObjectName('OpenedW')
    self.OpenedL.addWidget(self.ListObjectW, 0, 3, 100, 30)
    self.OpenedL.addWidget(self.ListNewsW, 0, 67, 100, 30)
    self.OpenedL.setSpacing(0)
    self.OpenedL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.OpenedL.setRowStretch(i,1)
        self.OpenedL.setColumnStretch(i,1)
    self.OpenedW.setLayout(self.OpenedL)
    self.Layout.addWidget(self.OpenedW, 10, 0, 80, 100)
    self.OpenedW.show()
    self.OpenedW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ListPageUi(self):
    self.OpenedW.setObjectName('OpenedW')
    self.AddObjectB.setObjectName('AddObjectB')
    self.OpenedL.addWidget(self.ListObjectW, 0, 0, 90, 100)
    self.OpenedL.addWidget(self.AddObjectB, 94, 40,6, 20)
    self.OpenedL.setSpacing(0)
    self.OpenedL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.OpenedL.setRowStretch(i, 1)
        self.OpenedL.setColumnStretch(i, 1)
    self.OpenedW.setLayout(self.OpenedL)
    self.Layout.addWidget(self.OpenedW, 10, 0, 80, 100)
    self.OpenedW.show()
    self.OpenedW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.AddObjectB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ListPageReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BListPage.css', encoding='utf-8').read()
    c = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BListPage{self.Theme}.css', encoding='utf-8').read()
    self.OpenedW.setStyleSheet(m+c)

def ListPageRetranslate(self):
    t = json.load(open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/CListPageRetranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.AddObjectB.setText(t['AddObjectB'][l])

def ListAddPageUi(self):
    self.OpenedW.setObjectName('OpenedW')
    self.ListAddBackgroundW.setObjectName('ListAddBackgroundW')
    self.NameL.setObjectName('NameL')
    self.ListAddS.setObjectName('ListAddS')
    self.ListAddW.setObjectName('ListAddW')
    self.ExitB.setObjectName('ExitB')
    self.ListAddL.setSpacing(0)
    self.ListAddL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.ListAddL.setColumnStretch(i, 1)
    self.ListAddW.setLayout(self.ListAddL)
    self.ListAddBackgroundL.addWidget(self.NameL, 0, 0, 5, 100)
    self.ListAddBackgroundL.addWidget(self.ListAddS, 7, 2, 93, 96)
    self.ListAddBackgroundL.setSpacing(0)
    self.ListAddBackgroundL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.ListAddBackgroundL.setRowStretch(i, 1)
        self.ListAddBackgroundL.setColumnStretch(i, 1)
    self.ListAddBackgroundW.setLayout(self.ListAddBackgroundL)
    self.OpenedL.addWidget(self.ListAddBackgroundW, 0, 30, 90, 40)
    self.OpenedL.addWidget(self.ExitB, 94, 40, 6, 20)
    self.OpenedL.setSpacing(0)
    self.OpenedL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.OpenedL.setRowStretch(i, 1)
        self.OpenedL.setColumnStretch(i, 1)
    self.OpenedW.setLayout(self.OpenedL)
    self.Layout.addWidget(self.OpenedW, 10, 0, 80, 100)
    self.OpenedW.show()
    self.ListAddS.setWidgetResizable(True)
    self.ListAddS.setWidget(self.ListAddW)
    self.NameL.setAlignment(Qt.AlignCenter)
    self.OpenedW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListAddBackgroundW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListAddS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListAddW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ListAddPageReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BListAddPage.css', encoding='utf-8').read()
    c = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BListAddPage{self.Theme}.css', encoding='utf-8').read()
    self.OpenedW.setStyleSheet(m+c)

def ListAddPageRetranslate(self):
    t = json.load(open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/CListAddPageRetranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.ExitB.setText(t['ExitB'][l])

def ListSearchPageUi(self):
    self.OpenedW.setObjectName('OpenedW')
    self.SearchW.setObjectName('SearchW')
    self.SearchE.setObjectName('SearchE')
    self.StockB.setObjectName('StockB')
    self.MarketB.setObjectName('MarketB')
    self.CountryB.setObjectName('CountryB')
    self.StockB.setProperty('class', 'SortTypeB')
    self.MarketB.setProperty('class', 'SortTypeB')
    self.CountryB.setProperty('class', 'SortTypeB')
    self.ExitB.setObjectName('ExitB')
    self.SearchL.addWidget(self.SearchE, 0, 30, 10, 40)
    self.SearchL.addWidget(self.StockB, 12, 25, 5, 10)
    self.SearchL.addWidget(self.MarketB, 12, 38, 5, 10)
    self.SearchL.addWidget(self.CountryB, 12, 49, 5, 10)
    self.SearchL.setSpacing(0)
    self.SearchL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.SearchL.setRowStretch(i,1)
        self.SearchL.setColumnStretch(i,1)
    self.SearchW.setLayout(self.SearchL)
    self.OpenedL.addWidget(self.SearchW, 0, 30, 90, 40)
    self.OpenedL.addWidget(self.ExitB, 94, 40, 6, 20)
    self.OpenedL.setSpacing(0)
    self.OpenedL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.OpenedL.setRowStretch(i, 1)
        self.OpenedL.setColumnStretch(i, 1)
    self.OpenedW.setLayout(self.OpenedL)
    self.Layout.addWidget(self.OpenedW, 10, 0, 80, 100)
    self.OpenedW.show()
    self.OpenedW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SearchW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SearchE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.StockB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.MarketB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.CountryB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ListSearchPageReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BListSearchPage.css', encoding='utf-8').read()
    c = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BListSearchPage{self.Theme}.css', encoding='utf-8').read()
    self.OpenedW.setStyleSheet(m+c)

def ListSearchPageRetranslate(self):
    t = json.load(open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/CListSearchPageRetranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.SearchE.setPlaceholderText(t['SearchE'][l])
    self.StockB.setText(t['StockB'][l])
    self.MarketB.setText(t['MarketB'][l])
    self.CountryB.setText(t['CountryB'][l])
    self.ExitB.setText(t['ExitB'][l])

def ObjectPageUi(self):
    self.OpenedW.setObjectName('OpenedW')
    self.OpenedL.addWidget(self.ListObjectW, 0, 1, 100, 14)
    self.OpenedL.addWidget(self.ObejctInfoS, 0, 16, 100, 41)
    self.OpenedL.addWidget(self.ObjectStatsW, 0, 58, 100, 41)
    self.OpenedL.setSpacing(0)
    self.OpenedL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.OpenedL.setColumnStretch(i, 1)
    self.OpenedW.setLayout(self.OpenedL)
    self.Layout.addWidget(self.OpenedW, 10, 0, 80 ,100)
    self.OpenedW.show()
    self.OpenedW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def NewsPageUi(self):
    self.OpenedW.setObjectName('OpenedW')
    self.NewsStockB.setObjectName('NewsStockB')
    self.NewsMarketB.setObjectName('NewsMarketB')
    self.NewsCountryB.setObjectName('NewsCountryB')
    self.NewsWorldB.setObjectName('NewsWorldB')
    self.NewsStockB.setProperty('class', 'NewsB')
    self.NewsMarketB.setProperty('class', 'NewsB')
    self.NewsCountryB.setProperty('class', 'NewsB')
    self.NewsWorldB.setProperty('class', 'NewsB')
    self.OpenedL.addWidget(self.NewsStockB, 90, 57, 10, 8)
    self.OpenedL.addWidget(self.NewsMarketB, 90, 67, 10, 8)
    self.OpenedL.addWidget(self.NewsCountryB, 90, 77, 10, 8)
    self.OpenedL.addWidget(self.NewsWorldB, 90, 89, 10, 8)
    self.OpenedL.setSpacing(0)
    self.OpenedL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.OpenedL.setRowStretch(i, 1)
        self.OpenedL.setColumnStretch(i, 1)
    self.OpenedW.setLayout(self.OpenedL)
    self.Layout.addWidget(self.OpenedW, 10, 0, 80, 100)
    self.OpenedW.show()
    self.OpenedW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NewsStockB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NewsMarketB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NewsCountryB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NewsWorldB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def NewsPageReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BNewsPage.css', encoding='utf-8').read()
    c = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/BNewsPage{self.Theme}.css', encoding='utf-8').read()
    self.setStyleSheet(m+c)

def NewsPageRetranslate(self):
    t = json.load(open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/Main/CNewsPageRetranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.NewsStockB.setText(t['NewsStockB'][l])
    self.NewsMarketB.setText(t['NewsMarketB'][l])
    self.NewsCountryB.setText(t['NewsCountryB'][l])
    self.NewsWorldB.setText(t['NewsWorldB'][l])

def LoadSvg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap