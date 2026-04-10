""" Import packages """
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QLabel, 
    QComboBox,
    QScrollArea,
    QGridLayout,
    QVBoxLayout
)
from PyQt5.QtCore import (
    pyqtSignal
)
""" Import settings modules """
from .ui import *
from .logic import *
""" Import button modules """
from soundbutton.structure import QPushButton_sound
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Settings_widget(QWidget):
    update_created = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = ResourcePath(2)
        """ Create objects """
        self.layout = QGridLayout(self)
        self.menu_scroll = QScrollArea(self)
        self.menu_scroll_widget = QWidget(self.menu_scroll)
        self.menu_scroll_layout = QVBoxLayout(self.menu_scroll_widget)
        self.menu_theme_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_sound_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_update_button = QPushButton_sound(self.menu_scroll_widget)
        self.menu_language_button = QPushButton_sound(self.menu_scroll_widget)
        self.exit_button = QPushButton_sound(self.menu_scroll)
        self.sub_menu_scroll = None
        """ Call functions """
        settings_ui(self)
        settings_reload_style(self)
        settings_retranslate(self)
        self.sub_menu_open(self.theme_widget_open)
        """ Connect functions """
        self.menu_theme_button.clicked.connect(lambda: self.sub_menu_open(self.theme_widget_open))
        self.menu_sound_button.clicked.connect(lambda: self.sub_menu_open(self.sound_widget_open))
        self.menu_update_button.clicked.connect(lambda: self.sub_menu_open(self.update_widget_open))
        self.menu_language_button.clicked.connect(lambda: self.sub_menu_open(self.language_widget_open))

    def sub_menu_open(self, open_func):
        if self.sub_menu_scroll:
            self.sub_menu_scroll.deleteLater()
        """ Create objects """
        self.sub_menu_scroll = QScrollArea(self)
        self.sub_menu_widget = QWidget(self.sub_menu_scroll)
        self.sub_menu_layout = QGridLayout(self.sub_menu_widget)
        self.title_label = QLabel(self.sub_menu_widget)
        """ Call functions """
        sub_menu_ui(self)
        open_func()
    
    def theme_widget_open(self):
        """ Create objects """
        self.day_night_label = QLabel(self.sub_menu_widget)
        self.day_night_button = QPushButton_sound(self.sub_menu_widget)
        self.list_label = QLabel(self.sub_menu_widget)
        self.list_combobox = QComboBox(self.sub_menu_widget)
        self.list_combobox.addItem("Vintage Elegance Light")
        self.list_combobox.addItem("Vintage Elegance Dark")
        """ Call functions """
        theme_ui(self)
        theme_retranslate(self)
        """ Connect functions """
        self.day_night_button.clicked.connect(lambda: change_d_n(self))
        self.list_combobox.currentIndexChanged.connect(lambda: change_theme(self))

    def sound_widget_open(self):
        """ Create objects """
        self.button_label = QLabel(self.sub_menu_widget)
        self.button_button = QPushButton_sound(self.sub_menu_widget)
        """ Call functions """
        sound_ui(self)
        sound_retranslate(self)
        """ Connect functions """
        self.button_button.clicked.connect(lambda: change_sound_d_e(self, 'button'))

    def update_widget_open(self):
        """ Create objects """
        self.version_heading1_label = QLabel(self.sub_menu_widget)
        self.version_desc_label = QLabel(self.sub_menu_widget)
        self.version_desc_value_label = QLabel(self.sub_menu_widget)
        self.version_changelog_label = QLabel(self.sub_menu_widget)
        self.version_changelog_button = QPushButton_sound(self.sub_menu_widget)
        self.advanced_heading1_label = QLabel(self.sub_menu_widget)
        self.advanced_capacity_label = QLabel(self.sub_menu_widget)
        self.advanced_capacity_combobox = QComboBox(self.sub_menu_widget)
        self.advanced_capacity_combobox.addItem("500 KB/s")
        self.advanced_capacity_combobox.addItem("1000KB/s")
        self.advanced_capacity_combobox.addItem("2000KB/s")
        self.advanced_capacity_combobox.addItem("5000KB/s")
        self.advanced_capacity_combobox.addItem("Unlimited")
        """ Call functions """
        update_ui(self)
        update_retranslate(self)
        """ Connect functions """
        self.advanced_capacity_combobox.currentIndexChanged.connect(lambda: change_capacity(self))
        self.update_created.emit()

    def language_widget_open(self):
        """ Create objects """
        self.type_label = QLabel(self.sub_menu_widget)
        self.type_combobox = QComboBox(self.sub_menu_widget)
        self.type_combobox.addItem("English / English")
        self.type_combobox.addItem("Polski / Polish ")
        """ Call functions """
        language_ui(self)
        language_retranslate(self)
        """ Connect functions """
        self.type_combobox.currentIndexChanged.connect(lambda: change_language(self))
#______________________________________________________________________________________________________________________
