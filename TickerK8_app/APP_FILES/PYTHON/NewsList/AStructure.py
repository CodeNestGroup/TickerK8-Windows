#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QVBoxLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class NewsListS(QScrollArea): 
    def __init__(self, MainSelf, GetNewsListData):
        super().__init__(MainSelf.OpenedW)
        self.MainSelf = MainSelf
        self.Path = self.MainSelf.Path
        self.Theme = self.MainSelf.Theme
        self.Language = self.MainSelf.Language
        self.GetNewsListData = GetNewsListData
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Create objects ---
        self.ListW = QWidget(self)
        self.ListL = QVBoxLayout(self)
#           --- Call functions ---
        NewsListUi(self)
        NewsListReloadStyle(self)
        CreateList(self)
#           --- Connect  functions ---