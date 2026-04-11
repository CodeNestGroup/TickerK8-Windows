""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QGridLayout
        )
from PyQt5.QtCore import (
        Qt,
        pyqtSignal
        )
""" Import register modules """
from .ui import *
from .logic import *
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Register_widget(QWidget):
    correct_data = pyqtSignal(tuple)
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        """ Set paths, file name"""
        self.main_path = ResourcePath(5)
        """ Create objects """
        self.register_layout = QGridLayout(self)
        self.register_name_subtitle_label = QLabel(self)
        self.register_name_lineedit = QLineEdit(self)
        self.register_name_label = QLabel(self)
        self.register_emial_subtitle_label = QLabel(self)
        self.register_emial_lineedit = QLineEdit(self)
        self.register_emial_confirm_lineedit = QLineEdit(self)
        self.register_email_label = QLabel(self)
        self.register_phonenumber_subtitle_label = QLabel(self)
        self.register_phonenumber_combobox = QComboBox(self)
        self.register_phonenumber_lineedit = QLineEdit(self)
        self.register_country_subtitle_label = QLabel(self)
        self.register_country_combobox = QComboBox(self)
        self.register_password_subtitle_label = QLabel(self)
        self.register_password_lineedit = QLineEdit(self)
        self.register_password_requirements_label = QLabel(self)
        self.register_password_show_button = QPushButton(self)
        self.register_password_confirm_lineedit = QLineEdit(self)
        self.register_register_button = QPushButton(self)
        self.register_exit_button = QPushButton(self)
        """ Call functions """
        register_ui(self)
        register_reload_style(self)
        register_retranslate(self)
        """ Connect local functions """
        self.user_exists = lambda: user_exists(self)
        self.email_exists = lambda: email_exists(self)
        self.phone_exists = lambda: phone_exists(self)
        self.register_name_lineedit.textChanged.connect(lambda: reset_name(self))
        self.register_emial_lineedit.textChanged.connect(lambda: reset_email(self))
        self.register_emial_confirm_lineedit.textChanged.connect(lambda: reset_confirm_email(self))
        self.register_phonenumber_lineedit.textChanged.connect(lambda: reset_phone(self))
        self.register_password_lineedit.textChanged.connect(lambda: reset_password(self))
        self.register_password_confirm_lineedit.textChanged.connect(lambda: reset_confirm_password(self))
        self.register_register_button.clicked.connect(lambda: register_controller(self))
        self.register_password_show_button.clicked.connect(lambda: show_hide_password(self))
#______________________________________________________________________________________________________________________
