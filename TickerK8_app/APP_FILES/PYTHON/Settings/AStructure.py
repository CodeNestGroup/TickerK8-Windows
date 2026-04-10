#   --- Import ---
import pathlib
import json
#   --- Import PyQt5 packages ---
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox, 
    QGridLayout,
    QVBoxLayout 
)
from PyQt5.QtCore import (
    Qt
)
#   --- Import settings modules ---
from .AUi import *
from .ALogic import *

#   --- Class ----
class SettingsW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = parent.main_path
        self.LoggedUserId = parent.logged_user_id
        self.GetUserConfig = parent.database.GetUserConfig
        self.Config = json.loads(self.GetUserConfig(self.LoggedUserId)[0])
        self.UserData = parent.database.GetUserData(self.LoggedUserId)[0]
        self.Theme = self.Config['theme']
        self.Language = self.Config['language']
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NaviS = QScrollArea(self)
        self.NaviW = QWidget(self.NaviS)
        self.NaviL = QVBoxLayout(self.NaviW)
        self.NaviUserB = QPushButton(self.NaviW)
        self.NaviStyleB = QPushButton(self.NaviW)
        self.NaviUpdateB = QPushButton(self.NaviW)
        self.NaviLanguageB = QPushButton(self.NaviW)
        self.NaviExitB  = QPushButton(self)
        self.PanelS = None
#           --- Call functions ---
        SettingsUi(self)
        SettingsReloadStyle(self)
        SettingsRetranslate(self)
#           --- Connect  functions ---
        self.NaviUserB.clicked.connect(self.UserPage)
        self.NaviStyleB.clicked.connect(self.StylePage)
        self.NaviUpdateB.clicked.connect(self.UpdatePage)
        self.NaviLanguageB.clicked.connect(self.LanguagePage)

    def ResetPage(self):
        if self.PanelS:
            self.PanelS.deleteLater()
            self.PanelS = None

    def UserPage(self):
        self.ResetPage()
        self.PanelS = QScrollArea(self)
        self.PanelW = QWidget(self.PanelS)
        self.PanelL = QGridLayout(self.PanelW)
        self.PanelTitleL = QLabel(self.PanelW)
        self.UserNameNameL = QLabel(self.PanelW)
        self.UserNameValueL = QLabel(self.PanelW)
        self.UserEmailNameL = QLabel(self.PanelW)
        self.UserEmailValueL = QLabel(self.PanelW)
        self.UserPhoneNameL = QLabel(self.PanelW)
        self.UserPhoneValueL = QLabel(self.PanelW)
        self.UserCountryNameL = QLabel(self.PanelW)
        self.UserCountryValueL = QLabel(self.PanelW)
        self.UserCreateDateNameL = QLabel(self.PanelW)
        self.UserCreateDateValueL = QLabel(self.PanelW)
#           --- Call functions ---
        UserUi(self)
        UserRetranslate(self)
#           --- Connect  functions ---

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
        