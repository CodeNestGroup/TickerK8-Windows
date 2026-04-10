#   --- Improt ---
import json
from PyQt5.QtWidgets import (
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)
from PyQt5.QtGui import (
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
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
    m = open(f'{self.Path}/APP_FILES/PYTHON/ListNews/BMain.css', encoding='utf-8').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/ListNews/B{t}.css', encoding='utf-8').read()
    self.setStyleSheet(m+c)
    