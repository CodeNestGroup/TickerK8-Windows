""" Import packages """
import json
import string
import mysql
""" Import PyQt5 packages"""
from PyQt5.QtWidgets import QLineEdit
#______________________________________________________________________________________________________________________

def show_hide_password(self):
    """ Variables """
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    _t = json.load(open(self.main_path+'/CONFIG/register/translate.json', 'r'))['register_password_show_button']
    """ Set hide or show """
    if self.register_password_lineedit.echoMode() == QLineEdit.Normal: 
        self.register_password_lineedit.setEchoMode(QLineEdit.Password) 
        self.register_password_show_button.setText(_t[_l][1])
    else:
        self.register_password_lineedit.setEchoMode(QLineEdit.Normal)
        self.register_password_show_button.setText(_t[_l][0])
#______________________________________________________________________________________________________________________

def register_controller(self):
    """ Variables """
    """ Texts """
    _t = json.load(open(self.main_path+'/CONFIG/register/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    """ Style """
    _wrong_data = 'border: 2px solid #c01414;'
    """ Data to insert """
    c_n = None # Correct name.
    c_e = None # Correct email.
    c_p = None # Correct phone number.
    c_c = None # Correct country.
    c_pass = None # Correct password.
    """ Database """
    connect = mysql.connector.connect(
        host = "localhost",
        user = "register_user",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()
    if self.register_name_lineedit.text() != '':
        _name_line = self.register_name_lineedit.text()
        cursor.execute('SELECT id FROM users WHERE name=%s;', (_name_line,))
        c_n_e = cursor.fetchall() 
        if c_n_e == []:
            c_n = _name_line
        else:
            c_n = None
            self.register_name_label.setHidden(False)
            self.register_name_label.setText(f'{_t['register_name_label'][1][_l]}')
            self.register_name_lineedit.setStyleSheet(_wrong_data)
    else:
        c_n = None
        self.register_name_label.setHidden(False)
        self.register_name_label.setText(f'{_t['register_name_label'][0][_l]}')
        self.register_name_lineedit.setStyleSheet(_wrong_data)
    """ Check if emial exists"""
    if self.register_emial_lineedit.text() != '':
        _email_line = self.register_emial_lineedit.text()
        cursor.execute('SELECT id FROM users WHERE emial=%s;', (_email_line,))
        c_e_e = cursor.fetchall()
        if c_e_e == []: 
            if self.register_emial_confirm_lineedit.text() == _email_line:
                c_e = _email_line
            else:
                c_e = None
                self.register_email_label.setHidden(False)
                self.register_email_label.setText(f'{_t['register_email_label'][2][_l]}')
                self.register_emial_confirm_lineedit.setStyleSheet(_wrong_data)
        else:
            c_e = None
            self.register_email_label.setHidden(False)
            self.register_email_label.setText(f'{_t['register_email_label'][1][_l]}')
            self.register_emial_lineedit.setStyleSheet(_wrong_data)
            self.register_emial_confirm_lineedit.setStyleSheet(_wrong_data)
    else:
        c_e = None
        self.register_email_label.setHidden(False)
        self.register_email_label.setText(f'{_t['register_email_label'][0][_l]}')
        self.register_emial_lineedit.setStyleSheet(_wrong_data)
        self.register_emial_confirm_lineedit.setStyleSheet(_wrong_data)
    """ Check if phone correct """
    try:
        if self.register_phonenumber_lineedit.text() != '':
            int_nunber = int(self.register_phonenumber_lineedit.text())
            c_p = f'{self.register_phonenumber_combobox.currentText()}{int_nunber}'
    except:
        c_p = None
        self.register_phonenumber_lineedit.setText(f'{_t['register_phonenumber_lineedit_error'][_l]}')
        self.register_phonenumber_lineedit.setStyleSheet(_wrong_data)
    """ Country set """
    c_c = self.register_country_combobox.currentText()
    """ Check if password correct"""
    _password_confirm = self.register_password_confirm_lineedit.text()
    if len(_password_confirm) >= 8 and any(h.isupper() for h in _password_confirm) and any(h.isdigit() for h in _password_confirm) and any(h in string.punctuation for h in _password_confirm):
        if self.register_password_lineedit.text() == _password_confirm:
            c_pass = _password_confirm 
        else:
            c_pass = None
            self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][1][_l]}')
            self.register_password_confirm_lineedit.setStyleSheet(_wrong_data)
    else:
        c_pass = None
        self.register_password_lineedit.setStyleSheet('border: 2px solid #c01414;')
        self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][2][_l]}')
    """ Correct register call function """
    if c_n and c_e and c_p and c_c and c_pass:
        correct_register(self, c_n, c_e, c_p, c_c, c_pass)
    """ Close connection """
    cursor.close()
    connect.close()
#______________________________________________________________________________________________________________________

def correct_register(self, name, email, phone, country, password):
    """ Variables """
    _name = name
    _emial = email
    _phone = phone
    _country = country
    _password = password
    _t = json.load(open(self.main_path+'/CONFIG/register/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    """ Database """
    connect = mysql.connector.connect( 
        host = "localhost",
        user = "register_user",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()
    cursor.execute('INSERT INTO users (name, emial, phone, country, password) values(%s, %s, %s, %s, %s);', (_name, _emial, _phone, _country, _password))
    connect.commit()
    cursor.close()
    connect.close()
    """ Confirm cuccess"""
    self.register_name_lineedit.setDisabled(True)
    self.register_emial_lineedit.setDisabled(True)
    self.register_emial_confirm_lineedit.setDisabled(True)
    self.register_phonenumber_combobox.setDisabled(True)
    self.register_phonenumber_lineedit.setDisabled(True)
    self.register_country_combobox.setDisabled(True)
    self.register_password_lineedit.setDisabled(True)
    self.register_password_confirm_lineedit.setDisabled(True)
    self.register_register_button.setDisabled(True)
    self.register_register_button.setText(_t['register_register_button'][1][_l])
    self.register_register_button.setStyleSheet('background-color: #2e8317;')
#______________________________________________________________________________________________________________________

def reset_name(self):
    self.register_name_label.setHidden(True)
    self.register_name_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_email(self):
    self.register_email_label.setHidden(True)
    self.register_emial_lineedit.setStyleSheet('border: 0;')
    self.register_emial_confirm_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_confirm_email(self):
    self.register_email_label.setHidden(True) 
    self.register_emial_confirm_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_phone(self):
    self.register_phonenumber_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_password(self):
    _t = json.load(open(self.main_path+'/CONFIG/register/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][0][_l]}')
    self.register_password_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_confirm_password(self):
    _t = json.load(open(self.main_path+'/CONFIG/register/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.register_password_requirements_label.setText(f'{_t['register_password_requirements_label'][0][_l]}')
    self.register_password_confirm_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________
