""" Import packages """
import pathlib
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout
        )
from PyQt5.QtCore import (
        Qt,
        QTimer,
        pyqtSignal
        )
""" Import login modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Login_widget(QWidget):
    correct_login = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
        self.login_translate = json.load(open(self.main_path+'/CONFIG/login/translate.json', 'r'))
        self.login_conf = json.load(open(self.main_path+'/CONFIG/login/background_conf.json', 'r'))
        self.index_changed = -10
        """ Create objects """
        self.login_layout = QGridLayout(self)
        self.login_login_lineedit = QLineEdit(self)
        self.login_password_lineedit = QLineEdit(self)
        self.login_login_button = QPushButton(self)
        self.login_register_button = QPushButton(self)
        self.login_welcome_title_label = QLabel(self)
        self.login_welcome_sub_label = QLabel(self)
        self.login_welcome_icon_label = QLabel(self)
        self.timer = QTimer(self)
        """ Call functions """
        login_ui(self)
        login_reload_style(self)
        login_retranslate(self)
        login_widget_background_painter(self)
        self.login_widget_background = lambda: login_widget_background_painter(self)
        self.timer.timeout.connect(self.login_widget_background)
        self.timer.start(1)
        """ Connect functions """
        self.login_login_button.clicked.connect(lambda: sign_in_controller(self))
        self.login_login_lineedit.textChanged.connect(lambda: reset_style(self))
        self.login_password_lineedit.textChanged.connect(lambda: reset_style(self))
#______________________________________________________________________________________________________________________
