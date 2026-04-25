#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QGridLayout,
    QVBoxLayout
)
#   --- Import UpdateChangelog modules ---
from .Ui import *
from .Logic import *


#   --- UpdateChangelogW ---

class UpdateChangelogW(QWidget):
    def __init__(self, parent, data=None):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.Theme = parent.ConfigOffline['theme']
        self.Language = parent.ConfigOffline['language']
        if not data:
            data = json.load(open(self.Path+'/assets/JSON/Changelog.json', 'r', encoding='utf-8'))
        self.ChangelogData = data
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.TitleL = QLabel(self)
        self.ChangelogS = QScrollArea(self)
        self.ChangelogW = QWidget(self.ChangelogS)
        self.ChangelogL = QVBoxLayout(self.ChangelogW)
        self.ChangelogTitleL = QLabel(self.ChangelogW)
        self.ChangelogDateL = QLabel(self.ChangelogW)
        self.ChangelogTextL = QLabel(self.ChangelogW)
        self.ExitB = QPushButton(self)
#           --- Call functions ---
        UpdateChangelogUi(self)
        UpdateChangelogReloadStyle(self)
        UpdateChangelogRetranslate(self)
#           --- Connect functions  ---
        self.ExitB.clicked.connect(parent.UpdateOpen)
