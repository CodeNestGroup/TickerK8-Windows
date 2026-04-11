""" Import packages """
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QGridLayout,
    QVBoxLayout
)
""" Import changelog modules """
from .ui import *
from .logic import *
""" Import custom modules """
from soundbutton.structure import QPushButton_sound
from ResourcePath.Structure import ResourcePath
#______________________________________________________________________________________________________________________

class Changelog_widget(QWidget):
    def __init__(self, parent, data):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = ResourcePath(3)
        if data == '':
            data = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/changelog.json', 'r', encoding='utf-8'))
        self.changelog_data = data
        """ Create objects """
        self.layout = QGridLayout(self)
        self.title_label = QLabel(self)
        self.scroll = QScrollArea(self)
        self.update_widget = QWidget(self.scroll)
        self.update_layout = QVBoxLayout(self.update_widget)
        self.update_title_label = QLabel(self.update_widget)
        self.update_date_label = QLabel(self.update_widget)
        self.update_text_label = QLabel(self.update_widget)
        self.exit_button = QPushButton_sound(self)
        """ Call functions """
        changelog_ui(self)
        changelog_reload_style(self)
        changelog_retranslate(self)
        """ Connect functions  """
#______________________________________________________________________________________________________________________