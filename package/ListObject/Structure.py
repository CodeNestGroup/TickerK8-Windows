#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from .Ui import *
from .Logic import *

#   --- Class ListObject ---
class ListObjectW(QWidget): 
    def __init__(self, parent, d, f):
        super().__init__(parent.OpenedW)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ main ] ---
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
        self.ObjectList = parent.ObjectList
#           --- Set Class varaibles ---
        self.SetData = d
#           --- Get functions from parent [ main ] ---
        self.Open = f
#       --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NullDataL = None
        self.NameL = None
        self.DataS = None
#       --- Call functions ---
        ListObjectUi(self)
        ListObjectReloadStyle(self)
        if self.ObjectList:
            self.Data(parent)
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