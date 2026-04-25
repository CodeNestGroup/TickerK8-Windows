#   --- Import ---
import json
#   --- Import PySide ---
from PySide6.QtWidgets import (
    QSizePolicy
)
from PySide6.QtCore import (
    Qt,
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

def UpdateSettingsUi(self):
    self.setObjectName('SettingsW')
    self.NaviS.setObjectName('NaviS')
    self.NaviW.setObjectName('NaviW')
    self.NaviStyleB.setObjectName('NaviStyleB')
    self.NaviUpdateB.setObjectName('NaviUpdateB')
    self.NaviLanguageB.setObjectName('NaviLanguageB')
    self.NaviExitB.setObjectName('NaviExitB')
    self.NaviStyleB.setProperty('class', 'NaviB')
    self.NaviUpdateB.setProperty('class', 'NaviB')
    self.NaviLanguageB.setProperty('class', 'NaviB')
    self.NaviExitB.setProperty('class', 'NaviB')
    self.NaviL.addWidget(self.NaviStyleB)
    self.NaviL.addWidget(self.NaviUpdateB)
    self.NaviL.addWidget(self.NaviLanguageB)
    self.NaviL.setSpacing(0)
    self.NaviL.setContentsMargins(0,0,0,0)
    self.NaviW.setLayout(self.NaviL)
    self.Layout.addWidget(self.NaviS, 0, 0, 90, 20)
    self.Layout.addWidget(self.NaviExitB, 90, 0, 10, 20)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.setLayout(self.Layout)
    self.show()
    self.NaviS.setWidgetResizable(True)
    self.NaviS.setWidget(self.NaviW)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviStyleB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviUpdateB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviLanguageB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.NaviExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def UpdateSettingsReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/SettingsMain.css').read()
    c = open(f'{self.Path}/assets/CSS/Settings{t}.css').read()
    self.setStyleSheet(m+c)
    self.NaviExitB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Exit{t}.svg', 256, 256)))
    self.NaviExitB.setIconSize(self.NaviExitB.size())

def UpdateSettingsRetranslate(self):
    t = json.load(open(f'{self.Path}/assets/JSON/SettingsNaviTranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.NaviStyleB.setText(t['NaviStyleB'][l])
    self.NaviUpdateB.setText(t['NaviUpdateB'][l])
    self.NaviLanguageB.setText(t['NaviLanguageB'][l])

def StyleUi(self):
    self.PanelS.setObjectName('PanelS')
    self.PanelW.setObjectName('PanelW')
    self.PanelTitleL.setObjectName('PanelTitleL')
    self.StyleThemeDayNightNameL.setObjectName('StyleThemeDayNightNameL')
    self.StyleThemeDayNightValueB.setObjectName('StyleThemeDayNightValueB')
    self.StyleThemeThemesNameL.setObjectName('StyleThemeThemesNameL')
    self.StyleThemeThemesValueC.setObjectName('StyleThemeThemesValueC')
    self.StyleThemeDayNightNameL.setProperty('class', 'NameL')
    self.StyleThemeThemesNameL.setProperty('class', 'NameL')
    self.StyleThemeDayNightValueB.setProperty('class', 'ValueB')
    self.StyleThemeThemesValueC.setProperty('class', 'ValueC')
    self.PanelL.addWidget(self.PanelTitleL, 0, 0, 1, 100)
    self.PanelL.addWidget(self.StyleThemeDayNightNameL, 1, 0, 1, 25)
    self.PanelL.addWidget(self.StyleThemeDayNightValueB, 1, 25, 1, 25)
    self.PanelL.addWidget(self.StyleThemeThemesNameL, 2, 0, 1, 25)
    self.PanelL.addWidget(self.StyleThemeThemesValueC, 2, 25, 1, 25)
    self.PanelL.setSpacing(0)
    self.PanelL.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.PanelL.setColumnStretch(i,1)
    self.PanelW.setLayout(self.PanelL)
    self.Layout.addWidget(self.PanelS, 0, 20, 100, 75)
    self.show()
    self.PanelS.setWidgetResizable(True)
    self.PanelS.setWidget(self.PanelW)
    self.PanelTitleL.setAlignment(Qt.AlignCenter)
    self.StyleThemeDayNightNameL.setAlignment(Qt.AlignCenter)
    self.StyleThemeThemesNameL.setAlignment(Qt.AlignCenter)
    self.PanelS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PanelW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PanelTitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.StyleThemeDayNightNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.StyleThemeDayNightValueB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.StyleThemeThemesNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.StyleThemeThemesValueC.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def StyleRetranslate(self):
    t = json.load(open(f'{self.Path}/assets/JSON/SettingsStyleTranslate.json', 'r'))
    l = self.Language
    if self.Theme == 'vintage_elegance_l':
        i = 0
    elif self.Theme == 'vintage_elegance_d':
        i = 1
    self.PanelTitleL.setText(t['PanelTitleL'][l])
    self.StyleThemeDayNightNameL.setText(t['StyleThemeDayNightNameL'][l]+':')
    self.StyleThemeDayNightValueB.setText(t['StyleThemeDayNightValueB'][l][i])
    self.StyleThemeThemesNameL.setText(t['StyleThemeThemesNameL'][l]+':')
    self.StyleThemeThemesValueC.blockSignals(True)
    self.StyleThemeThemesValueC.clear()
    self.StyleThemeThemesValueC.addItems(dict(t['StyleThemeThemesValueC']).keys())
    self.StyleThemeThemesValueC.setCurrentIndex(i)
    self.StyleThemeThemesValueC.blockSignals(False)

def UpdateUi(self):
    self.PanelS.setObjectName('PanelS')
    self.PanelW.setObjectName('PanelW')
    self.PanelTitleL.setObjectName('PanelTitleL')
    self.UpdateDescriptionNameL.setObjectName('UpdateDescriptionNameL')
    self.UpdateDescriptionValueL.setObjectName('UpdateDescriptionValueL')
    self.UpdateChangelogNameL.setObjectName('UpdateChangelogNameL')
    self.UpdateChangelogValueS.setObjectName('UpdateChangelogValueS')
    self.UpdateChangelogValueW.setObjectName('UpdateChangelogValueW')
    self.UpdateChangelogValueLA.setObjectName('UpdateChangelogValueLA')
    self.UpdateDescriptionNameL.setProperty('class', 'NameL')
    self.UpdateChangelogNameL.setProperty('class', 'NameL')
    self.UpdateDescriptionValueL.setProperty('class', 'ValueL')
    self.UpdateChangelogValueS.setProperty('class', 'ValueS')
    self.UpdateChangelogValueW.setProperty('class', 'ValueW')
    self.UpdateChangelogValueLA.setProperty('class', 'ValueL')
    self.UpdateChangelogValueL.addWidget(self.UpdateChangelogValueLA,0,0,1,1)
    self.UpdateChangelogValueL.setSpacing(0)
    self.UpdateChangelogValueL.setContentsMargins(0,0,0,0)
    self.UpdateChangelogValueW.setLayout(self.UpdateChangelogValueL)
    self.PanelL.addWidget(self.PanelTitleL, 0, 0, 1, 100)
    self.PanelL.addWidget(self.UpdateDescriptionNameL, 1, 0, 1, 25)
    self.PanelL.addWidget(self.UpdateDescriptionValueL, 1, 25, 1, 25)
    self.PanelL.addWidget(self.UpdateChangelogNameL, 2, 0, 1, 25)
    self.PanelL.addWidget(self.UpdateChangelogValueS, 2, 25, 1, 50)
    self.PanelL.setSpacing(0)
    self.PanelL.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.PanelL.setColumnStretch(i,1)
    self.PanelW.setLayout(self.PanelL)
    self.Layout.addWidget(self.PanelS, 0, 20, 100, 75)
    self.show()
    self.UpdateChangelogValueS.setWidgetResizable(True)
    self.UpdateChangelogValueS.setWidget(self.UpdateChangelogValueW)
    self.PanelS.setWidgetResizable(True)
    self.PanelS.setWidget(self.PanelW)
    self.PanelTitleL.setAlignment(Qt.AlignCenter)
    self.UpdateDescriptionNameL.setAlignment(Qt.AlignCenter)
    self.UpdateDescriptionValueL.setAlignment(Qt.AlignCenter)
    self.UpdateChangelogNameL.setAlignment(Qt.AlignCenter)
    self.UpdateChangelogValueLA.setWordWrap(True)
    self.PanelS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PanelW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PanelTitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.UpdateDescriptionNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.UpdateDescriptionValueL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.UpdateChangelogNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.UpdateChangelogValueS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.UpdateChangelogValueW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.UpdateChangelogValueLA.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def UpdateRetranslate(self):
    t = json.load(open(f'{self.Path}/assets/JSON/SettingsUpdateTranslate.json', 'r', encoding='utf-8'))
    u = json.load(open(self.Path+'/assets/JSON/Changelog.json', 'r', encoding='utf-8'))
    l = self.Language
    self.PanelTitleL.setText(t['PanelTitleL'][l])
    self.UpdateDescriptionNameL.setText(t['UpdateDescriptionNameL'][l]+':')
    self.UpdateChangelogNameL.setText(t['UpdateChangelogNameL'][l]+':')
    self.UpdateChangelogValueLA.setText(u['body'])

def LanguageUi(self):
    self.PanelS.setObjectName('PanelS')
    self.PanelW.setObjectName('PanelW')
    self.PanelTitleL.setObjectName('PanelTitleL')
    self.LanguageNameL.setObjectName('LanguageNameL')
    self.LanguageValueC.setObjectName('LanguageValueC')
    self.LanguageNameL.setProperty('class', 'NameL')
    self.LanguageValueC.setProperty('class', 'ValueC')
    self.PanelL.addWidget(self.PanelTitleL, 0, 0, 1, 100)
    self.PanelL.addWidget(self.LanguageNameL, 1, 0, 1, 25)
    self.PanelL.addWidget(self.LanguageValueC, 1, 25, 1, 25)
    self.PanelL.setSpacing(0)
    self.PanelL.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.PanelL.setColumnStretch(i,1)
    self.PanelW.setLayout(self.PanelL)
    self.Layout.addWidget(self.PanelS, 0, 20, 100, 75)
    self.show()
    self.PanelS.setWidgetResizable(True)
    self.PanelS.setWidget(self.PanelW)
    self.PanelTitleL.setAlignment(Qt.AlignCenter)
    self.LanguageNameL.setAlignment(Qt.AlignCenter)
    self.PanelS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PanelW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.PanelTitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LanguageNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.LanguageValueC.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def LanguageRetranslate(self):
    t = json.load(open(f'{self.Path}/assets/JSON/SettingsLanguageTranslate.json', 'r', encoding='utf-8'))
    l = self.Language
    self.PanelTitleL.setText(t['PanelTitleL'][l])
    self.LanguageNameL.setText(t['LanguageNameL'][l]+':')
    self.LanguageValueC.blockSignals(True)
    self.LanguageValueC.clear()
    self.LanguageValueC.addItems(t['LanguageValueC'])
    self.LanguageValueC.setCurrentIndex(l)
    self.LanguageValueC.blockSignals(False)

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(width, height)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
