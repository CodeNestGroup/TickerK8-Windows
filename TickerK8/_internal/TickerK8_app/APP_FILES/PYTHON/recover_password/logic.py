""" Import PyQt5 Widgets line edit """
from PyQt5.QtWidgets import QLineEdit
#######################################################################################################################
""" Show hide password """
def show_hide_password(self):
    _l = self.global_config['__language__']
    _t = self.recover_password_translate['recover_password_password_show_button']
    if self.recover_password_password_lineedit.echoMode() == QLineEdit.Normal:
        self.recover_password_password_lineedit.setEchoMode(QLineEdit.Password)
        self.recover_password_password_show_button.setText(_t[_l][1])
    else:
        self.recover_password_password_lineedit.setEchoMode(QLineEdit.Normal)
        self.recover_password_password_show_button.setText(_t[_l][0])
#______________________________________________________________________________________________________________________
""" Show hide confirm password """
def show_hide_confirm_password(self):
    _l = self.global_config['__language__']
    _t = self.recover_password_translate['recover_password_confirm_password_show_button']
    if self.recover_password_confirm_password_lineedit.echoMode() == QLineEdit.Normal:
        self.recover_password_confirm_password_lineedit.setEchoMode(QLineEdit.Password)
        self.recover_password_confirm_password_show_button.setText(_t[_l][1])
    else:
        self.recover_password_confirm_password_lineedit.setEchoMode(QLineEdit.Normal)
        self.recover_password_confirm_password_show_button.setText(_t[_l][0])
#######################################################################################################################