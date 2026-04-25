#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QScrollArea,
    QGridLayout,
    QVBoxLayout
)
from PySide6.QtCore import (
    Qt,
    QThread,
    QTimer
)
from .Ui import *
from .Logic import *
#   --- Import backend ---
from ..Ping.Logic import PingO


#   --- UpdateW ---

class UpdateW(QWidget):
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
        self.UpdateChangelogOpenF = parent.UpdateChangelogOpen
        self.UpdateSettingsOpenF = parent.UpdateSettingsOpen
#           --- Set Class varaibles ---
        self.PingT = None
        self.LastPing = False
        self.ChangelogDotsT = None
        self.GetReleasesT = None
#           --- Set Class Threads ---
        self.PingT = QThread(self)
        self.PingO = PingO()
        self.PingO.moveToThread(self.PingT)
        self.PingT.started.connect(self.PingO.run)
        self.PingO.Status.connect(self.PingHandler)
        self.PingT.start()
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.ChangelogW = None
        self.ChangelogS = None
        self.SettingsB = QPushButton(self)
        self.InstagramB = QPushButton(self)
        self.GithubB = QPushButton(self)
        self.DiscordB = QPushButton(self)
        self.FuncB = None
        self.InfoL = None
#           --- Call functions ---
        UpdateUi(self)
        UpadateReloadStyle(self)
#        --- Connect functions ---
        self.SettingsB.clicked.connect(lambda: UpdateSettingsOpenHandler(self))
        self.InstagramB.clicked.connect(lambda: OpenLink('https://www.instagram.com/codenestgroup/'))
        self.GithubB.clicked.connect(lambda: OpenLink('https://github.com/CodeNestGroup'))
        self.DiscordB.clicked.connect(lambda: OpenLink('https://discord.gg/twZ3SNcC'))

    def PingHandler(self, Status):
        if Status and self.LastPing:
            self.LastPing = True
        elif Status and not self.LastPing:
            self.ChangelogLoading()
            self.LastPing = True
        else:
            self.ChangelogNoConnection()
            self.LastPing = False

    def ChangelogReset(self):
        if self.ChangelogW:
            try:
                self.ChangelogW.deleteLater()
            except:
                pass
            self.ChangelogW = None
        if self.ChangelogS:
            try:
                self.ChangelogS.deleteLater()
            except:
                pass
            self.ChangelogS = None

    def ChangelogNoConnection(self):
        self.ChangelogReset()
#           --- Create objects ---
        self.ChangelogW = QWidget(self)
        self.ChangelogL = QGridLayout(self.ChangelogW)
        self.ChangelogIconL = QLabel(self.ChangelogW)
        self.ChangelogMessageL = QLabel(self.ChangelogW)
#           --- Call functions ---
        ChangelogNoConnectionUi(self)
        ChangelogNoConnectionReloadStyle(self)
        ChangelogNoConnectionRetranslate(self)

    def ChangelogLoading(self):
        self.ChangelogReset()
#           --- Create objects ---
        self.ChangelogW = QWidget(self)
        self.ChangelogL = QGridLayout(self.ChangelogW)
        self.ChangelogIconL = QLabel(self.ChangelogW)
        self.ChangelogMessageL = QLabel(self.ChangelogW)
        self.ChaneglogDotsL = QLabel(self.ChangelogW)
        self.ChangelogDotsT = QTimer()
        self.GetReleasesT = GetReleasesT()
        self.GetReleasesT.setObjectName('111')
#           --- Call functions ---
        ChangelogLoadingUi(self)
        ChangelogLoadingRetranslate(self)
#           --- Connect functions ---
        self.ChangelogDotsT.timeout.connect(lambda: DotsUpdate(self))
        self.ChangelogDotsT.start(500)
        self.GetReleasesT.List.connect(lambda r: self.ChangelogConnection(r))
        self.GetReleasesT.Finished.connect(lambda: CloseGetReleasesThread(self))
        self.GetReleasesT.start()

    def ChangelogConnection(self, r):
        self.ChangelogReset()
#           --- Create objects ---
        self.ChangelogS = QScrollArea(self)
        self.ChangelogW = QWidget(self.ChangelogS)
        self.ChangelogL = QVBoxLayout(self.ChangelogW)
#           --- Call functions ---
        ChangelogConnctionUi(self)
        ChangelogConnectionSetup(self, r)
