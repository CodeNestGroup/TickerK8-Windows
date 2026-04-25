#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QSizePolicy
)
from PySide6.QtCore import (
    Qt,
    QSize
)
from PySide6.QtGui import (
    QPixmap,
    QIcon,
    QPainter
)
from PySide6.QtSvg import (
    QSvgRenderer
)

def LoginConfigurationUi(self):
    self.setObjectName('LoginConfigurationW')
    self.TitleL.setObjectName('TitleL')
    self.InfoL.setObjectName('InfoL')
    self.LeftB.setObjectName('LeftB')
    self.ExitB.setObjectName('ExitB')
    self.RightB.setObjectName('RightB')
    self.AcceptB.setObjectName('AcceptB')
    self.NaviL.setObjectName('NaviL')
    self.LeftB.setProperty('class', 'NaviButton')
    self.ExitB.setProperty('class', 'NaviButton')
    self.RightB.setProperty('class', 'NaviButton')
    self.AcceptB.setProperty('class', 'NaviButton')
    self.Layout.addWidget(self.TitleL, 0, 0, 10, 100)
    self.Layout.addWidget(self.InfoL, 15, 0, 75, 100)
    self.Layout.addWidget(self.LeftB, 92, 10, 3, 10)
    self.Layout.addWidget(self.ExitB, 97, 10, 3, 10)
    self.Layout.addWidget(self.RightB, 92, 80, 3, 10)
    self.Layout.addWidget(self.AcceptB, 97, 80, 3, 10)
    self.Layout.addWidget(self.NaviL, 92, 20, 6, 60)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.show()
    self.AcceptB.hide()
    self.TitleL.setAlignment(Qt.AlignCenter)
    self.InfoL.setAlignment(Qt.AlignCenter)
    self.NaviL.setAlignment(Qt.AlignCenter)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.TitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InfoL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LeftB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RightB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.AcceptB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def LoginConfigurationReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/LoginConfigurationMain.css').read()
    c = open(f'{self.Path}/assets/CSS/LoginConfiguration{t}.css').read()
    self.setStyleSheet(m+c)

def LoginConfigurationRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationTranslate.json', 'r', encoding='utf-8'))
    self.TitleL.setText(t['TitleL'][l])
    self.InfoL.setText(t['InfoL'][l][0])
    self.LeftB.setText(t['LeftB'][l])
    self.ExitB.setText(t['ExitB'][l])
    self.RightB.setText(t['RightB'][l])
    self.AcceptB.setText(t['AcceptB'][l])

def AppConfUi(self):
    self.CenterW.setObjectName('CenterW')
    self.LanguageSubtitleL.setObjectName('LanguageSubtitleL')
    self.LanguageC.setObjectName('LanguageC')
    self.ThemeSubtitleL.setObjectName('ThemeSubtitleL')
    self.ThemeC.setObjectName('ThemeC')
    self.LanguageSubtitleL.setProperty('class', 'SubTitle')
    self.ThemeSubtitleL.setProperty('class', 'SubTitle')
    self.LanguageC.setProperty('class', 'List')
    self.ThemeC.setProperty('class', 'List')
    self.CenterL.addWidget(self.LanguageSubtitleL, 0, 0, 10, 50)
    self.CenterL.addWidget(self.LanguageC, 20, 20, 80, 20)
    self.CenterL.addWidget(self.ThemeSubtitleL, 0, 50, 10, 50)
    self.CenterL.addWidget(self.ThemeC, 20, 60, 80, 20)
    self.Layout.addWidget(self.CenterW, 15, 0, 75, 100)
    self.AcceptB.hide()
    self.LanguageSubtitleL.setAlignment(Qt.AlignCenter)
    self.ThemeSubtitleL.setAlignment(Qt.AlignCenter)
    self.CenterW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LanguageSubtitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LanguageC.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ThemeSubtitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ThemeC.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def AppConfRetranslate(self):
    l = self.Language
    if self.Theme == 'vintage_elegance_l':
        ti = 0
    elif self.Theme == 'vintage_elegance_d':
        ti = 1
    t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationAppConfTranslate.json', 'r', encoding='utf-8'))
    self.LanguageSubtitleL.setText(t['LanguageSubtitleL'][l])
    self.LanguageC.blockSignals(True)
    self.LanguageC.clear()
    self.LanguageC.addItems(t['LanguageC'])
    self.LanguageC.setCurrentIndex(l)
    self.LanguageC.blockSignals(False)
    self.ThemeSubtitleL.setText(t['ThemeSubtitleL'][l])
    self.ThemeC.blockSignals(True)
    self.ThemeC.clear()
    self.ThemeC.addItems(dict(t['ThemeC']).keys())
    self.ThemeC.setCurrentIndex(ti)
    self.ThemeC.blockSignals(False)

def SubConfUi(self):
    self.CenterW.setObjectName('CenterW')
    self.LeftB.setObjectName('LeftB')
    self.CenterB.setObjectName('CenterB')
    self.RightB.setObjectName('RightB')
    self.LeftB.setProperty('class', 'SubButton')
    self.CenterB.setProperty('class', 'SubButton')
    self.RightB.setProperty('class', 'SubButton')
    self.CenterL.addWidget(self.LeftB, 0, 10, 100, 15)
    self.CenterL.addWidget(self.CenterB, 0, 30, 100, 40)
    self.CenterL.addWidget(self.RightB, 0, 75, 100, 15)
    self.Layout.addWidget(self.CenterW, 15, 0, 75, 100)
    self.AcceptB.hide()
    self.CenterW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LeftB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.CenterB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RightB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def SubConfRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationSubConfTranslate.json', 'r', encoding='utf-8'))
    self.LeftB.setText(t['LeftB'][l])
    self.CenterB.setText(t['CenterB'][l])
    self.RightB.setText(t['RightB'][l])

def AcceptSettingsUi(self):
    self.CenterW.setObjectName('CenterW')
    self.RegulationsS.setObjectName('RegulationsS')
    self.RegulationsW.setObjectName('RegulationsW')
    self.RegulationsValueL.setObjectName('RegulationsValueL')
    self.RegulationsL.addWidget(self.RegulationsValueL, 0, 0)
    self.RegulationsL.setSpacing(0)
    self.RegulationsL.setContentsMargins(0,0,0,0)
    self.RegulationsW.setLayout(self.RegulationsL)
    self.CenterL.addWidget(self.RegulationsS, 0, 20, 100, 60)
    self.Layout.addWidget(self.CenterW, 15, 0, 75, 100)
    self.AcceptB.show()
    self.RegulationsS.setWidget(self.RegulationsW)
    self.RegulationsS.setWidgetResizable(True)
    self.RegulationsS.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.RegulationsValueL.setAlignment(Qt.AlignCenter)
    self.CenterW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RegulationsS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RegulationsW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.RegulationsValueL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def AcceptSettingsRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationAcceptSettingsTranslate.json', 'r', encoding='utf-8'))
    self.RegulationsValueL.setText(t['RegulationsValueL'][l])
