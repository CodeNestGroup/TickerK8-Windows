#   --- Improt ---
import json
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)

def NewsReadUi(self):
    self.setObjectName('NewsReadS')
    self.ReadW.setObjectName('ReadW')
    self.PhotoL.setObjectName('PhotoL')
    self.TitleL.setObjectName('TitleL')
    self.ItemNameL.setObjectName('ItemNameL')
    self.DataL.setObjectName('DataL')
    self.ContentW.setObjectName('ContentW')
    self.SourceW.setObjectName('SourceW')
    self.SourceTitleL.setObjectName('SourceTitleL')
    self.HashW.setObjectName('HashW')
    self.HashTitleL.setObjectName('HashTitleL')
    self.AuthorL.setObjectName('AuthorL')
    self.ContentW.setProperty('class', 'SubW')
    self.SourceW.setProperty('class', 'SubW')
    self.HashW.setProperty('class', 'SubW')
    self.SourceTitleL.setProperty('class', 'SubTitleL')
    self.HashTitleL.setProperty('class', 'SubTitleL')
    self.ReadL.addWidget(self.PhotoL)
    self.ReadL.addWidget(self.TitleL)
    self.ReadL.addWidget(self.ItemNameL)
    self.ReadL.addWidget(self.DataL)
    self.ReadL.addWidget(self.ContentW)
    self.ReadL.addWidget(self.SourceW)
    self.ReadL.addWidget(self.HashW)
    self.ReadL.addWidget(self.AuthorL)
    self.ReadL.setSpacing(0)
    self.ReadL.setContentsMargins(0,0,0,0)
    self.ReadW.setLayout(self.ReadL)
    self.ContentL.setSpacing(0)
    self.ContentL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.ContentL.setColumnStretch(i, 1)
    self.ContentW.setLayout(self.ContentL)
    self.SourceL.addWidget(self.SourceTitleL, 0, 2, 1, 96)
    self.SourceL.setSpacing(0)
    self.SourceL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.SourceL.setColumnStretch(i, 1)
    self.HashW.setLayout(self.HashL)
    self.HashL.addWidget(self.HashTitleL, 0, 2, 1, 96)
    self.HashL.setSpacing(0)
    self.HashL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.HashL.setColumnStretch(i, 1)
    self.HashW.setLayout(self.HashL)
    self.MainSelf.OpenedL.addWidget(self, 0, 3, 90, 40)
    self.show()
    self.setWidgetResizable(True)
    self.setWidget(self.ReadW)
    self.TitleL.setAlignment(Qt.AlignCenter)
    self.TitleL.setWordWrap(True)
    self.ItemNameL.setAlignment(Qt.AlignLeft)
    self.DataL.setAlignment(Qt.AlignLeft)
    self.SourceTitleL.setAlignment(Qt.AlignCenter)
    self.HashTitleL.setAlignment(Qt.AlignCenter)
    self.AuthorL.setAlignment(Qt.AlignLeft)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ReadW.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.PhotoL.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.PhotoL.setFixedSize(QSize(self.width(), int(self.height()*0.4)))
    self.TitleL.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.ItemNameL.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.DataL.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.ContentW.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.SourceW.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.SourceTitleL.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.HashW.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.HashTitleL.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

def NewsReadReloadStyle(self):
    m = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/NewsRead/BNewsRead.css', encoding='utf-8').read()
    c = open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/NewsRead/BNewsRead{self.Theme}.css', encoding='utf-8').read()
    self.setStyleSheet(m+c)

def NewsReadRetranslate(self):
    t = json.load(open(f'{self.Path}/TickerK8_app/APP_FILES/PYTHON/NewsRead/CNewsReadRetranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    ItemName = ''
    if self.NewsData[4]:
        ItemName = self.NewsData[4]
    elif self.NewsData[5]:
        ItemName = self.NewsData[5]
    elif self.NewsData[6]:
        ItemName = self.NewsData[6]
    self.TitleL.setText(self.NewsData[2])
    self.ItemNameL.setText(ItemName)
    self.DataL.setText(str(self.NewsData[1].strftime("%Y-%m-%d %H:%M:%S")))
    self.SourceTitleL.setText(t['SourceTitleL'][l])
    self.HashTitleL.setText(t['HashTitleL'][l])
    self.AuthorL.setText(f'By {self.NewsData[9]}')
