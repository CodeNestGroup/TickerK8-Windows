""" Import packages """
import json
import string
""" Import PyQt5 packages"""
from PyQt5.QtWidgets import QLineEdit
#______________________________________________________________________________________________________________________
def show_hide_password(self):
    """ Variables """
    _l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    _t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))['register_password_show_button']
    """ Set hide or show """
    if self.register_password_lineedit.echoMode() == QLineEdit.Normal: 
        self.register_password_lineedit.setEchoMode(QLineEdit.Password) 
        self.register_password_show_button.setText(_t[_l][1])
    else:
        self.register_password_lineedit.setEchoMode(QLineEdit.Normal)
        self.register_password_show_button.setText(_t[_l][0])
#______________________________________________________________________________________________________________________

def register_controller(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    wrong_data = 'border: 2px solid #c01414;'
    name = None
    email = None
    email_confirm = None
    phone_prefix = None
    phone = None
    country = None
    password = None
    password_confirm = None

    name = self.register_name_lineedit.text()
    if name == '':
        name = None
        self.register_name_label.setHidden(False)
        self.register_name_label.setText(f'{t['register_name_label'][0][l]}')
        self.register_name_lineedit.setStyleSheet(wrong_data)
    
    email = self.register_emial_lineedit.text()
    email_confirm = self.register_emial_confirm_lineedit.text()
    if email != email_confirm:
        email = None
        email_confirm = None
        self.register_email_label.setHidden(False)
        self.register_email_label.setText(f'{t['register_email_label'][2][l]}')
        self.register_emial_confirm_lineedit.setStyleSheet(wrong_data)
    if email == '' or email_confirm == '':
        email = None
        email_confirm = None
        self.register_email_label.setHidden(False)
        self.register_email_label.setText(f'{t['register_email_label'][0][l]}')
        self.register_emial_lineedit.setStyleSheet(wrong_data)
        self.register_emial_confirm_lineedit.setStyleSheet(wrong_data)
    
    phone_prefix = self.register_phonenumber_combobox.currentText()
    if phone_prefix == '':
        phone_prefix = None

    phone = self.register_phonenumber_lineedit.text()
    if phone == '' or not phone.isdigit():
        phone = None
        self.register_phonenumber_lineedit.setText('')
        self.register_phonenumber_lineedit.setPlaceholderText(f'{t['register_phonenumber_lineedit'][2][l]}')
        self.register_phonenumber_lineedit.setStyleSheet(wrong_data)
    

    country = self.register_country_combobox.currentText()
    if country == '':
        country = None

    password = self.register_password_lineedit.text()
    password_confirm = self.register_password_confirm_lineedit.text()
    if len(password_confirm) < 8 and not any(h.isupper() for h in password_confirm) and not any(h.isdigit() for h in password_confirm) and not any(h in string.punctuation for h in password_confirm):
        password = None
        self.register_password_lineedit.setStyleSheet('border: 2px solid #c01414;')
        self.register_password_requirements_label.setText(f'{t['register_password_requirements_label'][2][l]}')
        self.register_password_lineedit.setStyleSheet(wrong_data)
    if password  != password_confirm:
        password = None
        self.register_password_requirements_label.setText(f'{t['register_password_requirements_label'][1][l]}')
        self.register_password_confirm_lineedit.setStyleSheet(wrong_data)
    
    if name and password and email and phone_prefix and phone and country:
        self.correct_data.emit((name, password, email, phone_prefix, phone, country))
#______________________________________________________________________________________________________________________


def user_exists(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_name_lineedit.setStyleSheet('border: 2px solid #c01414;')
    self.register_name_label.setText(t['register_name_label'][1][l])

def email_exists(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_emial_lineedit.setStyleSheet('border: 2px solid #c01414;')
    self.register_email_label.setText(t['register_email_label'][1][l])

def phone_exists(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_phonenumber_lineedit.setStyleSheet('border: 2px solid #c01414;')
    self.register_phonenumber_lineedit.setText('')
    self.register_phonenumber_lineedit.setPlaceholderText(t['register_phonenumber_lineedit'][1][l])

def reset_name(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_name_lineedit.setStyleSheet('border: 0;')
    self.register_name_label.setText(t['register_name_label'][0][l])

def reset_email(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_emial_lineedit.setStyleSheet('border: 0;')
    self.register_name_label.setText(t['register_name_label'][0][l])
#______________________________________________________________________________________________________________________

def reset_confirm_email(self):
    self.register_emial_confirm_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_phone(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_phonenumber_lineedit.setStyleSheet('border: 0;')
    self.register_phonenumber_lineedit.setPlaceholderText(t['register_phonenumber_lineedit'][0][l])
#______________________________________________________________________________________________________________________

def reset_password(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_password_requirements_label.setText(f'{t['register_password_requirements_label'][0][l]}')
    self.register_password_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________

def reset_confirm_password(self):
    t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/register/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.register_password_requirements_label.setText(f'{t['register_password_requirements_label'][0][l]}')
    self.register_password_confirm_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________
