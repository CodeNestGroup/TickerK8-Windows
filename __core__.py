#   --- Import ---
import sys
import json

#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QMainWindow
    )
from PySide6.QtCore import (
    QRect,
    QThread
    )
from PySide6.QtGui import (
    QGuiApplication,
    QFontDatabase,
    QFont
    )
#   --- Import __core__ modules ---
from package.Update.Structure import UpdateW
from package.UpdateSettings.Structure import UpdateSettingsW
from package.UpdateChangelog.Structure import UpdateChangelogW
from package.Login.Structure import LoginW
from package.Register.Structure import RegisterW
from package.LoginConfig.Structure import LoginConfigurationW
from package.Main.Structure import MainW
from package.Settings.Structure import SettingsW

#   --- Import backend ---
from package.Path.Structure import Path
from package.Db.Connection import Database


#   --- AppWindow ---

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
#           --- AppWindowUi ---
        self.OpenedW = None
        self.setObjectName('AppWindow')
        self.Layout = QVBoxLayout(self)
        self.Layout.setSpacing(0)
        self.Layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.Layout)
#           --- Get app data ---
        self.Path = Path()
        self.Geometry = self.screen().availableGeometry()
        self.LoggedUserId = None
        self.ConfigOffline = None
#           --- App functions  ---
        self.Database = Database(self)
        self.ReloadConfigOffline()

#   --- Func for opens windows ---
    def ReloadConfigOffline(self):
        self.ConfigOffline = json.load(open(f'{self.Path}/assets/JSON/ConfigOffline.json', 'r', encoding='utf-8'))

    def Reset(self):
        if self.OpenedW:
            self.OpenedW.deleteLater()
            self.OpenedW = None

    def UpdateOpen(self):
        self.Reset()
        self.OpenedW = UpdateW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)
        self.ConfigOffline = json.load(open(f'{self.Path}/assets/JSON/ConfigOffline.json', 'r', encoding='utf-8'))

    def UpdateSettingsOpen(self):
        self.Reset()
        self.OpenedW = UpdateSettingsW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)

    def UpdateChangelogOpen(self, d):
        self.Reset()
        self.OpenedW = UpdateChangelogW(self, d)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//4, self.Geometry.width()//2, self.Geometry.height()//2
        self.setGeometry(x, y, w, h)

    def LoginOpen(self):
        self.Reset()
        self.LoggedUserId = None
        self.OpenedW = LoginW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//12, self.Geometry.width()//2, self.Geometry.height()//1.25
        self.setGeometry(x, y, w, h)

    def RegisterOpen(self):
        self.Reset()
        self.OpenedW = RegisterW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//12, self.Geometry.width()//2, self.Geometry.height()//1.25
        self.setGeometry(x, y, w, h)
        
    def LoginConfigurationOpen(self):
        self.Reset()
        self.OpenedW = LoginConfigurationW(self)
        self.Layout.addWidget(self.OpenedW)
        x, y, w, h = self.Geometry.width()//4, self.Geometry.height()//12, self.Geometry.width()//2, self.Geometry.height()//1.25
        self.setGeometry(x, y, w, h)

    def MainOpen(self):
        self.Reset()
        self.OpenedW = MainW(self)
        self.Layout.addWidget(self.OpenedW)
        self.showMaximized()
        x, y, w, h = self.Geometry.width(), self.Geometry.height(), self.Geometry.width(), self.Geometry.height()
        self.setGeometry(x, y, w, h)

    def SettingsOpen(self):
        self.Reset()
        self.OpenedW = SettingsW(self)
        self.Layout.addWidget(self.OpenedW)
        self.showMaximized()
        x, y, w, h = self.Geometry.width(), self.Geometry.height(), self.Geometry.width(), self.Geometry.height()
        self.setGeometry(x, y, w, h)

    def SetLoggedUserId(self, i):
        self.LoggedUserId = i
        self.Database.LoggedUserId = self.LoggedUserId
            
def SetFont():
    font_id = QFontDatabase.addApplicationFont(str(Path())+'/assets/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(SetFont())
    AppW = AppWindow()
    AppW.show()
    AppW.UpdateOpen()
    sys.exit(application.exec())
    