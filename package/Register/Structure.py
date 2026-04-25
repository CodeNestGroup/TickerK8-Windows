#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QGridLayout
        )
from PySide6.QtCore import (
        Qt,
        )
#   --- Import Register modules ---
from .Ui import *
from .Logic import *


#   --- RegisterW   ---

class RegisterW(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.Theme = parent.ConfigOffline['theme']
        self.Language = parent.ConfigOffline['language']
#           --- Get functions from parent [ core ] ---
        self.GetCountriesF = parent.Database.GetCountries
        self.GetPhonePrefixF = parent.Database.GetPhonePrefix
        self.RegisterUserF = parent.Database.RegisterUser
        self.LoginOpenF = parent.LoginOpen
#           --- Set Class varaibles ---
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.NameSubtitleL = QLabel(self)
        self.NameL = QLineEdit(self)
        self.NameInfoL = QLabel(self)
        self.EmialSubtitleL = QLabel(self)
        self.EmialL = QLineEdit(self)
        self.EmialConfirmL = QLineEdit(self)
        self.EmailInfoL = QLabel(self)
        self.PhonenumberSubtitleL = QLabel(self)
        self.PhonenumberC = QComboBox(self)
        self.PhonenumberL= QLineEdit(self)
        self.CountrySubtitleL = QLabel(self)
        self.CountryC = QComboBox(self)
        self.PasswordSubtitleL = QLabel(self)
        self.PasswordL = QLineEdit(self)
        self.PasswordRequirementsL = QLabel(self)
        self.PasswordShowB = QPushButton(self)
        self.PasswordConfirmL = QLineEdit(self)
        self.RegisterB = QPushButton(self)
        self.ExitB = QPushButton(self)
#           --- Call functions ---
        RegisterUi(self)
        RegisterReloadStyle(self)
        RegisterRetranslate(self)
#        --- Connect functions ---
        self.UserExists = lambda: UserExists(self)
        self.EmailExists = lambda: EmailExists(self)
        self.PhoneExists = lambda: PhoneExists(self)
        self.NameL.textChanged.connect(lambda: ResetName(self))
        self.EmialL.textChanged.connect(lambda: ResetEmail(self))
        self.EmialConfirmL.textChanged.connect(lambda: ResetConfirmEmail(self))
        self.PhonenumberL.textChanged.connect(lambda: ResetPhone(self))
        self.PasswordL.textChanged.connect(lambda: ResetPassword(self))
        self.PasswordConfirmL.textChanged.connect(lambda: ResetConfirmPassword(self))
        self.PasswordShowB.clicked.connect(lambda: ShowHidePassword(self))

        self.RegisterB.clicked.connect(lambda: RegisterController(self))
        self.ExitB.clicked.connect(self.LoginOpenF)
