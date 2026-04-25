#   --- Import ---
import json
import string
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLineEdit
)

def ShowHidePassword(self):
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))['PasswordShowB']

    if self.PasswordL.echoMode() == QLineEdit.Normal: 
        self.PasswordL.setEchoMode(QLineEdit.Password) 
        self.PasswordShowB.setText(t[1][l])
    else:
        self.PasswordL.setEchoMode(QLineEdit.Normal)
        self.PasswordShowB.setText(t[0][l])

def RegisterController(self):
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    WrongData = 'border-color: #c01414;'
    Name = None
    Email = None
    EmailConfirm = None
    PhonePrefix = None
    Phone = None
    Country = None
    Password = None
    PasswordConfirm = None

    Name = self.NameL.text()
    if Name == '':
        Name = None
        self.NameInfoL.show()
        self.NameInfoL.setText(f'{t['NameInfoL'][0][l]}')
        self.NameL.setStyleSheet(WrongData)
    
    Email = self.EmialL.text()
    EmailConfirm = self.EmialConfirmL.text()
    if Email != EmailConfirm:
        Email = None
        EmailConfirm = None
        self.EmailInfoL.show()
        self.EmailInfoL.setText(f'{t['EmailInfoL'][2][l]}')
        self.EmialConfirmL.setStyleSheet(WrongData)
    if Email == '' or EmailConfirm == '':
        Email = None
        EmailConfirm = None
        self.EmailInfoL.show()
        self.EmailInfoL.setText(f'{t['EmailInfoL'][0][l]}')
        self.EmialL.setStyleSheet(WrongData)
        self.EmialConfirmL.setStyleSheet(WrongData)
    
    PhonePrefix = self.PhonenumberC.currentText()
    if PhonePrefix == '':
        PhonePrefix = None

    Phone = self.PhonenumberL.text()
    if Phone == '' or not Phone.isdigit():
        Phone = None
        self.PhonenumberL.setText('')
        self.PhonenumberL.setPlaceholderText(f'{t['PhonenumberL'][2][l]}')
        self.PhonenumberL.setStyleSheet(WrongData)
    
    Country = self.CountryC.currentText()
    if Country == '':
        Country = None

    Password = self.PasswordL.text()
    PasswordConfirm = self.PasswordConfirmL.text()
    if len(PasswordConfirm) < 8 or not any(h.isupper() for h in PasswordConfirm) or not any(h.isdigit() for h in PasswordConfirm) or not any(h in string.punctuation for h in PasswordConfirm):
        Password = None
        self.PasswordRequirementsL.setText(f'{t['PasswordRequirementsL'][2][l]}')
        self.PasswordL.setStyleSheet(WrongData)
    if Password  != PasswordConfirm:
        Password = None
        self.PasswordRequirementsL.setText(f'{t['PasswordRequirementsL'][1][l]}')
        self.PasswordConfirmL.setStyleSheet(WrongData)
    
    if Name and Password and Email and PhonePrefix and Phone and Country:
        try:
            err = self.RegisterUserF((Name, Password, Email, PhonePrefix, Phone, Country))
            if not err:
                self.LoginOpenF()
            else:
                for e in err:
                    if e == 'USER_EXISTS':
                        UserExists(self)
                    elif e == 'EMAIL_EXISTS':
                        EmailExists(self)
                    elif e == 'PHONE_EXISTS_IN_PREFIX':
                        PhoneExists(self)
                    else:
                        raise Exception
        except Exception as e:
            print(e) # Dopisz do logi

def UserExists(self):
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.NameL.setStyleSheet('border-color: #c01414;')
    self.NameInfoL.setText(t['NameInfoL'][1][l])

def EmailExists(self):
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.EmialL.setStyleSheet('border-color: #c01414;')
    self.EmailInfoL.setText(t['register_email_label'][1][l])

def PhoneExists(self):
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.PhonenumberL.setStyleSheet('border-color: #c01414;')
    self.PhonenumberL.setText('')
    self.PhonenumberL.setPlaceholderText(t['PhonenumberL'][1][l])

def ResetName(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.NameL.setStyleSheet(f'border-color: {c};')
    self.NameInfoL.setText(t['NameInfoL'][0][l])

def ResetEmail(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.EmialL.setStyleSheet(f'border-color: {c};')
    self.EmailInfoL.setText(t['EmailInfoL'][0][l])

def ResetConfirmEmail(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    self.EmialConfirmL.setStyleSheet(f'border-color: {c};')

def ResetPhone(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.PhonenumberL.setStyleSheet(f'border-color: {c};')
    self.PhonenumberL.setPlaceholderText(t['PhonenumberL'][0][l])

def ResetPassword(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.PasswordRequirementsL.setText(f'{t['PasswordRequirementsL'][0][l]}')
    self.PasswordL.setStyleSheet(f'border-color: {c};')

def ResetConfirmPassword(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    l = self.Language
    t = json.load(open(self.Path+'/assets/JSON/RegisterTranslate.json', 'r', encoding='utf-8'))
    self.PasswordRequirementsL.setText(f'{t['PasswordRequirementsL'][0][l]}')
    self.PasswordConfirmL.setStyleSheet(f'border-color: {c};')
