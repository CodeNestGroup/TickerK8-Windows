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

def main_ui(self):
    """ Set object name """
    self.setObjectName('main_widget')
    self.search_button.setObjectName('search_button')
    self.objects_list_title_label.setObjectName('objects_list_title_label')
    self.objects_list_scroll.setObjectName('objects_list_scroll')
    self.type_list_button.setObjectName('type_list_button')
    self.data_list_button.setObjectName('data_list_button')
    self.settings_button.setObjectName('settings_button')
    self.logout_button.setObjectName('logout_button')
    self.object_icon_label.setObjectName('object_icon_label')
    self.object_ticker_label.setObjectName('object_ticker_label')
    self.object_name_label.setObjectName('object_name_label')
    self.object_news_button.setObjectName('object_news_button')
    self.object_chart_button.setObjectName('object_chart_button')
    self.object_stats_button.setObjectName('object_stats_button')
    self.news_next_left_button.setObjectName('news_next_left_button')
    self.news_next_right_button.setObjectName('news_next_right_button')
    self.news_market_button.setObjectName('news_market_button')
    self.news_country_button.setObjectName('news_country_button')
    self.news_world_button.setObjectName('news_world_button')
    """ Set property """
    self.type_list_button.setProperty('class', 'list_button')
    self.data_list_button.setProperty('class', 'list_button')
    self.settings_button.setProperty('class', 'bottom_button')
    self.logout_button.setProperty('class', 'bottom_button')
    self.object_news_button.setProperty('class', 'object_button')
    self.object_chart_button.setProperty('class', 'object_button')
    self.object_stats_button.setProperty('class', 'object_button')
    self.news_next_left_button.setProperty('class', 'news_nav_button')
    self.news_next_right_button.setProperty('class', 'news_nav_button')
    self.news_market_button.setProperty('class', 'news_type_button')
    self.news_country_button.setProperty('class', 'news_type_button')
    self.news_world_button.setProperty('class', 'news_type_button')
    """ Set layout """
    self.layout.addWidget(self.search_button, 2, 1, 1, 13)
    self.layout.addWidget(self.objects_list_title_label, 8, 1, 2, 13)
    self.layout.addWidget(self.objects_list_scroll, 15, 1, 72, 13)
    self.layout.addWidget(self.type_list_button, 90, 1, 2, 6)
    self.layout.addWidget(self.data_list_button, 90, 8, 2, 6)
    self.layout.addWidget(self.settings_button, 96, 1, 2, 2)
    self.layout.addWidget(self.logout_button, 96, 4, 2, 2)
    self.layout.addWidget(self.object_icon_label, 2, 15, 2, 42)
    self.layout.addWidget(self.object_ticker_label, 5, 15, 2, 42)
    self.layout.addWidget(self.object_name_label, 8, 15, 2, 42)
    self.layout.addWidget(self.object_news_button, 96, 15, 2, 13)
    self.layout.addWidget(self.object_chart_button, 96, 29, 2, 14)
    self.layout.addWidget(self.object_stats_button, 96, 44, 2, 13)
    self.layout.addWidget(self.news_next_left_button, 90, 58, 2, 20)
    self.layout.addWidget(self.news_next_right_button, 90, 79, 2, 20)
    self.layout.addWidget(self.news_market_button, 96, 58, 2, 13)
    self.layout.addWidget(self.news_country_button, 96, 72, 2, 13)
    self.layout.addWidget(self.news_world_button, 96, 86, 2, 13)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    """ Set widget """
    self.setHidden(False)
    self.object_ticker_label.setHidden(True)
    self.objects_list_scroll.setWidgetResizable(True)
    """ Set label """
    self.objects_list_title_label.setAlignment(Qt.AlignCenter)
    self.object_icon_label.setAlignment(Qt.AlignCenter)
    self.object_ticker_label.setAlignment(Qt.AlignCenter)
    self.object_name_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    self.object_news_button.setDisabled(True)
    self.object_chart_button.setDisabled(True)
    self.object_stats_button.setDisabled(True)
    self.news_world_button.setDisabled(True)
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.search_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.objects_list_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.objects_list_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.data_list_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.logout_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_news_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_chart_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_stats_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_next_left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_next_right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_market_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_country_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_world_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def main_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main/'+_global_config['theme']+'.css')).read())
    self.search_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/search_'+_global_config['theme']+'.svg'), 256, 256)))
    self.search_button.setIconSize(self.search_button.size())
    self.type_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/list_'+_global_config['theme']+'.svg'), 256, 256)))
    self.type_list_button.setIconSize(self.type_list_button.size())
    self.data_list_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/edit_table_data_'+_global_config['theme']+'.svg'), 256, 256)))
    self.data_list_button.setIconSize(self.data_list_button.size())
    self.settings_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/settings_'+_global_config['theme']+'.svg'), 256, 256)))
    self.settings_button.setIconSize(self.settings_button.size())
    self.logout_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg'), 256, 256)))
    self.logout_button.setIconSize(self.logout_button.size())
    self.object_news_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/news_'+_global_config['theme']+'.svg'), 256, 256)))
    self.object_news_button.setIconSize(self.object_news_button.size())
    self.object_chart_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/chart_'+_global_config['theme']+'.svg'), 256, 256)))
    self.object_chart_button.setIconSize(self.object_chart_button.size())
    self.object_stats_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/statistics_'+_global_config['theme']+'.svg'), 256, 256)))
    self.object_stats_button.setIconSize(self.object_stats_button.size())
    self.news_next_left_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/arrow_left_'+_global_config['theme']+'.svg'), 256, 256)))
    self.news_next_left_button.setIconSize(self.news_next_left_button.size())
    self.news_next_right_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/arrow_right_'+_global_config['theme']+'.svg'), 256, 256)))
    self.news_next_right_button.setIconSize(self.news_next_right_button.size())
    self.news_market_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/market_'+_global_config['theme']+'.svg'), 256, 256)))
    self.news_market_button.setIconSize(self.news_market_button.size())
    self.news_country_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/country_'+_global_config['theme']+'.svg'), 256, 256)))
    self.news_country_button.setIconSize(self.news_country_button.size())
    self.news_world_button.setIcon(QIcon(load_svg(str(self.main_path+'/STYLE/IMG/icons/main/world_'+_global_config['theme']+'.svg'), 256, 256)))
    self.news_world_button.setIconSize(self.news_world_button.size())
