#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout,
    QVBoxLayout
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class ListObjectW(QWidget): 
    def __init__(self, parent, s, d, func):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language
        self.ObjectList = s.ObjectList
        self.SetData = d
        self.OpenFunc = func
#       --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NullDataL = None
        self.NameL = None
        self.DataS = None
#       --- Call functions ---
        ListObjectUi(self)
        ListObjectReloadStyle(self)
        if self.ObjectList:
            self.Data(s)
        else:
            self.NullData()
#       --- Connect functions ---

    def NullData(self):
#       --- Create objects ---
        self.NullDataL = QLabel(self)
#       --- Call functions 
        NullDataUi(self)
        NullDataRetranslate(self)
    
    def Data(self, MainSelf):
#       --- Create objects ---
        self.NameL = QLabel(self)
        self.DataS = QScrollArea(self)
        self.DataW = QWidget(self.DataS)
        self.DataL = QGridLayout(self.DataW)
#       --- Call functions ---
        DataUi(self)
        SetupData(self, MainSelf)
#       --- Connect functions ---