#
# Import
#

from PyQt5.QtWidgets import QLineEdit
#-----------------------------------------------------------------------------------------------------------------------

#
# set lineedit
#
def login_setLineEdit(self):
    #
    # Main Widget
    #

#-----------------------------------------------------------------------------------------------------------------------

    #
    # Login Widget
    #

    self.login_login_lineedit.setPlaceholderText('LOGIN')
    self.login_password_lineedit.setPlaceholderText('PASSWORD')
    self.login_password_lineedit.setEchoMode(QLineEdit.Password)

#-----------------------------------------------------------------------------------------------------------------------

    #
    # Register Widget
    #

    self.register_name_lineedit.setPlaceholderText('user name')
    self.register_emial_lineedit.setPlaceholderText('email')
    self.register_emial_confirm_lineedit.setPlaceholderText('email confirm')
    self.register_phonenumber_lineedit.setPlaceholderText('phone number')
    self.register_password_lineedit.setPlaceholderText('password')
    self.register_password_lineedit.setEchoMode(QLineEdit.Password)
    self.register_password_confirm_lineedit.setPlaceholderText('password confirm')
    self.register_password_confirm_lineedit.setEchoMode(QLineEdit.Password)
#-----------------------------------------------------------------------------------------------------------------------
