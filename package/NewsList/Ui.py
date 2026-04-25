#   --- Improt ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QSizePolicy
)
from PySide6.QtCore import (
    Qt,
    QSize
)

def NewsListUi(self):
    self.setObjectName('NewsListS')
    self.ListW.setObjectName('ListW')
    self.ListL.setSpacing(0)
    self.ListL.setContentsMargins(0,0,0,0)
    self.ListW.setLayout(self.ListL)
    self.Parent.OpenedL.addWidget(self, 0, 57, 90, 40)
    self.show()
    self.setWidgetResizable(True)
    self.setWidget(self.ListW)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ListW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def NewsListReloadStyle(self):
    m = open(f'{self.Path}/assets/CSS/NewsListMain.css').read()
    c = open(f'{self.Path}/assets/CSS/NewsList{self.Theme}.css').read()
    self.setStyleSheet(m+c)
    