""" Import packages """
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
        Qt,
        pyqtSignal
)
""" Import main list pacakges """
from .ui import *
from .logic import *
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Main_news_list_widget(QWidget):
    open_news = pyqtSignal(int)
    def __init__(self, parent, news_type):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.parent = parent
        self.news_type = news_type
        """ Set paths, file name"""
        self.main_path = ResourcePath(2)
        """ Create objects """
        self.main_layout = QGridLayout(self) 
        self.panel_widget = QWidget(self)
        self.panel_layout = QGridLayout(self.panel_widget)
        self.title_label = QLabel(self)
        self.news_list_scroll = QScrollArea(self)
        self.exit_button = QPushButton(self)
        """ Call functions"""
        main_news_list_ui(self)
        main_news_list_reload_style(self)
        main_news_list_retranslate(self)
        news_list_widget(self)
        """ Connect functions """
        self.exit_button.clicked.connect(lambda: self.deleteLater())
#______________________________________________________________________________________________________________________
