#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QVBoxLayout
)
from PySide6.QtCore import (
    Qt,
    QTimer
)
from .Ui import *
from .Logic import *

#   --- ListNews ---
class ListNewsW(QWidget): 
    def __init__(self, parent):
        super().__init__(parent.OpenedW)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ main ] ---
        self.Path = parent.Path
        self.Theme = parent.Theme
        self.Language = parent.Language
#           --- Set Class varaibles ---
        self.NewsTimer = None
#           --- Get functions from parent [ core ] ---
#        self.NewsList = parent.NewsList
#           --- Create objects ---
        self.Layout = QVBoxLayout(self)
#           --- Call functions ---
        ListNewsUi(self)
        ListNewsReloadStyle(self)
        Setup(self)