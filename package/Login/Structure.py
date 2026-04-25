#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout
        )
from PySide6.QtCore import (
        Qt,
        QTimer
        )
#   --- Import Login modules ---
from .Ui import *
from .Logic import *


#   --- LoginW  ---

class LoginW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.Theme = parent.ConfigOffline['theme']
        self.Language = parent.ConfigOffline['language']
#           --- Set Class varaibles ---
        self.Background = json.load(open(self.Path+'/assets/JSON/BackgroundConf.json', 'r', encoding='utf-8'))
        self.LoginWelcomeTranslate = json.load(open(self.Path+'/assets/JSON/LoginWelcomeTranslate.json', 'r', encoding='utf-8'))
        self.IndexChanged = -10
#           --- Get functions from parent [ core ] ---
        self.CheckLoginF = parent.Database.LoginByName
        self.UpdateLastLoginF = parent.Database.UpdateLastLogin
        self.LoginConfigurationOpenF = parent.LoginConfigurationOpen
        self.RegisterOpenF = parent.RegisterOpen
        self.MainOpenF = parent.MainOpen
        self.SetLoggedUserIdF = parent.SetLoggedUserId
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.LoginL = QLineEdit(self)
        self.PasswordL = QLineEdit(self)
        self.LoginB = QPushButton(self)
        self.RegisterB = QPushButton(self)
        self.WelcomeTitleL = QLabel(self)
        self.WelcomeSubL = QLabel(self)
        self.WelcomeIconL = QLabel(self)
        self.Timer = QTimer(self)
#           --- Call functions ---
        LoginUi(self)
        LoginReloadStyle(self)
        LoginRetranslate(self)
        BackgroundPainter(self)
        self.Timer.timeout.connect(lambda: BackgroundPainter(self))
        self.Timer.start(1)
#           --- Connect functions ---
        self.LoginL.textChanged.connect(lambda: ResetStyle(self))
        self.PasswordL.textChanged.connect(lambda: ResetStyle(self))
        self.LoginB.clicked.connect(lambda: LoginController(self))
        self.RegisterB.clicked.connect(self.RegisterOpenF)
