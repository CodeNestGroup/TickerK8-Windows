#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QVBoxLayout
)
from PySide6.QtCore import (
    Qt,
    QTimer
)
from .Ui import *
from .Logic import *

#   --- Class NewsList ---
class NewsListS(QScrollArea): 
    def __init__(self, parent, GetNewsListData):
        super().__init__(parent.OpenedW)
        #           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ Main ] ---
        self.Parent  = parent
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
        self.GetNewsListData = GetNewsListData
#           --- Set Class varaibles ---
#           --- Get functions from parent [ Main ] ---
        self.GetNewsByIdF = parent.GetNewsByIdF
        self.UpdateNewsPopularityF = parent.UpdateNewsPopularityF


#           --- Create objects ---
        self.ListW = QWidget(self)
        self.ListL = QVBoxLayout(self)
#           --- Call functions ---
        NewsListUi(self)
        NewsListReloadStyle(self)
        CreateList(self)
#           --- Connect  functions ---