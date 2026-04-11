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
    QIcon,
    QPixmap,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
#______________________________________________________________________________________________________________________

def main_search_ui(self):
    """ Set object name """
    self.setObjectName('main_search_widget')
    self.panel_widget.setObjectName('panel_widget')
    self.panel_search_widget.setObjectName('panel_search_widget')
    self.panel_search_lineedit.setObjectName('panel_search_lineedit')
    self.panel_type_stock_button.setObjectName('panel_type_stock_button')
    self.panel_type_etf_button.setObjectName('panel_type_etf_button')
    self.panel_type_forex_button.setObjectName('panel_type_forex_button')
    self.panel_type_index_button.setObjectName('panel_type_index_button')
    self.panel_type_market_button.setObjectName('panel_type_market_button')
    self.panel_type_country_button.setObjectName('panel_type_country_button')
    self.panel_id_label.setObjectName('panel_id_label')
    self.panel_object_name_label.setObjectName('panel_object_name_label')
    self.panel_market_name_label.setObjectName('panel_market_name_label')
    self.panel_scroll.setObjectName('panel_scroll')
    self.panel_exit_button.setObjectName('panel_exit_button')
    """ Set property """
    self.panel_type_stock_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_etf_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_forex_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_index_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_market_button.setProperty('class', 'panel_type_buttons')
    self.panel_type_country_button.setProperty('class', 'panel_type_buttons')
    self.panel_id_label.setProperty('class', 'panel_tags')
    self.panel_object_name_label.setProperty('class', 'panel_tags')
    self.panel_market_name_label.setProperty('class', 'panel_tags')
    self.panel_scroll.setProperty('class', 'panel_scroll_class')
    self.panel_exit_button.setProperty('class', 'panel_exit_button_class')
    """ Set layout """
    self.main_layout.addWidget(self.panel_widget, 10, 20, 80, 60)
    self.main_layout.setSpacing(0)
    self.main_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.main_layout.setRowStretch(enc, 1)
        self.main_layout.setColumnStretch(enc, 1)
    self.setLayout(self.main_layout)
    self.panel_layout.addWidget(self.panel_search_widget)
    self.panel_layout.setSpacing(0)
    self.panel_layout.setContentsMargins(0,0,0,0)
    self.panel_widget.setLayout(self.panel_layout)
    self.panel_search_layout.addWidget(self.panel_search_lineedit, 5, 30, 5, 40)
    self.panel_search_layout.addWidget(self.panel_type_stock_button, 15, 5, 3, 14)
    self.panel_search_layout.addWidget(self.panel_type_etf_button, 15, 20, 3, 14)
    self.panel_search_layout.addWidget(self.panel_type_forex_button, 15, 35, 3, 14)
    self.panel_search_layout.addWidget(self.panel_type_index_button, 15, 50, 3, 14)
    self.panel_search_layout.addWidget(self.panel_type_market_button, 15, 65, 3, 14)
    self.panel_search_layout.addWidget(self.panel_type_country_button, 15, 80, 3, 14)
    self.panel_search_layout.addWidget(self.panel_id_label, 20, 7, 3, 5)
    self.panel_search_layout.addWidget(self.panel_object_name_label, 20, 26, 3, 26)
    self.panel_search_layout.addWidget(self.panel_market_name_label, 20, 66, 3, 26)
    self.panel_search_layout.addWidget(self.panel_scroll, 23, 5, 72, 90)
    self.panel_search_layout.addWidget(self.panel_exit_button, 2, 5, 6, 5)
    self.panel_search_layout.setSpacing(0)
    self.panel_search_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_search_layout.setRowStretch(enc, 1)
        self.panel_search_layout.setColumnStretch(enc, 1)
    self.panel_search_widget.setLayout(self.panel_search_layout)
    """ Set widget """
    self.setHidden(False)
    self.panel_widget.setHidden(False)
    self.panel_search_widget.setHidden(False)
    self.panel_scroll.setWidgetResizable(True)
    self.panel_type_etf_button.setDisabled(True)
    self.panel_type_forex_button.setDisabled(True)
    """ Set label """
    self.panel_id_label.setAlignment(Qt.AlignCenter)
    self.panel_object_name_label.setAlignment(Qt.AlignCenter)
    self.panel_market_name_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.setGeometry(0, 0, self.parent.width(), self.parent.height())
    self.panel_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_search_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_search_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_stock_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_etf_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_forex_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_index_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_type_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_id_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_object_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_market_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def main_search_reload_style(self):
    _global_config = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    self.setStyleSheet(open(str(self.main_path+'/TickerK8_app/APP_FILES/STYLE/CSS/main_search/'+_global_config['theme']+'.css')).read())
    self.panel_exit_button.setIcon(QIcon(load_svg(self.main_path+'/TickerK8_app/APP_FILES/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg', 256, 256)))
#______________________________________________________________________________________________________________________

def main_search_retranslate(self):
    _t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/main_search/translate.json', 'r', encoding='utf-8'))
    _l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.panel_search_lineedit.setPlaceholderText(_t['panel_search_lineedit'][_l])
    self.panel_type_stock_button.setText(_t['panel_type_stock_button'][_l])
    self.panel_type_etf_button.setText(_t['panel_type_etf_button'][_l])
    self.panel_type_forex_button.setText(_t['panel_type_forex_button'][_l])
    self.panel_type_index_button.setText(_t['panel_type_index_button'][_l])
    self.panel_type_market_button.setText(_t['panel_type_market_button'][_l])
    self.panel_type_country_button.setText(_t['panel_type_country_button'][_l])
    self.panel_id_label.setText('#')
    self.panel_object_name_label.setText(_t['panel_object_name_label'][_l])
    self.panel_market_name_label.setText(_t['panel_market_name_label'][_l])
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
