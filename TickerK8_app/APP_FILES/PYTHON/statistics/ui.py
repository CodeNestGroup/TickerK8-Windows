""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings
    QSize # Szie
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon, # Icon
    QPixmap, # Graphic.
    QPainter # Painter.
) 
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Statistics ui """
def statistics_ui(self):
    """ Set object name """
    self.setObjectName('statistics_widget')
    self.main_title_label.setObjectName('main_title_label')
    self.main_flag_label.setObjectName('main_flag_label')
    self.main_exit_button.setObjectName('main_exit_button')
    self.main_close_button.setObjectName('main_close_button')
    self.main_scroll.setObjectName('main_scroll')
#_______________________________________________________________________________________________________________________
    """ Set property """
    self.main_exit_button.setProperty('class', 'main_e_c_button')
    self.main_close_button.setProperty('class', 'main_e_c_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.main_layout.addWidget(self.main_title_label, 0, 40, 8, 15)
    self.main_layout.addWidget(self.main_flag_label, 2, 56, 3, 4)
    self.main_layout.addWidget(self.main_exit_button, 2, 2, 3, 3)
    self.main_layout.addWidget(self.main_close_button, 2, 2, 3, 3)
    self.main_layout.addWidget(self.main_scroll, 10, 0, 92, 100)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
    self.main_close_button.setHidden(True)
    self.main_scroll.setWidgetResizable(True)
    self.main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.main_title_label.setAlignment(Qt.AlignCenter)
    self.main_flag_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_flag_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_close_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Statistics reload style """
def statistics_reload_style(self):
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/statistics/'+self.global_config['__theme__']+'.css')).read())
    self.main_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+self.global_config['__theme__']+'.svg', 256, 256)))
    self.main_close_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+self.global_config['__theme__']+'.svg', 256, 256)))
#######################################################################################################################
""" Statistics retranslate """
def statistics_retranslate(self):
    pass
#######################################################################################################################
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
