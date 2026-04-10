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

def ObjectUi(self):
    self.setObjectName('ObjectW')
    self.IconL.setObjectName('IconL')
    self.TickerL.setObjectName('TickerL')
    self.ChartW.setObjectName('ChartW')
    self.InfoTitleL.setObjectName('InfoTitleL')
    self.InfoW.setObjectName('InfoW')
    self.InfoNameNameL.setObjectName('InfoNameNameL')
    self.InfoNameValueL.setObjectName('InfoNameValueL')
    self.InfoTickerNameL.setObjectName('InfoTickerNameL')
    self.InfoTickerValueL.setObjectName('InfoTickerValueL')
    self.InfoNameNameL.setProperty('class', 'Name')
    self.InfoTickerNameL.setProperty('class', 'Name')
    self.InfoNameValueL.setProperty('class', 'Value')
    self.InfoTickerValueL.setProperty('class', 'Value')
    self.Layout.addWidget(self.IconL, 2, 30, 8, 40)
    self.Layout.addWidget(self.TickerL, 15, 0, 5, 100)
    self.Layout.addWidget(self.ChartW, 25, 0, 40, 100)
    self.Layout.addWidget(self.InfoTitleL, 70, 0, 5, 100)
    self.Layout.addWidget(self.InfoW, 80, 0, 20, 100)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.InfoL.addWidget(self.InfoNameNameL, 0, 0, 10, 50)
    self.InfoL.addWidget(self.InfoNameValueL, 0, 50, 10, 50)
    self.InfoL.addWidget(self.InfoTickerNameL, 10, 0, 10, 50)
    self.InfoL.addWidget(self.InfoTickerValueL, 10, 50, 10, 50)
    self.InfoL.setSpacing(0)
    self.InfoL.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.InfoL.setRowStretch(enc, 1)
        self.InfoL.setColumnStretch(enc, 1)
    self.InfoW.setLayout(self.InfoL)
    self.show()
    self.IconL.setAlignment(Qt.AlignCenter)
    self.TickerL.setAlignment(Qt.AlignCenter)
    self.InfoTitleL.setAlignment(Qt.AlignCenter)
    self.InfoNameNameL.setAlignment(Qt.AlignCenter)
    self.InfoNameValueL.setAlignment(Qt.AlignCenter)
    self.InfoTickerNameL.setAlignment(Qt.AlignCenter)
    self.InfoTickerValueL.setAlignment(Qt.AlignCenter)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.IconL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.TickerL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChartW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoTitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoNameNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoNameValueL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoTickerNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoTickerValueL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ObjectReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/APP_FILES/PYTHON/Object/BMain.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/Object/B{t}.css').read()
    self.setStyleSheet(m+c)

def ObjectRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Object/CMainObject.json', 'r'))
    l = self.Language
    self.InfoTitleL.setText(t['InfoTitleL'][l])
    self.InfoNameNameL.setText(t['InfoNameNameL'][l])
    self.InfoTickerNameL.setText(t['InfoTickerNameL'][l])
