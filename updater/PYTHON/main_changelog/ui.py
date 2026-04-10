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
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
#______________________________________________________________________________________________________________________

def changelog_ui(self):
    """ Set obejct name """
    self.setObjectName('changelog_widget')
    """ Set property"""
    """ Set layout """
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    self.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    """ Set label """
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def changelog_reload_style(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    t = g['theme']
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_changelog/'+t+'.css')).read())
#______________________________________________________________________________________________________________________

def no_connection_ui(self):
    """ Set object name """
    self.widget.setObjectName('widget')
    self.icon_label.setObjectName('icon_label')
    self.message_label.setObjectName('message_label')
    """ Set property """
    """ Set layout """
    self.widget_layout.addWidget(self.icon_label, 30, 0, 30, 100)
    self.widget_layout.addWidget(self.message_label, 62, 0, 10, 100)
    self.widget_layout.setSpacing(0)
    self.widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.widget_layout.setRowStretch(enc, 1)
        self.widget_layout.setColumnStretch(enc, 1)
    self.widget.setLayout(self.widget_layout)
    self.layout.addWidget(self.widget)
    """ Set widget """
    self.widget.setHidden(False)
    """ Set label """
    self.icon_label.setAlignment(Qt.AlignCenter)
    self.message_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


def no_connection_reload_style(self):
    t = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['theme']
    self.icon_label.setPixmap(load_svg(str(self.main_path+'/STYLE/IMG/icons/main_changelog/no_connection_'+t+'.svg'), 256, 256))

def no_connection_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/main_changelog/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.message_label.setText(t['message_label'][0][l])

def loading_ui(self):
    """ Set object name """
    self.widget.setObjectName('widget')
    self.icon_label.setObjectName('icon_label')
    self.message_label.setObjectName('message_label')
    self.dots_label.setObjectName('dots_label')
    """ Set property """
    """ Set layout """
    self.widget_layout.addWidget(self.icon_label, 30, 0, 30, 100)
    self.widget_layout.addWidget(self.message_label, 62, 0, 10, 50)
    self.widget_layout.addWidget(self.dots_label, 62, 50, 10, 50)
    self.widget_layout.setSpacing(0)
    self.widget_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.widget_layout.setRowStretch(enc, 1)
        self.widget_layout.setColumnStretch(enc, 1)
    self.widget.setLayout(self.widget_layout)
    self.layout.addWidget(self.widget)
    """ Set widget """
    self.widget.setHidden(False)
    """ Set label """
    self.icon_label.setAlignment(Qt.AlignCenter)
    self.message_label.setAlignment(Qt.AlignRight)
    self.dots_label.setAlignment(Qt.AlignLeft)
    """ Set button """
    """ Set size """
    self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.dots_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def loading_reload_style(self):
    t = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['theme']
    self.icon_label.setPixmap(load_svg(str(self.main_path+'/STYLE/IMG/icons/main_changelog/no_connection_'+t+'.svg'), 256, 256))

def loading_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/main_changelog/translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.message_label.setText(t['message_label'][1][l])
#______________________________________________________________________________________________________________________

def connection_ui(self):
    """ Set object name """
    self.scroll.setObjectName('scroll')
    self.widget.setObjectName('widget')
    """ Set property """
    for button in self.releases_button_list:
        button.setProperty('class', 'buttons')
    """ Set layout """
    for button in self.releases_button_list:
        self.widget_layout.addWidget(button)
    self.widget_layout.setSpacing(0)
    self.widget_layout.setContentsMargins(0,0,0,0)
    self.widget.setLayout(self.widget_layout)
    self.layout.addWidget(self.scroll)
    """ Set wigdet """
    self.scroll.setHidden(False)
    self.scroll.setWidgetResizable(True)
    self.scroll.setWidget(self.widget)
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    """ Set label """
    """ Set button """
    """ Set size """
    self.scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    for button in self.releases_button_list:
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def connection_retranslate(self):
    d = self.release_data
    for i, button in enumerate(self.releases_button_list, start=0):
        button.setText(d[i]['name'])
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
