#   --- Import ---
import json
import datetime
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget
    )
from PySide6.QtCore import (
    Qt,
    )
from PySide6.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)
from PySide6.QtSvg import (
    QSvgRenderer
)

def BackgroundPainter(self):
    l = self.Language
    ColorsJson = self.Background['background']
    IconsJson = self.Background['icon']
    Color0 = '#000000'
    Color1 = '#000000'
    Color2 = '#000000'
    Alpha1 = 'ff'
    Alpha2 = 'ff'
    X1 = 0.0
    X2 = 1.0 
#       --- Calculate index and precent ---
    Now = datetime.datetime.now()
    TodaySec = Now.hour*3600+Now.minute*60+Now.second
    if TodaySec >=86400:
        TodaySec = 86399
    Index = TodaySec//8640 
    Percent = (TodaySec/8640)-Index 
#       --- Set colors ---
    if Percent <= 0.5:
        X1 = 1-(Percent*2)
        X2 = 1.0
        Alpha1 = 'ff'
        Alpha2 = f'{int(255 *(Percent / 0.5)):02X}'
        Color0 = f'#ff{ColorsJson[Index-1]}'
    else:
        X1 = 0.0
        X2 = 1-(Percent-0.5)*2
        Alpha1 = f'{255-int(255 *(Percent - 0.5) / 0.5):02X}'
        Alpha2 = 'ff'
        Color0 = f'#ff{ColorsJson[Index]}'
    Color1 = f'#{Alpha1}{ColorsJson[Index-1]}'
    Color2 = f'#{Alpha2}{ColorsJson[Index]}'
#       --- Paint background ---
    Pixmap = QPixmap(self.size())
    Pixmap.fill(QColor(Color0))
    Painter = QPainter(Pixmap)
    Gradient = QLinearGradient(0,0,self.width(), 0)
    Gradient.setColorAt(X1, QColor(Color1))
    Gradient.setColorAt(X2, QColor(Color2))
    Painter.fillRect(self.rect(), Gradient)
    Painter.end()
    Palette = self.palette()
    Palette.setBrush(QPalette.Window, QBrush(Pixmap))
    self.setAutoFillBackground(True)
    self.setPalette(Palette)
#       --- Call text and icon change ---
    if self.IndexChanged != Index:
        Icon = f'{self.Path}/assets/ICON/{IconsJson[Index]}vintage_elegance_d.svg'
        ChangeTextIcon(
            self,
            self.LoginWelcomeTranslate['WelcomeTitleL'][Index][l],
            self.LoginWelcomeTranslate['WelcomeSubL'][Index][l],
            Icon)
        self.IndexChanged = Index

def ChangeTextIcon(self, t='', s='', i=''):
    self.WelcomeTitleL.setText(t)
    self.WelcomeSubL.setText(s)
    Render = QSvgRenderer(i)
    IconPixmap = QPixmap(self.WelcomeIconL.height(), self.WelcomeIconL.height())
    IconPixmap.fill(Qt.transparent)
    IconPainter = QPainter(IconPixmap)
    Render.render(IconPainter)
    IconPainter.end()
    self.WelcomeIconL.setPixmap(QPixmap(IconPixmap))

def ResetStyle(self):
    if self.Theme == 'vintage_elegance_l':
        c = '#e0e0e0'
    elif self.Theme == 'vintage_elegance_d':
        c = '#1a1a1a'
    self.LoginL.setStyleSheet(f'border-color: {c};')
    self.PasswordL.setStyleSheet(f'border-color: {c};')

def LoginController(self):
    d = self.CheckLoginF(str(self.LoginL.text()))
    if d[1] == self.PasswordL.text():
        if d[2]:
             pass
        else:
            self.SetLoggedUserIdF(d[0])
            if not d[3]:
                self.LoginConfigurationOpenF()
            else:
                self.UpdateLastLoginF(d[0])
                self.MainOpenF()
    else:
        self.LoginL.clear()
        self.PasswordL.clear()
        self.LoginL.setStyleSheet('border: 2px solid red;')
        self.PasswordL.setStyleSheet('border: 2px solid red;')  
