#
# Import
#

import mysql.connector
import json
import os
#-----------------------------------------------------------------------------------------------------------------------

#
# Login
#

# Try Login
def login(self):
    _json_file = json.load(open(os.getcwd() + '/TickerK8_app/app_files/JSON/CONFIG/_00_main_config.json'))
    _connect = mysql.connector.connect(
        host=_json_file['__SQL__']['_host_'],
        user=_json_file['__SQL__']['_user_'],
        password=_json_file['__SQL__']['_password_'],
        database=_json_file['__SQL__']['_database_']
    )
    _cursor = _connect.cursor()
    _cursor.execute(f'SELECT name, country FROM users WHERE emial like "{self.login_login_lineedit.text()}" and password like "{self.login_password_lineedit.text()}"'
                    f' or phone like "{self.login_login_lineedit.text()}" and password like "{self.login_password_lineedit.text()}"'
                    f' or name like "{self.login_login_lineedit.text()}" and password like "{self.login_password_lineedit.text()}";')

    _login_date = _cursor.fetchall()
    if _login_date:
        success_login(self)
    else:
       failed_login(self)

    _connect.close()
#-----------------------------------------------------------------------------------------------------------------------

# Success Login
def success_login(self):
    _json_file = json.load(open(os.getcwd() + '/TickerK8_app/app_files/JSON/CONFIG/_00_main_config.json'))
    self.deleteLater()
    self.window_widget.showFullScreen()
    self.window_widget.create_destroy_app_widget()


# Failed Login
def failed_login(self):
    self.login_login_lineedit.setStyleSheet('border-color: #c43025;')
    self.login_login_lineedit.setPlaceholderText('WRONG!!!')
    self.login_password_lineedit.setStyleSheet('border-color: #c43025;')
    self.login_password_lineedit.setPlaceholderText('WRONG!!!')


#-----------------------------------------------------------------------------------------------------------------------

#
# Register
#

# Try Register
def register(self):
    _json_file = json.load(open(os.getcwd() + '/TickerK8_app/app_files/JSON/CONFIG/_00_main_config.json'))
    _connect = mysql.connector.connect(
        host=_json_file['__SQL__']['_host_'],
        user = _json_file['__SQL__']['_user_'],
        password = _json_file['__SQL__']['_password_'],
        database = _json_file['__SQL__']['_database_']
    )
    _name = self.register_name_lineedit.text()
    _emial = None
    _phone = '+48'+self.register_phonenumber_lineedit.text()
    _country = 'poland'
    _password = None

    if self.register_emial_lineedit.text() == self.register_emial_confirm_lineedit.text():
        _emial = self.register_emial_lineedit.text()

    if self.register_password_lineedit.text() == self.register_password_confirm_lineedit.text():
        _password = self.register_password_lineedit.text()


    _connect.cursor().execute(f'INSERT INTO users (name, emial, phone, country, password) VALUES ("{_name}", "{_emial}", "{_phone}", "{_country}", "{_password}")')
    _connect.commit()
    _connect.close()

    show_hide_login_register_widget(self)

#-----------------------------------------------------------------------------------------------------------------------

#
# Show, Hide Widgets
#

def show_hide_login_register_widget(self):
    if self.register_widget.isHidden():
        self.register_widget.show()
        self.login_widget.hide()
    elif self.login_widget.isHidden():
        self.register_widget.hide()
        self.login_widget.show()
    else:
        print('Error with open login or register widget')
#-----------------------------------------------------------------------------------------------------------------------
