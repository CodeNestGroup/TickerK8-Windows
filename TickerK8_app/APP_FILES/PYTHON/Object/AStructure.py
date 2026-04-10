#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class ObjectW(QWidget): 
    def __init__(self, parent, s, t, i):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language
        self.ObjectList = s.ObjectList
        self.ObjectListSorted = []
        self.ObjectListSortedIndex = 0
        self.Timer = None
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.IconL = QLabel(self)
        self.TickerL = QLabel(self)
        self.ChartW = QWidget(self)
        self.InfoTitleL = QLabel(self)
        self.InfoW = QWidget(self)
        self.InfoL = QGridLayout(self.InfoW)
        self.InfoNameNameL = QLabel(self.InfoW)
        self.InfoNameValueL = QLabel(self.InfoW)
        self.InfoTickerNameL = QLabel(self.InfoW)
        self.InfoTickerValueL = QLabel(self.InfoW)
#           --- Call functions ---
        ObjectUi(self)
        ObjectReloadStyle(self)
        ObjectRetranslate(self)
        Setup(self, t, i)
