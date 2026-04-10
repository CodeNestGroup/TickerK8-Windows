""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Simple line edit
    QGridLayout # Grid layout
)
from PyQt5.QtCore import Qt
#______________________________________________________________________________________________________________________
""" Import recover password ui """
from .ui import *
#______________________________________________________________________________________________________________________
""" Import recover password logic """
from .logic import *
#######################################################################################################################
""" Recover password widget """
class Recover_password_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True) # Force widget to draw background
        self.setParent(parent) # Set parent
#______________________________________________________________________________________________________________________
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8')) # Get global config data
        self.recover_password_translate = json.load(open(self.main_path+'/CONFIG/recover_password/translate.json', 'r', encoding='utf-8')) # Get global translate data
#______________________________________________________________________________________________________________________
        """ Create objects """
        self.recover_password_layout = QGridLayout(self)
        self.recover_password_title_label = QLabel(self)
        self.recover_password_requirments_label = QLabel(self)
        self.recover_password_password_lineedit = QLineEdit(self)
        self.recover_password_password_show_button = QPushButton(self)
        self.recover_password_confirm_password_lineedit = QLineEdit(self)
        self.recover_password_confirm_password_show_button = QPushButton(self)
        self.recover_password_code_label = QLabel(self)
        self.recover_password_time_label = QLabel(self)
        self.recover_password_code_lineedit = QLineEdit(self)
        self.recover_password_code_button = QPushButton(self)
        self.recover_password_confirm_button = QPushButton(self)
        self.recover_password_exit_button = QPushButton(self)
#______________________________________________________________________________________________________________________
        """ Call functions """
        recover_password_ui(self)
        recover_password_style(self)
        recover_password_translate(self)
#______________________________________________________________________________________________________________________
        """ Connect functions """
        self.recover_password_password_show_button.clicked.connect(lambda: show_hide_password(self))
        self.recover_password_confirm_password_show_button.clicked.connect(lambda: show_hide_confirm_password(self))
#######################################################################################################################
