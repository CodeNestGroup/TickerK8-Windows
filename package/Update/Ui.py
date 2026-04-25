#   --- Import ---
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy
)
from PySide6.QtCore import (
    Qt,
    QRectF,
    QSize
)
from PySide6.QtGui import (
    QIcon,
    QPixmap,
    QPainter
)
from PySide6.QtSvg import (
    QSvgRenderer
)

def UpdateUi(self):
    self.setObjectName('UpdateW')
    self.SettingsB.setObjectName('SettingsB')
    self.InstagramB.setObjectName('InstagramB')
    self.GithubB.setObjectName('GithubB')
    self.DiscordB.setObjectName('DiscordB')
    self.SettingsB.setProperty('class', 'Button')
    self.InstagramB.setProperty('class', 'Button')
    self.GithubB.setProperty('class', 'Button')
    self.DiscordB.setProperty('class', 'Button')
    self.Layout.addWidget(self.SettingsB, 30, 51, 25, 23)
    self.Layout.addWidget(self.InstagramB, 30, 75, 25, 23)
    self.Layout.addWidget(self.GithubB, 56, 51, 25, 23)
    self.Layout.addWidget(self.DiscordB, 56, 75, 25, 23)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.SettingsB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.InstagramB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.GithubB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.DiscordB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def UpadateReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/UpdateMain.css').read()
    c = open(f'{self.Path}/assets/CSS/Update{t}.css').read()
    self.setStyleSheet(m+c)
    self.SettingsB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Settings{t}.svg', 256, 256)))
    self.SettingsB.setIconSize(self.SettingsB.size())
    self.InstagramB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Instagram{t}.svg', 256, 256)))
    self.InstagramB.setIconSize(self.InstagramB.size())
    self.GithubB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Github{t}.svg', 256, 256)))
    self.GithubB.setIconSize(self.GithubB.size())
    self.DiscordB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Discord{t}.svg', 256, 256)))
    self.DiscordB.setIconSize(self.DiscordB.size())

def ChangelogNoConnectionUi(self):
    self.ChangelogW.setObjectName('ChangelogW')
    self.ChangelogIconL.setObjectName('ChangelogIconL')
    self.ChangelogMessageL.setObjectName('ChangelogMessageL')
    self.ChangelogL.addWidget(self.ChangelogIconL, 30,0, 30, 100)
    self.ChangelogL.addWidget(self.ChangelogMessageL, 62, 0, 10, 100)
    self.ChangelogL.setSpacing(0)
    self.ChangelogL.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.ChangelogL.setRowStretch(enc, 1)
        self.ChangelogL.setColumnStretch(enc, 1)
    self.ChangelogW.setLayout(self.ChangelogL)
    self.Layout.addWidget(self.ChangelogW, 0, 0, 100, 50)
    self.ChangelogW.show()
    self.ChangelogIconL.setAlignment(Qt.AlignCenter)
    self.ChangelogMessageL.setAlignment(Qt.AlignCenter)
    self.ChangelogW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogIconL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogMessageL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ChangelogNoConnectionReloadStyle(self):
    t = self.Theme
    self.ChangelogIconL.setPixmap(QPixmap(load_svg(f'{self.Path}/assets/ICON/NoConnection{t}.svg', 256, 256)))

def ChangelogNoConnectionRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/UpdateTranslate.json', 'r', encoding='utf-8'))
    self.ChangelogMessageL.setText(t['ChangelogMessageL'][0][l])

def ChangelogLoadingUi(self):
    self.ChangelogW.setObjectName('ChangelogW')
    self.ChangelogIconL.setObjectName('ChangelogIconL')
    self.ChangelogMessageL.setObjectName('ChangelogMessageL')
    self.ChaneglogDotsL.setObjectName('ChaneglogDotsL')
    self.ChangelogL.addWidget(self.ChangelogIconL, 30,0, 30, 100)
    self.ChangelogL.addWidget(self.ChangelogMessageL, 62, 0, 10, 50)
    self.ChangelogL.addWidget(self.ChaneglogDotsL, 62, 50, 10, 50)
    self.ChangelogL.setSpacing(0)
    self.ChangelogL.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.ChangelogL.setRowStretch(enc, 1)
        self.ChangelogL.setColumnStretch(enc, 1)
    self.ChangelogW.setLayout(self.ChangelogL)
    self.Layout.addWidget(self.ChangelogW, 0, 0, 100, 50)
    self.ChangelogW.show()
    self.ChangelogIconL.setAlignment(Qt.AlignCenter)
    self.ChangelogMessageL.setAlignment(Qt.AlignCenter)
    self.ChaneglogDotsL.setAlignment(Qt.AlignCenter)
    self.ChangelogW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogIconL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogMessageL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChaneglogDotsL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ChangelogLoadingReloadStyle(self):
    t = self.Theme
    self.ChangelogIconL.setPixmap(QPixmap(load_svg(f'{self.Path}/assets/ICON/NoConnection{t}.svg', 256, 256)))

def ChangelogLoadingRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/UpdateTranslate.json', 'r', encoding='utf-8'))
    self.ChangelogMessageL.setText(t['ChangelogMessageL'][1][l])

def ChangelogConnctionUi(self):
    self.ChangelogS.setObjectName('ChangelogS')
    self.ChangelogW.setObjectName('ChangelogW')
    self.ChangelogL.setSpacing(0)
    self.ChangelogL.setContentsMargins(0,0,0,0)
    self.ChangelogW.setLayout(self.ChangelogL)
    self.Layout.addWidget(self.ChangelogS, 0, 0, 100, 50)
    self.ChangelogS.show()
    self.ChangelogS.setWidgetResizable(True)
    self.ChangelogS.setWidget(self.ChangelogW)
    self.ChangelogS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) 
    pixmap = QPixmap(width, height) 
    pixmap.fill(Qt.transparent) 
    painter = QPainter(pixmap) 
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
