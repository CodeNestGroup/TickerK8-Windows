#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QLabel, 
    QPushButton,
    QComboBox,
    QScrollArea,
    QGridLayout,
    QVBoxLayout
)
from PySide6.QtCore import (
    Qt,
    Signal
)
#   --- Import UpdateSettings modules ---
from .Ui import *
from .Logic import *


#   --- UpdateSettingsW ---

class UpdateSettingsW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.ConfigOffline = parent.ConfigOffline
        self.Theme = parent.ConfigOffline['theme']
        self.Language = parent.ConfigOffline['language']
#           --- Get functions from parent [ core ] ---
        self.ReloadConfigOfflineF = parent.ReloadConfigOffline
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NaviS = QScrollArea(self)
        self.NaviW = QWidget(self.NaviS)
        self.NaviL = QVBoxLayout(self.NaviW)
        self.NaviStyleB = QPushButton(self.NaviW)
        self.NaviUpdateB = QPushButton(self.NaviW)
        self.NaviLanguageB = QPushButton(self.NaviW)
        self.NaviExitB  = QPushButton(self)
        self.PanelS = None
#           --- Call functions ---
        UpdateSettingsUi(self)
        UpdateSettingsReloadStyle(self)
        UpdateSettingsRetranslate(self)
#           --- Connect  functions ---
        self.NaviStyleB.clicked.connect(self.StylePage)
        self.NaviUpdateB.clicked.connect(self.UpdatePage)
        self.NaviLanguageB.clicked.connect(self.LanguagePage)
        self.NaviExitB.clicked.connect(lambda: SaveConfig(self))
        self.NaviExitB.clicked.connect(parent.UpdateOpen)

    def ResetPage(self):
        if self.PanelS:
            self.PanelS.deleteLater()
            self.PanelS = None
    
    def StylePage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelS)
        self.PanelL = QGridLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.StyleThemeDayNightNameL = QLabel(self.PanelW)
        self.StyleThemeDayNightValueB = QPushButton(self.PanelW)
        self.StyleThemeThemesNameL = QLabel(self.PanelW)
        self.StyleThemeThemesValueC = QComboBox(self.PanelW)
#           --- Call functions ---
        StyleUi(self)
        StyleRetranslate(self)
#           --- Connect  functions ---
        self.StyleThemeDayNightValueB.clicked.connect(lambda:ChangeDayNight(self))
        self.StyleThemeThemesValueC.currentIndexChanged.connect(lambda: ChangeTheme(self))

    def UpdatePage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelS)
        self.PanelL = QGridLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.UpdateDescriptionNameL = QLabel(self.PanelW)
        self.UpdateDescriptionValueL = QLabel(self.PanelW)
        self.UpdateChangelogNameL = QLabel(self.PanelW)
        self.UpdateChangelogValueS = QScrollArea(self.PanelW)
        self.UpdateChangelogValueW = QWidget(self.UpdateChangelogValueS)
        self.UpdateChangelogValueL = QGridLayout(self.UpdateChangelogValueW)
        self.UpdateChangelogValueLA = QLabel(self.UpdateChangelogValueW)
#           --- Call functions ---
        UpdateUi(self)
        UpdateRetranslate(self)
#           --- Connect  functions ---  

    def LanguagePage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelS)
        self.PanelL = QGridLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.LanguageNameL = QLabel(self.PanelW)
        self.LanguageValueC = QComboBox(self.PanelW)
#           --- Call functions ---
        LanguageUi(self)
        LanguageRetranslate(self)
#           --- Connect functions ---
        self.LanguageValueC.currentIndexChanged.connect(lambda: ChangeLanguage(self))
        