#______________________________________________________________________________________________________________________

def main_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.search_button.setText(_t['search_button'][_l])
    self.type_list_button.setText(_t['type_list_button'][_l])
    self.data_list_button.setText(_t['data_list_button'][_l])
    self.object_news_button.setText(_t['object_news_button'][_l])
    self.object_chart_button.setText(_t['object_chart_button'][_l])
    self.object_stats_button.setText(_t['object_stats_button'][_l])
    self.news_market_button.setText(_t['news_market_button'][_l])
    self.news_country_button.setText(_t['news_country_button'][_l])
    self.news_world_button.setText(_t['news_world_button'][_l])
#______________________________________________________________________________________________________________________

def object_list_lists_ui(self):
    """ Set object name """
    self.objects_list_lists_title_label.setObjectName('objects_list_lists_title_label')
    self.objects_list_lists_scroll.setObjectName('objects_list_lists_scroll')
    self.objects_list_lists_widget.setObjectName('objects_list_lists_widget')
    self.objects_list_lists_exit_button.setObjectName('objects_list_lists_exit_button')
    """ Set layout """
    self.layout.addWidget(self.objects_list_lists_title_label, 8, 1, 2, 11)
    self.layout.addWidget(self.objects_list_lists_scroll, 15, 1, 72, 11)
    self.layout.addWidget(self.objects_list_lists_exit_button, 90, 1, 2, 11)
    self.objects_list_lists_layout.setSpacing(0)
    self.objects_list_lists_layout.setContentsMargins(0,0,0,0)
    self.objects_list_lists_widget.setLayout(self.objects_list_lists_layout)
    """ Set widget """
    self.objects_list_lists_scroll.setWidgetResizable(True)
    self.objects_list_lists_scroll.setWidget(self.objects_list_lists_widget)
    """ Set label """
    self.objects_list_lists_title_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.objects_list_lists_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.objects_list_lists_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.objects_list_lists_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.objects_list_lists_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def object_list_lists_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.objects_list_lists_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg', 256, 256)))
    self.objects_list_lists_exit_button.setIconSize(self.objects_list_lists_exit_button.size())
#______________________________________________________________________________________________________________________

def object_list_lists_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.objects_list_lists_title_label.setText(_t['objects_list_lists_title_label'][_l])
#______________________________________________________________________________________________________________________

