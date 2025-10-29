""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy, # Size policy
    QGraphicsView # Graphic view 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings
    QSize # Size 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Chart Ui """
def chart_ui(self):
    """ Set object name """
    self.setObjectName('chart_widget')
    self.top_widget.setObjectName('top_widget')
    self.top_exit_button.setObjectName('top_exit_button')
    self.top_title_label.setObjectName('top_title_label')
    self.top_fullscrean_button.setObjectName('top_fullscrean_button')
    self.top_settings_button.setObjectName('top_settings_button')
    self.bottom_widget.setObjectName('bottom_widget')
    self.bottom_1d_button.setObjectName('bottom_1d_button')
    self.bottom_5d_button.setObjectName('bottom_5d_button')
    self.bottom_1m_button.setObjectName('bottom_1m_button')
    self.bottom_3m_button.setObjectName('bottom_3m_button')
    self.bottom_1y_button.setObjectName('bottom_1y_button')
    self.bottom_ytd_button.setObjectName('bottom_ytd_button')
    self.bottom_all_button.setObjectName('bottom_all_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.top_exit_button.setProperty('class', 'top_button')
    self.top_fullscrean_button.setProperty('class', 'top_button')
    self.top_settings_button.setProperty('class', 'top_button')
    self.bottom_1d_button.setProperty('class', 'bottom_button')
    self.bottom_5d_button.setProperty('class', 'bottom_button')
    self.bottom_1m_button.setProperty('class', 'bottom_button')
    self.bottom_3m_button.setProperty('class', 'bottom_button')
    self.bottom_1y_button.setProperty('class', 'bottom_button')
    self.bottom_ytd_button.setProperty('class', 'bottom_button')
    self.bottom_all_button.setProperty('class', 'bottom_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.top_widget, 0, 0, 10, 100)
    self.main_layout.addWidget(self.bottom_widget, 90, 0, 10, 100)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.top_layout.addWidget(self.top_exit_button, 15, 2, 25, 3)
    self.top_layout.addWidget(self.top_fullscrean_button, 15, 7, 25, 3)
    self.top_layout.addWidget(self.top_settings_button, 15, 12, 25, 3)
    self.top_layout.addWidget(self.top_title_label, 30, 40, 40, 20)
    self.top_layout.setSpacing(0)
    self.top_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.top_layout.setRowStretch(enc, 1)
        self.top_layout.setColumnStretch(enc, 1)
    self.top_widget.setLayout(self.top_layout)
    self.bottom_layout.addWidget(self.bottom_1d_button, 10, 10, 80, 8)
    self.bottom_layout.addWidget(self.bottom_5d_button, 10, 20, 80, 8)
    self.bottom_layout.addWidget(self.bottom_1m_button, 10, 30, 80, 8)
    self.bottom_layout.addWidget(self.bottom_3m_button, 10, 40, 80, 8)
    self.bottom_layout.addWidget(self.bottom_1y_button, 10, 50, 80, 8)
    self.bottom_layout.addWidget(self.bottom_ytd_button, 10, 60, 80, 8)
    self.bottom_layout.addWidget(self.bottom_all_button, 10, 70, 80, 8)
    self.bottom_layout.setSpacing(0)
    self.bottom_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.bottom_layout.setRowStretch(enc, 1)
        self.bottom_layout.setColumnStretch(enc, 1)
    self.bottom_widget.setLayout(self.bottom_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.top_title_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_fullscrean_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.top_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_1d_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_5d_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_1m_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_3m_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_1y_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_ytd_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.bottom_all_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Chart style """
def chart_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/chart/'+self.global_config['__theme__']+'.css')).read())
    self.top_exit_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/exit_'+self.global_config['__theme__']+'.svg'), 256, 256)))
    self.top_exit_button.setIconSize(self.top_exit_button.size())
#######################################################################################################################
""" Chart retranslate """
def chart_retranslate(self):
    _t = self.chart_translate # Translate texts 
    _l = self.global_config['__language__'] # Language
    self.bottom_1d_button.setText(_t['bottom_1d_button'][_l])
    self.bottom_5d_button.setText(_t['bottom_5d_button'][_l])
    self.bottom_1m_button.setText(_t['bottom_1m_button'][_l])
    self.bottom_3m_button.setText(_t['bottom_3m_button'][_l])
    self.bottom_1y_button.setText(_t['bottom_1y_button'][_l])
    self.bottom_ytd_button.setText(_t['bottom_ytd_button'][_l])
    self.bottom_all_button.setText(_t['bottom_all_button'][_l])
######################################################################################################################
""" Load svg script """
def load_svg(svg_path, width, height):
    renderer = QSvgRenderer(svg_path) # Render svg
    pixmap = QPixmap(width, height) # Create pixmap
    pixmap.fill(Qt.transparent) # Transparent
    painter = QPainter(pixmap) # Render graphic 
    renderer.render(painter) # Render graphic
    painter.end() # Render graphic
    scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
    return scaled_pixmap
#######################################################################################################################