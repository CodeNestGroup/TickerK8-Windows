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

def ListObjectUi(self):
    self.setObjectName('ListObjectW')
    self.Layout.setSpacing(0)
    self.Layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.Layout.setRowStretch(i, 1)
        self.Layout.setColumnStretch(i, 1)
    self.show()
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def ListObjectReloadStyle(self):
    m = open(f'{self.Path}/APP_FILES/PYTHON/ListObject/BMain.css').read()
    c = open(f'{self.Path}/APP_FILES/PYTHON/ListObject/B{self.Theme}.css').read()
    self.setStyleSheet(m+c)
    
def NullDataUi(self):
    self.NullDataL.setObjectName('NullDataL')
    self.Layout.addWidget(self.NullDataL, 0, 0, 100, 100)
    self.NullDataL.show()
    self.NullDataL.setAlignment(Qt.AlignCenter)
    self.NullDataL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def NullDataRetranslate(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/ListObject/CNullDataRetranslate.json', 'r'))
    l = self.Language
    self.NullDataL.setText(t['NullDataL'][l])

def DataUi(self):
    self.NameL.setObjectName('NameL')
    self.DataS.setObjectName('DataS')
    self.DataW.setObjectName('DataW')
    self.Layout.addWidget(self.NameL, 0, 0, 5, 100)
    self.Layout.addWidget(self.DataS, 7, 2, 88, 96)
    self.DataL.setSpacing(0)
    self.DataL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.DataL.setColumnStretch(i, 1)
    self.DataW.setLayout(self.DataL)
    self.DataS.setWidgetResizable(True)
    self.DataS.setWidget(self.DataW)
    self.NameL.setAlignment(Qt.AlignCenter)
    self.DataS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.DataW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def LoadSvg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap