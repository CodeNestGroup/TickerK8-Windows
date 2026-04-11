#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QVBoxLayout,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class NewsReadS(QScrollArea): 
    def __init__(self, MainSelf, NewsData):
        super().__init__(MainSelf.OpenedW)
        self.MainSelf = MainSelf
        self.Path = self.MainSelf.Path
        self.Theme = self.MainSelf.Theme
        self.Language = self.MainSelf.Language
        self.NewsData = NewsData[0]
        self.setAttribute(Qt.WA_StyledBackground, True)
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
