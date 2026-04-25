#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QVBoxLayout,
    QGridLayout
)
from PySide6.QtCore import (
    Qt,
    QTimer
)
from .Ui import *
from .Logic import *

#   --- Class NewsRead ---
class NewsReadS(QScrollArea): 
    def __init__(self, parent, NewsData):
        super().__init__(parent.OpenedW)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Parent = parent
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
#           --- Set Class varaibles ---
        self.NewsData = NewsData[0]
#           --- Get functions from parent [ core ] ---
#           --- Create objects ---
        self.ReadW = QWidget(self)
        self.ReadL = QVBoxLayout(self.ReadW)
        self.PhotoL = QLabel(self.ReadW)
        self.TitleL = QLabel(self.ReadW)
        self.ItemNameL = QLabel(self.ReadW)
        self.DataL = QLabel(self.ReadW)
        self.ContentW = QWidget(self.ReadW)
        self.ContentL = QGridLayout(self.ContentW)
        self.SourceW = QWidget(self.ReadW)
        self.SourceL = QGridLayout(self.SourceW)
        self.SourceTitleL = QLabel(self.SourceW)
        self.HashW = QWidget(self.ReadW)
        self.HashL = QGridLayout(self.HashW)
        self.HashTitleL = QLabel(self.HashW)
        self.AuthorL = QLabel(self.ReadW)
#           --- Call functions ---
        NewsReadUi(self)
        NewsReadReloadStyle(self)
        NewsReadRetranslate(self)
        SetupContent(self)
#           --- Connect  functions ---
