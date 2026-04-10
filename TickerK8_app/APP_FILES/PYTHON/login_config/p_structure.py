""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QComboBox
        )
from PyQt5.QtCore import (
        Qt,
        QTimer
        )
""" Import login configuration modules """
from .p_ui import *
from .p_logic import *
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Login_configuration_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.main_path = ResourcePath(2)
        self.widget_list = [None, self.app_conf, None, self.sub_conf, None, self.accept_settings]
        self.widget_list_index = 0
        ResetConfig(self)
#       --- Create objects ---
        self.layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.info_label = QLabel(self)
        self.center_widget = None
        self.left_button = QPushButton(self)
        self.exit_button = QPushButton(self)
        self.right_button = QPushButton(self)
        self.accept_button = QPushButton(self)
        self.navi_label = QLabel(self)
#       --- Call functions ---
        ui(self)
        reload_style(self)
        retranslate(self)
#       --- Connect functions ---
        self.left_button.clicked.connect(lambda: Previous(self))
        self.right_button.clicked.connect(lambda: Next(self))
        
    def center_widget_setup(self):
        if self.center_widget:
            self.center_widget.deleteLater()
            self.center_widget = None 
        self.center_widget = QWidget(self)
        self.center_layout = QGridLayout(self.center_widget)
        center_widget_setup_ui(self)

    def app_conf(self):
#       --- Create objects ---
        self.language_subtitle_label = QLabel(self.center_widget)
        self.language_combobox = QComboBox(self.center_widget)
        self.theme_subtitle_label = QLabel(self.center_widget)
        self.theme_combobox = QComboBox(self.center_widget)
#       --- Call functions ---
        app_conf_ui(self)
        app_conf_retranslate(self)
#       --- Connect functions ---
        self.language_combobox.currentIndexChanged.connect(lambda: ChangeLanguage(self))
        self.language_combobox.currentIndexChanged.connect(lambda: app_conf_retranslate(self))
        self.theme_combobox.currentIndexChanged.connect(lambda: ChangeTheme(self))

    def sub_conf(self):
#       --- Create objects ---
        self.checked_button = None
        self.left_button = QPushButton(self.center_widget)
        self.center_button = QPushButton(self.center_widget)
        self.right_button = QPushButton(self.center_widget)
#       --- Call functions ---
        sub_conf_ui(self)
        sub_conf_reload_style(self)
        sub_conf_retranslate(self)
#       --- Connect functions ---
        self.left_button.clicked.connect(lambda: ChangeSub(self, 3, self.left_button))
        self.center_button.clicked.connect(lambda: ChangeSub(self, 1, self.center_button))
        self.right_button.clicked.connect(lambda: ChangeSub(self, 2, self.right_button))

    def accept_settings(self):
#       --- Create objects ---
        self.regulations_scroll = QScrollArea(self.center_widget)
        self.regulations_widget = QWidget(self.regulations_scroll)
        self.regulations_layout = QGridLayout(self.regulations_widget)
        self.regulations_label = QLabel(self.regulations_widget)
#       --- Call functions ---
        accept_settings_ui(self)
        accept_settings_reload_style(self)
        accept_settings_retranslate(self)
#       --- Connect functions ---
