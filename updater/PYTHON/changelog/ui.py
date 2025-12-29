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

def changelog_ui(self):
    """ Set object name """
    self.setObjectName('changelog_widget')
    self.title_label.setObjectName('title_label')
    self.scroll.setObjectName('scroll')
    self.update_widget.setObjectName('update_widget')
    self.update_title_label.setObjectName('update_title_label')
    self.update_date_label.setObjectName('update_date_label')
    self.update_text_label.setObjectName('update_text_label')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    """ Set layout """
    self.layout.addWidget(self.title_label, 5, 5, 10, 90)
    self.layout.addWidget(self.scroll, 20, 5, 60, 90)
    self.layout.addWidget(self.exit_button, 89, 40, 6, 20)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    self.update_layout.addWidget(self.update_title_label)
    self.update_layout.addWidget(self.update_date_label)
    self.update_layout.addWidget(self.update_text_label)
    self.update_layout.setSpacing(0)
    self.update_layout.setContentsMargins(0,0,0,0)
    self.update_widget.setLayout(self.update_layout)
    """ Set widget """
    self.setHidden(False)
    self.scroll.setWidgetResizable(True)
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.scroll.setWidget(self.update_widget)
    """ Set label """
    self.title_label.setAlignment(Qt.AlignCenter)
    self.update_title_label.setAlignment(Qt.AlignCenter)
    self.update_date_label.setAlignment(Qt.AlignCenter)
    self.update_text_label.setWordWrap(True)
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def changelog_reload_style(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    t = g['theme']
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/changelog/'+t+'.css')).read())
    self.exit_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/changelog/exit_vintage_elegance_d.svg'), 256, 256)))

def changelog_retranslate(self):
    t = json.load(open(self.main_path+'/CONFIG/changelog/translate.json', 'r'))
    l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    c = self.changelog_data
    self.title_label.setText(t['title_label'][l])
    self.update_title_label.setText(c['name'])
    self.update_date_label.setText(str(c['published_at']).replace('T', ' ').replace('Z', ''))
    self.update_text_label.setText(c['body'])
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
