import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#
# Login
#

def open_close_offline_login(self, path):
    self.Login_offline_password_widget.setGeometry(QRect(0, 0, self.window.size().width(), self.window.size().height()))
    if self.Login_offline_password_widget.isHidden():
        self.Login_offline_password_widget.setHidden(False)
        self.Login_offline_password_line.setText("")
        self.Login_offline_password_line.setPlaceholderText("Offline Password")
    else:
        self.Login_offline_password_widget.setHidden(True)
        self.Login_offline_password_line.setText("")
        self.Login_offline_password_widget.setHidden(True)
    self.user_path = path
    buttons_sound()
