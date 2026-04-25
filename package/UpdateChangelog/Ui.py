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

def UpdateChangelogUi(self):
    self.setObjectName('UpdateChangelogW')
    self.TitleL.setObjectName('TitleL')
    self.ChangelogS.setObjectName('ChangelogS')
    self.ChangelogW.setObjectName('ChangelogW')
    self.ChangelogTitleL.setObjectName('ChangelogTitleL')
    self.ChangelogDateL.setObjectName('ChangelogDateL')
    self.ChangelogTextL.setObjectName('ChangelogTextL')
    self.ExitB.setObjectName('ExitB')
    self.ChangelogL.addWidget(self.ChangelogTitleL)
    self.ChangelogL.addWidget(self.ChangelogDateL)
    self.ChangelogL.addWidget(self.ChangelogTextL)
    self.ChangelogL.setSpacing(0)
    self.ChangelogL.setContentsMargins(0,0,0,0)
    self.ChangelogW.setLayout(self.ChangelogL)
    self.Layout.addWidget(self.TitleL, 5, 5, 10, 90)
    self.Layout.addWidget(self.ChangelogS, 20, 5, 60, 90)
    self.Layout.addWidget(self.ExitB, 89, 40, 6, 20)
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.Layout.setRowStretch(enc, 1)
        self.Layout.setColumnStretch(enc, 1)
    self.setLayout(self.Layout)
    self.setHidden(False)
    self.ChangelogS.setWidget(self.ChangelogW)
    self.ChangelogS.setWidgetResizable(True)
    self.ChangelogS.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.TitleL.setAlignment(Qt.AlignCenter)
    self.ChangelogTitleL.setAlignment(Qt.AlignCenter)
    self.ChangelogDateL.setAlignment(Qt.AlignCenter)
    self.ChangelogTextL.setWordWrap(True)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.TitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogTitleL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogDateL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ChangelogTextL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ExitB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def UpdateChangelogReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/UpdateChangelogMain.css').read()
    c = open(f'{self.Path}/assets/CSS/UpdateChangelog{t}.css').read()
    self.setStyleSheet(m+c)
    self.ExitB.setIcon(QIcon(load_svg(f'{self.Path}/assets/ICON/Exit{t}.svg', 256, 256)))

def UpdateChangelogRetranslate(self):
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/UpdateChangelogTranslate.json', 'r', encoding='utf-8'))
    c = self.ChangelogData
    self.TitleL.setText(t['TitleL'][l])
    self.ChangelogTitleL.setText(c['name'])
    self.ChangelogDateL.setText(str(c['published_at']).replace('T', ' ').replace('Z', ''))
    self.ChangelogTextL.setText(c['body'])

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) 
    pixmap = QPixmap(width, height) 
    pixmap.fill(Qt.transparent) 
    painter = QPainter(pixmap) 
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
