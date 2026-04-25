#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QLabel, 
    QGridLayout
)
from PySide6.QtCore import (
    Qt
)
from .Ui import *
from .Logic import *

#   --- Class Object ---
class ObjectW(QWidget): 
    def __init__(self, parent, t, i):
        super().__init__(parent.OpenedW)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ main ] ---
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
        self.ObjectList = parent.ObjectList
#           --- Set Class varaibles ---
#           --- Get functions from parent [ core ] ---
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
