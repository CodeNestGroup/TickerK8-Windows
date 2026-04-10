""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QGridLayout,
)
from PyQt5.QtCore import (
    Qt
)
""" Import main search modules """
from .ui import *
from .logic import *
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Main_search_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.parent= parent
        """ Set paths, file name"""
        self.main_path = ResourcePath(2)
        self.add_object = None
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.panel_widget = QWidget(self)
        self.panel_layout = QVBoxLayout(self.panel_widget)
        self.panel_search_widget = QWidget(self.panel_widget)
        self.panel_search_layout = QGridLayout(self.panel_search_widget)
        self.panel_search_lineedit = QLineEdit(self.panel_search_widget)
        self.panel_type_stock_button = QPushButton(self.panel_search_widget)
        self.panel_type_etf_button = QPushButton(self.panel_search_widget)
        self.panel_type_forex_button = QPushButton(self.panel_search_widget)
        self.panel_type_index_button = QPushButton(self.panel_search_widget)
        self.panel_type_market_button = QPushButton(self.panel_search_widget)
        self.panel_type_country_button = QPushButton(self.panel_search_widget)
        self.panel_id_label = QLabel(self.panel_search_widget)
        self.panel_object_name_label = QLabel(self.panel_search_widget)
        self.panel_market_name_label = QLabel(self.panel_search_widget)
        self.panel_scroll = QScrollArea(self.panel_search_widget)
        self.panel_scroll_widget = None 
        self.panel_exit_button = QPushButton(self.panel_search_widget)
        self.button_list = [
                self.panel_type_stock_button,
                self.panel_type_etf_button,
                self.panel_type_forex_button,
                self.panel_type_index_button,
                self.panel_type_market_button,
                self.panel_type_country_button
        ]
        self.add_object = None 
        self.panel_add_widget = None 
        self.panel_add_section_scroll = None 
        self.panel_add_section_exit_button = None 
        self.panel_add_object_scroll = None 
        self.panel_add_object_exit_button = None 
        """ Call functions """
        main_search_ui(self)
        main_search_reload_style(self)
        main_search_retranslate(self)
        filters_load(self)
        text_changed(self)
        """ Connect functions """
        self.panel_search_lineedit.textChanged.connect(lambda: text_changed(self))
        self.panel_type_stock_button.clicked.connect(lambda: filters_changed(self, 0))
        self.panel_type_etf_button.clicked.connect(lambda: filters_changed(self, 1))
        self.panel_type_forex_button.clicked.connect(lambda: filters_changed(self, 2))
        self.panel_type_index_button.clicked.connect(lambda: filters_changed(self, 3))
        self.panel_type_market_button.clicked.connect(lambda: filters_changed(self, 4))
        self.panel_type_country_button.clicked.connect(lambda: filters_changed(self, 5))
        self.panel_exit_button.clicked.connect(lambda: self.deleteLater())
#______________________________________________________________________________________________________________________
