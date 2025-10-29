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
    QGridLayout # Grid layout
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import statistics ui """
from .ui import *
#______________________________________________________________________________________________________________________
""" Import statistics logic """
from .logic import *
#######################################################################################################################
""" Statistics widget """
class Statistics_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.main_title_label = QLabel(self)
        self.main_flag_label = QLabel(self)
        self.main_exit_button = QPushButton(self)
        self.main_close_button = QPushButton(self)
        self.main_scroll = QScrollArea(self)
        self.scroll_widget = None 
#______________________________________________________________________________________________________________________
        """ Call functions  """
        statistics_ui(self)
        statistics_reload_style(self)
        if self.global_config['mid_object'][0] == 'country':
                statisitcs_country(self)
                self.main_close_button.clicked.connect(lambda: statisitcs_country(self))
        elif self.global_config['mid_object'][0] == 'market':
                statistics_market(self)
        elif self.global_config['mid_object'][0] == 'index':
                statisitcs_index(self)
        elif self.global_config['mid_object'][0] == 'stock':
                statistics_stock(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
#######################################################################################################################
