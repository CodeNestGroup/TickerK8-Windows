""" Import packages """
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QGridLayout,
    QVBoxLayout
)
from PyQt5.QtCore import (
    pyqtSignal
)
""" Import main changelog modules """
from .ui import *
from .logic import *
""" Import custom modules """
from soundbutton.structure import QPushButton_sound
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Changelog_widget(QWidget):
    connection_signal = pyqtSignal()
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        """ Set paths, file name """
        self.main_path = ResourcePath(2)
        """ Create objects """
        self.release_data = []
        self.releases_button_list = []
        self.layout = QVBoxLayout(self)
        self.scroll = None
        self.widget = None
        self.timer = None
        """ Call functions """
        changelog_ui(self)
        changelog_reload_style(self)
        self.no_connection()
        """ Connect functions """

    def reset(self):
        self.release_data = []
        self.releases_button_list = []
        if self.widget:
            self.widget.deleteLater()
            self.widget = None 
        if self.scroll:
            self.scroll.deleteLater()
            self.scroll = None 
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None 

    def no_connection(self):
        self.reset()
        """ Create objects """
        self.widget = QWidget(self)
        self.widget_layout = QGridLayout(self.widget)
        self.icon_label = QLabel(self.widget)
        self.message_label = QLabel(self.widget)
        """ Call functions """
        no_connection_ui(self)
        no_connection_reload_style(self)
        no_connection_retranslate(self)
        """ Connect functions """

    def loading(self):
        self.reset()
        """ Create objects """
        self.widget = QWidget(self)
        self.widget_layout = QGridLayout(self.widget)
        self.icon_label = QLabel(self.widget)
        self.message_label = QLabel(self.widget)
        self.dots_label = QLabel(self.widget)
        """ Call functions """
        loading_ui(self)
        loading_reload_style(self)
        loading_retranslate(self)
        loading_thread(self)

    def connection(self, release_data):
        self.reset()
        self.release_data = release_data
        """ Create objects """
        self.scroll = QScrollArea(self)
        self.widget = QWidget(self.scroll)
        self.widget_layout = QVBoxLayout(self.widget)
        for button in range(len(self.release_data)):
            button = QPushButton_sound(self.widget)
            self.releases_button_list.append(button)
        """ Call functions """
        connection_ui(self)
        connection_retranslate(self)
        self.connection_signal.emit()
        """ Connect functions """
#______________________________________________________________________________________________________________________
