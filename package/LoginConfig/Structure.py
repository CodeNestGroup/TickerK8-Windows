#   --- Import ---
import pathlib
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox,
    QGridLayout,
        )
from PySide6.QtCore import (
        Qt
        )
#   --- Import LoginConfiguration ---
from .Ui import *
from .Logic import *


#   --- LoginConfiguration ---

class LoginConfigurationW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
#           --- Set ---        
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.Theme = parent.ConfigOffline['theme']
        self.Language = parent.ConfigOffline['language']
#           --- Get functions from parent [ core ] ---
        self.LoginOpenF = parent.LoginOpen
        self.LoginConfigurationF = parent.Database.LoginConfiguration
#           --- Set Class varaibles ---
        self.StepIndex = 0
#       --- Create objects ---
        self.Layout = QGridLayout(self)
        self.TitleL = QLabel(self)
        self.InfoL = QLabel(self)
        self.CenterW = None
        self.LeftB = QPushButton(self)
        self.ExitB= QPushButton(self)
        self.RightB = QPushButton(self)
        self.AcceptB = QPushButton(self)
        self.NaviL = QLabel(self)
#       --- Call functions ---
        LoginConfigurationUi(self)
        LoginConfigurationReloadStyle(self)
        LoginConfigurationRetranslate(self)
#       --- Connect functions ---
        self.LeftB.clicked.connect(lambda: ChangePage(self, -1))
        self.RightB.clicked.connect(lambda: ChangePage(self, 1))
        self.ExitB.clicked.connect(self.LoginOpenF)
        self.AcceptB.clicked.connect(lambda: LoginConfigurationController(self))
    
    def Reset(self):
        if self.CenterW:
            self.CenterW.deleteLater()
            self.CenterW = None 

    def AppConf(self):
        self.Reset()
#       --- Create objects ---
        self.CenterW = QWidget(self)
        self.CenterL = QGridLayout(self.CenterW)
        self.LanguageSubtitleL = QLabel(self.CenterW)
        self.LanguageC = QComboBox(self.CenterW)
        self.ThemeSubtitleL = QLabel(self.CenterW)
        self.ThemeC = QComboBox(self.CenterW)
#       --- Call functions ---
        AppConfUi(self)
        AppConfRetranslate(self)
#       --- Connect functions ---
        self.LanguageC.currentIndexChanged.connect(lambda: ChangeLanguage(self))
        self.LanguageC.currentIndexChanged.connect(lambda: AppConfRetranslate(self))
        self.ThemeC.currentIndexChanged.connect(lambda: ChangeTheme(self))
        self.ThemeC.currentIndexChanged.connect(lambda: LoginConfigurationReloadStyle(self))

    def SubConf(self):
        self.Reset()
#       --- Create objects ---
        self.CenterW = QWidget(self)
        self.CenterL = QGridLayout(self.CenterW)
        self.LeftB = QPushButton(self.CenterW)
        self.CenterB = QPushButton(self.CenterW)
        self.RightB = QPushButton(self.CenterW)
        self.CheckedB = None
#       --- Call functions ---
        SubConfUi(self)
        SubConfRetranslate(self)
#       --- Connect functions ---
        self.LeftB.clicked.connect(lambda: ChangeSub(self, 3, self.LeftB))
        self.CenterB.clicked.connect(lambda: ChangeSub(self, 1, self.CenterB))
        self.RightB.clicked.connect(lambda: ChangeSub(self, 2, self.RightB))

    def AcceptSettings(self):
        self.Reset()
#       --- Create objects ---
        self.CenterW = QWidget(self)
        self.CenterL = QGridLayout(self.CenterW)
        self.RegulationsS = QScrollArea(self.CenterW)
        self.RegulationsW = QWidget(self.RegulationsS)
        self.RegulationsL = QGridLayout(self.RegulationsW)
        self.RegulationsValueL = QLabel(self.RegulationsW)
#       --- Call functions ---
        AcceptSettingsUi(self)
        AcceptSettingsRetranslate(self)
#       --- Connect functions ---
