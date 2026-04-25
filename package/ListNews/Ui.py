#   --- Improt ---
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

def ListNewsUi(self):
    self.setObjectName('ListNewsW')
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    self.setLayout(self.Layout)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ListNewsReloadStyle(self):
    t = self.Theme
    m = open(f'{self.Path}/assets/CSS/ListNewsMain.css').read()
    c = open(f'{self.Path}/assets/CSS/ListNews{t}.css').read()
    self.setStyleSheet(m+c)
    