""" Import packages """
import pathlib 
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton, 
    QComboBox,
    QGridLayout, 
    QVBoxLayout
)
from PyQt5.QtCore import (
        Qt
)
""" Import main news packages """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Main_news_widget(QWidget):
    def __init__(self, parent, data):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.parent = parent
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.panel_widget = QWidget(self)
        self.panel_layout = QGridLayout(self.panel_widget)
        self.news_scroll = QScrollArea(self.panel_widget)
        self.panel_exit_button = QPushButton(self.panel_widget)
        """ Call functions"""
        main_news_ui(self)
        main_news_reload_style(self)
        main_news_retranslate(self)
        news_widget(self, data)
        """ Connect functions """
        self.panel_exit_button.clicked.connect(lambda: self.deleteLater())
#______________________________________________________________________________________________________________________
