""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QScrollArea, # Scroll widget
    QGridLayout, # Grid layout
    QApplication,
    QGraphicsView
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import chart ui """
from .ui import *
#______________________________________________________________________________________________________________________
""" Import chart logic """
from .logic import *
#######################################################################################################################
class Chart_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
        self.main_news = None # Set dafoult
        self.main_news_list = None # Set dafoult
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8')) # Get global config data
        self.main_config = json.load(open(self.main_path+'/CONFIG/chart/main.json', 'r', encoding='utf-8')) # Get main config data
        self.chart_translate = json.load(open(self.main_path+'/CONFIG/chart/translate.json', 'r', encoding='utf-8')) # Get main translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.top_widget = QWidget(self)
        self.top_layout = QGridLayout(self.top_widget)
        self.top_exit_button = QPushButton(self.top_widget)
        self.top_title_label = QLabel(self.top_widget)
        self.top_fullscrean_button = QPushButton(self.top_widget)
        self.top_settings_button = QPushButton(self.top_widget)
        self.main_chart_graphics_view = None
        self.bottom_widget = QWidget(self)
        self.bottom_layout = QGridLayout(self.bottom_widget)
        self.bottom_1d_button = QPushButton(self.bottom_widget)
        self.bottom_5d_button = QPushButton(self.bottom_widget)
        self.bottom_1m_button = QPushButton(self.bottom_widget)
        self.bottom_3m_button = QPushButton(self.bottom_widget)
        self.bottom_1y_button = QPushButton(self.bottom_widget)
        self.bottom_ytd_button = QPushButton(self.bottom_widget)
        self.bottom_all_button = QPushButton(self.bottom_widget)
        self.settings_background_widget = None 
#______________________________________________________________________________________________________________________
        """ Call functions """
        chart_ui(self) # Call chart ui function
        chart_reload_style(self) # Call chart style function 
        chart_retranslate(self) # Call chart retranslate function
        #create_chart(self) # Create chart
#______________________________________________________________________________________________________________________
        """ Connect  functions """
        self.top_fullscrean_button.clicked.connect(full_screan)
        self.top_settings_button.clicked.connect(lambda: settings_widget(self))
        self.bottom_1d_button.clicked.connect(lambda: Chart_controller(self))
        self.bottom_5d_button.clicked.connect(lambda: create_chart(self))
        self.bottom_1m_button.clicked.connect(lambda: create_chart(self))
        self.bottom_3m_button.clicked.connect(lambda: create_chart(self))
        self.bottom_1y_button.clicked.connect(lambda: create_chart(self))
        self.bottom_ytd_button.clicked.connect(lambda: create_chart(self))
        self.bottom_all_button.clicked.connect(lambda: create_chart(self))
#######################################################################################################################
