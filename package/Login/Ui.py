#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLineEdit,
    QSizePolicy
)
from PySide6.QtCore import (
    Qt
)


def LoginUi(self):
    self.setObjectName('LoginW')
    self.LoginL.setObjectName('LoginL')
    self.PasswordL.setObjectName('PasswordL')
    self.LoginB.setObjectName('LoginB')
    self.RegisterB.setObjectName('RegisterB')
    self.WelcomeTitleL.setObjectName('WelcomeTitleL')
    self.WelcomeSubL.setObjectName('WelcomeSubL')
    self.WelcomeIconL.setObjectName('WelcomeIconL')
    self.LoginL.setProperty('class', 'InputL')
    self.PasswordL.setProperty('class', 'InputL')
    self.Layout.addWidget(self.LoginL, 42, 4, 4, 42)
    self.Layout.addWidget(self.PasswordL, 48, 4, 4, 42)
    self.Layout.addWidget(self.LoginB, 56, 12, 2, 26)
    self.Layout.addWidget(self.RegisterB, 97, 15, 1, 20)
    self.Layout.addWidget(self.WelcomeTitleL, 30, 50, 15, 50)
    self.Layout.addWidget(self.WelcomeSubL, 45, 50, 10, 50)
    self.Layout.addWidget(self.WelcomeIconL, 55, 50, 10, 50)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.show()
    self.WelcomeTitleL.setAlignment(Qt.AlignCenter)
    self.WelcomeSubL.setAlignment(Qt.AlignCenter)
    self.WelcomeIconL.setAlignment(Qt.AlignCenter)
    self.PasswordL.setEchoMode(QLineEdit.Password)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LoginL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PasswordL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LoginB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RegisterB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.WelcomeTitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.WelcomeSubL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.WelcomeIconL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def LoginReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/LoginMain.css').read()
    c = open(f'{self.Path}/assets/CSS/Login{t}.css').read()
    self.setStyleSheet(m+c)

def LoginRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/LoginTranslate.json', 'r', encoding='utf-8'))
    self.LoginL.setPlaceholderText(t['LoginL'][l])
    self.PasswordL.setPlaceholderText(t['PasswordL'][l])
    self.LoginB.setText(t['LoginB'][l])
    self.RegisterB.setText(t['RegisterB'][l])
