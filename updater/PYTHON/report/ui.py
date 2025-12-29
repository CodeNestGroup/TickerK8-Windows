""" Import packages """
import json
""" Import PyQt5 packages """
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
#______________________________________________________________________________________________________________________

def report_ui(self):
    """ Set object name """
    self.setObjectName('report_widget')
    self.textfield_textarea.setObjectName('textfield_textarea')
    self.send_button.setObjectName('send_button')
    self.clear_button.setObjectName('clear_button')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    self.send_button.setProperty('class', 'buttons')
    self.clear_button.setProperty('class', 'buttons')
    self.exit_button.setProperty('class', 'buttons')
    """ Set layout """
    self.layout.addWidget(self.textfield_textarea, 10, 10, 80, 80)
    self.layout.addWidget(self.send_button, 94, 10, 2, 22)
    self.layout.addWidget(self.clear_button, 94, 39, 2, 22)
    self.layout.addWidget(self.exit_button, 94, 68, 2, 22)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    """ Set label """
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.textfield_textarea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.send_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.clear_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def report_reload_style(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    t = g['theme']
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/report/'+t+'.css')).read())
    self.exit_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/report/exit_'+t+'.svg'), 256, 256)))

def report_retranslate(self):
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    t = json.load(open(self.main_path+'/CONFIG/report/translate.json', 'r'))
    self.send_button.setText(t['send_button'][l])
    self.clear_button.setText(t['clear_button'][l])
#______________________________________________________________________________________________________________________

def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) 
    pixmap = QPixmap(width, height) 
    pixmap.fill(Qt.transparent) 
    painter = QPainter(pixmap) 
    renderer.render(painter)
    painter.end()
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return scaled_pixmap
#______________________________________________________________________________________________________________________
