""" Import packages """
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QSizePolicy 
)
from PyQt5.QtCore import (
    Qt,
    QRect
)
from PyQt5.QtGui import (
    QIcon
)
#______________________________________________________________________________________________________________________

def main_news_ui(self):
    """ Set object name """
    self.setObjectName('main_news_widget')
    self.panel_widget.setObjectName('panel_widget')
    self.news_scroll.setObjectName('news_scroll')
    self.panel_exit_button.setObjectName('panel_exit_button')
    """ Set property """
    """ Set layout """
    self.main_layout.addWidget(self.panel_widget, 1, 20, 98, 60)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.panel_layout.addWidget(self.news_scroll, 0, 0, 90, 100)
    self.panel_layout.addWidget(self.panel_exit_button, 95, 40, 3, 20)
    self.panel_layout.setSpacing(0)
    self.panel_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_layout.setRowStretch(enc, 1)
        self.panel_layout.setColumnStretch(enc, 1)
    self.panel_widget.setLayout(self.panel_layout)
    """ Set widget """
    self.setHidden(False)
    self.news_scroll.setWidgetResizable(True)
    self.news_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.setGeometry(QRect(0, 0, self.parent.width(), self.parent.height()))
    self.panel_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def main_news_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_news/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________

def main_news_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main_news/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.panel_exit_button.setText(_t['panel_exit_button'][_l])
#______________________________________________________________________________________________________________________