def object_list_edit_ui(self):
    """ Set object name """
    self.object_list_edit_title_label.setObjectName('object_list_edit_title_label')
    self.object_list_edit_scroll.setObjectName('object_list_edit_scroll')
    self.object_list_edit_widget.setObjectName('object_list_edit_widget')
    self.object_list_edit_icon_button.setObjectName('object_list_edit_icon_button')
    self.object_list_edit_ticker_button.setObjectName('object_list_edit_ticker_button')
    self.object_list_edit_pe_ratio_button.setObjectName('object_list_edit_pe_ratio_button')
    self.object_list_edit_eps_button.setObjectName('object_list_edit_eps_button')
    self.object_list_edit_dividend_yield_button.setObjectName('object_list_edit_dividend_yield_button')
    self.object_list_edit_capitalization_button.setObjectName('object_list_edit_capitalization_button')
    self.object_list_edit_capital_button.setObjectName('object_list_edit_capital_button')
    self.object_list_edit_exit_button.setObjectName('object_list_edit_exit_button')
    """ Set property """
    self.object_list_edit_icon_button.setProperty('class', 'object_list_edit_data_button')
    self.object_list_edit_ticker_button.setProperty('class', 'object_list_edit_data_button')
    self.object_list_edit_pe_ratio_button.setProperty('class', 'object_list_edit_data_button')
    self.object_list_edit_eps_button.setProperty('class', 'object_list_edit_data_button')
    self.object_list_edit_dividend_yield_button.setProperty('class', 'object_list_edit_data_button')
    self.object_list_edit_capitalization_button.setProperty('class', 'object_list_edit_data_button')
    self.object_list_edit_capital_button.setProperty('class', 'object_list_edit_data_button')
    """ Set layout """
    self.layout.addWidget(self.object_list_edit_title_label, 8, 1, 2, 11)
    self.layout.addWidget(self.object_list_edit_scroll, 15, 1, 72, 11)
    self.layout.addWidget(self.object_list_edit_exit_button, 90, 1, 2, 11)
    self.object_list_edit_layout.addWidget(self.object_list_edit_icon_button,0,0)
    self.object_list_edit_layout.addWidget(self.object_list_edit_ticker_button,0,1)
    self.object_list_edit_layout.addWidget(self.object_list_edit_pe_ratio_button,1,0)
    self.object_list_edit_layout.addWidget(self.object_list_edit_eps_button,1,1)
    self.object_list_edit_layout.addWidget(self.object_list_edit_dividend_yield_button,2,0)
    self.object_list_edit_layout.addWidget(self.object_list_edit_capitalization_button,2,1)
    self.object_list_edit_layout.addWidget(self.object_list_edit_capital_button,3,0)
    self.object_list_edit_layout.setSpacing(0)
    self.object_list_edit_layout.setContentsMargins(0,0,0,0)
    self.object_list_edit_widget.setLayout(self.object_list_edit_layout)
    """ Set widget """
    self.object_list_edit_scroll.setWidgetResizable(True)
    self.object_list_edit_scroll.setWidget(self.object_list_edit_widget)
    """ Set label """
    self.object_list_edit_title_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.object_list_edit_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_icon_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_ticker_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_pe_ratio_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_eps_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_dividend_yield_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_capitalization_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_capital_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_list_edit_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def object_list_edit_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    self.object_list_edit_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg', 256, 256)))
    self.object_list_edit_exit_button.setIconSize(self.object_list_edit_exit_button.size())
#______________________________________________________________________________________________________________________

def object_list_edit_retranslate(self):
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.object_list_edit_title_label.setText(_t['object_list_edit_title_label'][_l])
    self.object_list_edit_icon_button.setText(_t['object_list_edit_icon_button'][_l])
    self.object_list_edit_ticker_button.setText(_t['object_list_edit_ticker_button'][_l])
    self.object_list_edit_pe_ratio_button.setText(_t['object_list_edit_pe_ratio_button'][_l])
    self.object_list_edit_eps_button.setText(_t['object_list_edit_eps_button'][_l])
    self.object_list_edit_dividend_yield_button.setText(_t['object_list_edit_dividend_yield_button'][_l])
    self.object_list_edit_capitalization_button.setText(_t['object_list_edit_capitalization_button'][_l])
    self.object_list_edit_capital_button.setText(_t['object_list_edit_capital_button'][_l])
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
