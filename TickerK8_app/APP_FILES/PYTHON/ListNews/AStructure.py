#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
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
class ListNewsW(QWidget): 
    def __init__(self, parent, s):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language
#        self.NewsList = parent.NewsList
        self.NewsTimer = None
#           --- Create objects ---
        self.Layout = QVBoxLayout(self)
#           --- Call functions ---
        ListNewsUi(self)
        ListNewsReloadStyle(self)
        Setup(self)