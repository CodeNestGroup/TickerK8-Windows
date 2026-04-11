import json # For json files
import sqlite3 # For local database
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QScrollArea, # Scroll widget
    QGridLayout, # Grid layout
    QVBoxLayout, # Vertical layout 
    QSizePolicy # Size policy 
)
from PyQt5.QtCore import Qt, QSize, QRect
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QPixmap, # Graphic.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
#######################################################################################################################
""" Statistics country """
def statisitcs_country(self):
    """ Set data """
    database = sqlite3.connect(database=self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    result = cursor.execute(f'SELECT name, icon FROM country WHERE id={self.global_config['mid_object'][1]};').fetchall()[0]
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________
    """ Show close button """
    self.main_exit_button.setHidden(False)
    self.main_close_button.setHidden(True)
#______________________________________________________________________________________________________________________
    """ Set title """
    self.main_title_label.setText(f'{result[0]}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.main_flag_label.setPixmap(load_svg(self.main_path+'/TickerK8_app/APP_FILES/STYLE/IMG/flags'+result[1]+'.svg', int(self.height()*0.15), int(self.height()*0.15)))
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.scroll_widget: # Check if main scroll have widget 
        self.scroll_widget.deleteLater() # Delete scroll widget
        self.scroll_widget = None # Set dafault 
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.scroll_widget = QWidget(self.main_scroll)
    self.scroll_layout = QGridLayout(self.scroll_widget)
    self.gdp_button = QPushButton(self.scroll_widget)
    self.n_r_button = QPushButton(self.scroll_widget)
    self.people_button = QPushButton(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.scroll_widget.setObjectName('scroll_widget')
    self.gdp_button.setObjectName('gdp_button')
    self.n_r_button.setObjectName('n_r_button')
    self.people_button.setObjectName('people_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.gdp_button.setProperty('class', 'option_button')
    self.n_r_button.setProperty('class', 'option_button')
    self.people_button.setProperty('class', 'option_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.scroll_layout.addWidget(self.gdp_button, 0, 0)
    self.scroll_layout.addWidget(self.n_r_button, 0, 1)
    self.scroll_layout.addWidget(self.people_button, 1, 0)
    self.scroll_layout.setSpacing(0)
    self.scroll_layout.setContentsMargins(0,0,0,0)
    self.scroll_widget.setLayout(self.scroll_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_scroll.setWidget(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.gdp_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.people_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.gdp_button.setText('GDP')
    self.n_r_button.setText('Natural Resources')
    self.people_button.setText('People')
    self.main_scroll.setWidget(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set connect """
    self.gdp_button.clicked.connect(lambda: open_gdp(self))
    self.n_r_button.clicked.connect(lambda: open_n_r(self))
    self.people_button.clicked.connect(lambda: open_people(self))
#######################################################################################################################
""" Statistics market """
def statisitcs_market(self):
    pass
#######################################################################################################################
""" Statistics index """
def statisitcs_index(self):
    pass
#######################################################################################################################
""" Statistics stock """
def statisitcs_stock(self):
    pass
#######################################################################################################################
""" Open gdp """
def open_gdp(self):
    pass
#######################################################################################################################
""" Open natural resources """
def open_n_r(self):
    """ Set data """
    database = sqlite3.connect(database=self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    n_r_forests_data = cursor.execute(f'''
    SELECT
    n_r_forests.area_ha,
    n_r_forests.area_percent, 
    n_r_forests.area_map,
    n_r_forests.logging,
    n_r_forests.growth_rate,
    n_r_forests.market_value,
    n_r_forests.date 
    FROM n_r_forests 
    WHERE n_r_forests.id_country={self.global_config['mid_object'][1]} 
    and n_r_forests.id_tree_type=0 
    ORDER BY n_r_forests.date DESC LIMIT 1;''').fetchall()[0]
    n_r_agriculture_data = cursor.execute(f'''
    SELECT
    n_r_agriculture.area_ha,
    n_r_agriculture.area_percent,
    n_r_agriculture.area_map,
    n_r_agriculture.harvastering,
    n_r_agriculture.market_value,
    n_r_agriculture.date 
    FROM n_r_agriculture 
    WHERE n_r_agriculture.id_country={self.global_config['mid_object'][1]} 
    and n_r_agriculture.id_crops_type=0 
    ORDER BY n_r_agriculture.date DESC LIMIT 1;''').fetchall()[0]
    n_r_minerals_data = cursor.execute(f'''
    SELECT 
    n_r_minerals.area_m3,
    n_r_minerals.area_map,
    n_r_minerals.extraction,
    n_r_minerals.market_value,
    n_r_minerals.date
    FROM n_r_minerals 
    WHERE n_r_minerals.id_country={self.global_config['mid_object'][1]} 
    and n_r_minerals.id_mineral_type=0 
    ORDER BY n_r_minerals.date DESC LIMIT 1;''').fetchall()[0]
    n_r_water_data = cursor.execute(f'''
    SELECT 
    n_r_water.area_ha,
    n_r_water.area_percent,
    n_r_water.area_map, 
    n_r_water.date
    FROM n_r_water 
    WHERE n_r_water.id_country={self.global_config['mid_object'][1]} 
    and n_r_water.id_water_type=0 
    ORDER BY n_r_water.date DESC LIMIT 1;''').fetchall()[0]
#______________________________________________________________________________________________________________________
    """ Show close button """
    self.main_exit_button.setHidden(True)
    self.main_close_button.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Setup widget """
    if self.scroll_widget: # Check if main scroll has widget 
        self.scroll_widget.deleteLater() # Delete widget 
        self.scroll_widget = None  # Set dafault 
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.scroll_widget = QWidget(self.main_scroll)
    self.scroll_layout = QVBoxLayout(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Forests """
    self.n_r_forests_button = QPushButton(self.scroll_widget)
    self.n_r_forests_widget = QWidget(self.n_r_forests_button)
    self.n_r_forests_layout = QGridLayout(self.n_r_forests_widget)
    self.n_r_forests_title_label = QLabel(self.n_r_forests_widget)
    self.n_r_forests_map_label = QLabel(self.n_r_forests_widget)
    self.n_r_forests_statistics_widget = QWidget(self.n_r_forests_widget)
    self.n_r_forests_statistics_layout = QGridLayout(self.n_r_forests_statistics_widget)
    self.n_r_forests_area_ha_name_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_area_ha_value_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_area_percent_name_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_area_percent_value_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_logging_name_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_logging_value_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_growth_rate_name_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_growth_rate_value_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_market_value_name_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_market_value_value_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_date_name_label = QLabel(self.n_r_forests_statistics_widget)
    self.n_r_forests_date_value_label = QLabel(self.n_r_forests_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Agroculture """
    self.n_r_agroculture_button = QPushButton(self.scroll_widget)
    self.n_r_agroculture_widget = QWidget(self.n_r_agroculture_button)
    self.n_r_agroculture_layout = QGridLayout(self.n_r_agroculture_widget)
    self.n_r_agroculture_title_label = QLabel(self.n_r_agroculture_widget)
    self.n_r_agroculture_map_label = QLabel(self.n_r_agroculture_widget)
    self.n_r_agriculture_statistics_widget = QWidget(self.n_r_agroculture_widget)
    self.n_r_agriculture_statistics_layout = QGridLayout(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_area_ha_name_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_area_ha_value_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_area_percent_name_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_area_percent_value_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_harvastering_name_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_harvastering_value_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_market_value_name_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_market_value_value_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_date_name_label = QLabel(self.n_r_agriculture_statistics_widget)
    self.n_r_agriculture_date_value_label = QLabel(self.n_r_agriculture_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Minerals """
    self.n_r_minerals_button = QPushButton(self.scroll_widget)
    self.n_r_minerals_widget = QWidget(self.n_r_minerals_button)
    self.n_r_minerals_layout = QGridLayout(self.n_r_minerals_widget)
    self.n_r_minerals_title_label = QLabel(self.n_r_minerals_widget)
    self.n_r_minerals_map_label = QLabel(self.n_r_minerals_widget)
    self.n_r_minerals_statistics_widget = QWidget(self.n_r_minerals_widget)
    self.n_r_minerals_statistics_layout = QGridLayout(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_area_m3_name_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_area_m3_value_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_extraction_name_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_extraction_value_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_market_value_name_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_market_value_value_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_date_name_label = QLabel(self.n_r_minerals_statistics_widget)
    self.n_r_minerals_date_value_label = QLabel(self.n_r_minerals_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Water """
    self.n_r_water_button = QPushButton(self.scroll_widget)
    self.n_r_water_widget = QWidget(self.n_r_water_button)
    self.n_r_water_layout = QGridLayout(self.n_r_water_widget)
    self.n_r_water_title_label = QLabel(self.n_r_water_widget)
    self.n_r_water_map_label = QLabel(self.n_r_water_widget)
    self.n_r_water_statistics_widget = QWidget(self.n_r_water_widget)
    self.n_r_water_statistics_layout = QGridLayout(self.n_r_water_statistics_widget)
    self.n_r_water_area_ha_name_label = QLabel(self.n_r_water_statistics_widget)
    self.n_r_water_area_ha_value_label = QLabel(self.n_r_water_statistics_widget)
    self.n_r_water_area_percent_name_label = QLabel(self.n_r_water_statistics_widget)
    self.n_r_water_area_percent_value_label = QLabel(self.n_r_water_statistics_widget)
    self.n_r_water_date_name_label = QLabel(self.n_r_water_statistics_widget)
    self.n_r_water_date_value_label = QLabel(self.n_r_water_statistics_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.scroll_widget.setObjectName('scroll_widget')
    """ Forest """
    self.n_r_forests_button.setObjectName('n_r_forests_button')
    self.n_r_forests_widget.setObjectName('n_r_forests_widget')
    self.n_r_forests_title_label.setObjectName('n_r_forests_title_label')
    self.n_r_forests_map_label.setObjectName('n_r_forests_map_label')
    self.n_r_forests_statistics_widget.setObjectName('n_r_forests_statistics_widget')
    self.n_r_forests_area_ha_name_label.setObjectName('n_r_forests_area_ha_name_label')
    self.n_r_forests_area_ha_value_label.setObjectName('n_r_forests_area_ha_value_label')
    self.n_r_forests_area_percent_name_label.setObjectName('n_r_forests_area_percent_name_label')
    self.n_r_forests_area_percent_value_label.setObjectName('n_r_forests_area_percent_value_label')
    self.n_r_forests_logging_name_label.setObjectName('n_r_forests_logging_name_label')
    self.n_r_forests_logging_value_label.setObjectName('n_r_forests_logging_value_label')
    self.n_r_forests_growth_rate_name_label.setObjectName('n_r_forests_growth_rate_name_label')
    self.n_r_forests_growth_rate_value_label.setObjectName('n_r_forests_growth_rate_value_label')
    self.n_r_forests_market_value_name_label.setObjectName('n_r_forests_market_value_name_label')
    self.n_r_forests_market_value_value_label.setObjectName('n_r_forests_market_value_value_label')
    self.n_r_forests_date_name_label.setObjectName('n_r_forests_date_name_label')
    self.n_r_forests_date_value_label.setObjectName('n_r_forests_date_value_label')
    """ Agroculture """
    self.n_r_agroculture_button.setObjectName('n_r_agroculture_button')
    self.n_r_agroculture_widget.setObjectName('n_r_agroculture_widget')
    self.n_r_agroculture_title_label.setObjectName('n_r_agroculture_title_label')
    self.n_r_agroculture_map_label.setObjectName('n_r_agroculture_map_label')
    self.n_r_agriculture_statistics_widget.setObjectName('n_r_agriculture_statistics_widget')
    self.n_r_agriculture_area_ha_name_label.setObjectName('n_r_agriculture_area_ha_name_label')
    self.n_r_agriculture_area_ha_value_label.setObjectName('n_r_agriculture_area_ha_value_label')
    self.n_r_agriculture_area_percent_name_label.setObjectName('n_r_agriculture_area_percent_name_label')
    self.n_r_agriculture_area_percent_value_label.setObjectName('n_r_agriculture_area_percent_value_label')
    self.n_r_agriculture_harvastering_name_label.setObjectName('n_r_agriculture_harvastering_name_label')
    self.n_r_agriculture_harvastering_value_label.setObjectName('n_r_agriculture_harvastering_value_label')
    self.n_r_agriculture_market_value_name_label.setObjectName('n_r_agriculture_market_value_name_label')
    self.n_r_agriculture_market_value_value_label.setObjectName('n_r_agriculture_market_value_value_label')
    self.n_r_agriculture_date_name_label.setObjectName('n_r_agriculture_date_name_label')
    self.n_r_agriculture_date_value_label.setObjectName('n_r_agriculture_date_value_label')
    """ Minerals """
    self.n_r_minerals_button.setObjectName('n_r_minerals_button')
    self.n_r_minerals_widget.setObjectName('n_r_minerals_widget')
    self.n_r_minerals_title_label.setObjectName('n_r_minerals_title_label')
    self.n_r_minerals_map_label.setObjectName('n_r_minerals_map_label')
    self.n_r_minerals_statistics_widget.setObjectName('n_r_minerals_statistics_widget')
    self.n_r_minerals_area_m3_name_label.setObjectName('n_r_minerals_area_m3_name_label')
    self.n_r_minerals_area_m3_value_label.setObjectName('n_r_minerals_area_m3_value_label')
    self.n_r_minerals_extraction_name_label.setObjectName('n_r_minerals_extraction_name_label')
    self.n_r_minerals_extraction_value_label.setObjectName('n_r_minerals_extraction_value_label')
    self.n_r_minerals_market_value_name_label.setObjectName('n_r_minerals_market_value_name_label')
    self.n_r_minerals_market_value_value_label.setObjectName('n_r_minerals_market_value_value_label')
    self.n_r_minerals_date_name_label.setObjectName('n_r_minerals_date_name_label')
    self.n_r_minerals_date_value_label.setObjectName('n_r_minerals_date_value_label')
    """ Water """
    self.n_r_water_button.setObjectName('n_r_water_button')
    self.n_r_water_widget.setObjectName('n_r_water_widget')
    self.n_r_water_title_label.setObjectName('n_r_water_title_label')
    self.n_r_water_map_label.setObjectName('n_r_water_map_label')
    self.n_r_water_statistics_widget.setObjectName('n_r_water_statistics_widget')
    self.n_r_water_area_ha_name_label.setObjectName('n_r_water_area_ha_name_label')
    self.n_r_water_area_ha_value_label.setObjectName('n_r_water_area_ha_value_label')
    self.n_r_water_area_percent_name_label.setObjectName('n_r_water_area_percent_name_label')
    self.n_r_water_area_percent_value_label.setObjectName('n_r_water_area_percent_value_label')
    self.n_r_water_date_name_label.setObjectName('n_r_water_date_name_label')
    self.n_r_water_date_value_label.setObjectName('n_r_water_date_value_label')
#______________________________________________________________________________________________________________________
    """ Set property """
    """ Forests """
    self.n_r_forests_button.setProperty('class', 'n_r_button')
    self.n_r_forests_widget.setProperty('class', 'n_r_widget')
    self.n_r_forests_title_label.setProperty('class', 'n_r_title_label')
    self.n_r_forests_map_label.setProperty('class', 'n_r_map_label')
    self.n_r_forests_statistics_widget.setProperty('class', 'n_r_statistics_widget')
    self.n_r_forests_area_ha_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_forests_area_ha_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_forests_area_percent_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_forests_area_percent_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_forests_logging_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_forests_logging_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_forests_growth_rate_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_forests_growth_rate_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_forests_market_value_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_forests_market_value_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_forests_date_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_forests_date_value_label.setProperty('class', 'n_r_value_label')
    """ Agroculture """
    self.n_r_agroculture_button.setProperty('class', 'n_r_button')
    self.n_r_agroculture_title_label.setProperty('class', 'n_r_widget')
    self.n_r_agroculture_title_label.setProperty('class', 'n_r_title_label')
    self.n_r_agroculture_map_label.setProperty('class', 'n_r_map_label')
    self.n_r_agriculture_statistics_widget.setProperty('class', 'n_r_statistics_widget')
    self.n_r_agriculture_area_ha_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_agriculture_area_ha_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_agriculture_area_percent_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_agriculture_area_percent_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_agriculture_harvastering_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_agriculture_harvastering_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_agriculture_market_value_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_agriculture_market_value_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_agriculture_date_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_agriculture_date_value_label.setProperty('class', 'n_r_value_label')
    """ Minerals """
    self.n_r_minerals_button.setProperty('class', 'n_r_button')
    self.n_r_minerals_widget.setProperty('class', 'n_r_widget')
    self.n_r_minerals_title_label.setProperty('class', 'n_r_title_label')
    self.n_r_minerals_map_label.setProperty('class', 'n_r_map_label')
    self.n_r_minerals_statistics_widget.setProperty('class', 'n_r_statistics_widget')
    self.n_r_minerals_area_m3_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_minerals_area_m3_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_minerals_extraction_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_minerals_extraction_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_minerals_market_value_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_minerals_market_value_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_minerals_date_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_minerals_date_value_label.setProperty('class', 'n_r_value_label')
    """ Water """
    self.n_r_water_button.setProperty('class', 'n_r_button')
    self.n_r_water_widget.setProperty('class', 'n_r_widget')
    self.n_r_water_title_label.setProperty('class', 'n_r_title_label')
    self.n_r_water_map_label.setProperty('class', 'n_r_map_label')
    self.n_r_water_statistics_widget.setProperty('class', 'n_r_statistics_widget')
    self.n_r_water_area_ha_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_water_area_ha_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_water_area_percent_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_water_area_percent_value_label.setProperty('class', 'n_r_value_label')
    self.n_r_water_date_name_label.setProperty('class', 'n_r_name_label')
    self.n_r_water_date_value_label.setProperty('class', 'n_r_value_label')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.scroll_layout.addWidget(self.n_r_forests_button)
    self.scroll_layout.addWidget(self.n_r_agroculture_button)
    self.scroll_layout.addWidget(self.n_r_minerals_button)
    self.scroll_layout.addWidget(self.n_r_water_button)
    self.scroll_layout.setSpacing(0)
    self.scroll_layout.setContentsMargins(0,0,0,0)
    self.scroll_widget.setLayout(self.scroll_layout)
    """ Forests """
    self.n_r_forests_layout.addWidget(self.n_r_forests_title_label, 0, 0, 20, 100)
    self.n_r_forests_layout.addWidget(self.n_r_forests_map_label, 20, 5, 80, 30)
    self.n_r_forests_layout.addWidget(self.n_r_forests_statistics_widget, 20, 55, 60, 40)
    self.n_r_forests_layout.setSpacing(0)
    self.n_r_forests_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.n_r_forests_layout.setRowStretch(enc, 1)
        self.n_r_forests_layout.setColumnStretch(enc, 1)
    self.n_r_forests_widget.setLayout(self.n_r_forests_layout)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_area_ha_name_label, 0, 0)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_area_ha_value_label, 0, 1)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_area_percent_name_label, 1, 0)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_area_percent_value_label, 1, 1)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_logging_name_label, 2, 0)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_logging_value_label, 2, 1)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_growth_rate_name_label, 3, 0)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_growth_rate_value_label, 3, 1)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_market_value_name_label, 4, 0)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_market_value_value_label, 4, 1)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_date_name_label, 5, 0)
    self.n_r_forests_statistics_layout.addWidget(self.n_r_forests_date_value_label, 5, 1)
    self.n_r_forests_statistics_layout.setSpacing(0)
    self.n_r_forests_statistics_layout.setContentsMargins(0,0,0,0)
    self.n_r_forests_statistics_widget.setLayout(self.n_r_forests_statistics_layout)
    """ Agroculture """
    self.n_r_agroculture_layout.addWidget(self.n_r_agroculture_title_label, 0, 0, 20, 100)
    self.n_r_agroculture_layout.addWidget(self.n_r_agroculture_map_label, 20, 5, 80, 30)
    self.n_r_agroculture_layout.addWidget(self.n_r_agriculture_statistics_widget, 20, 55, 60, 40)
    self.n_r_agroculture_layout.setSpacing(0)
    self.n_r_agroculture_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.n_r_agroculture_layout.setRowStretch(enc, 1)
        self.n_r_agroculture_layout.setColumnStretch(enc, 1)
    self.n_r_agroculture_widget.setLayout(self.n_r_agroculture_layout)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_area_ha_name_label, 0, 0)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_area_ha_value_label, 0, 1)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_area_percent_name_label, 1, 0)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_area_percent_value_label, 1, 1)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_harvastering_name_label, 2, 0)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_harvastering_value_label, 2, 1)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_market_value_name_label, 3, 0)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_market_value_value_label, 3, 1)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_date_name_label, 4, 0)
    self.n_r_agriculture_statistics_layout.addWidget(self.n_r_agriculture_date_value_label, 4, 1)
    self.n_r_agriculture_statistics_layout.setSpacing(0)
    self.n_r_agriculture_statistics_layout.setContentsMargins(0,0,0,0)
    self.n_r_agriculture_statistics_widget.setLayout(self.n_r_agriculture_statistics_layout)
    """ Minerals """
    self.n_r_minerals_layout.addWidget(self.n_r_minerals_title_label, 0, 0, 20, 100)
    self.n_r_minerals_layout.addWidget(self.n_r_minerals_map_label, 20, 5, 80, 30)
    self.n_r_minerals_layout.addWidget(self.n_r_minerals_statistics_widget, 20, 55, 60, 40)
    self.n_r_minerals_layout.setSpacing(0)
    self.n_r_minerals_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.n_r_minerals_layout.setRowStretch(enc, 1)
        self.n_r_minerals_layout.setColumnStretch(enc, 1)
    self.n_r_minerals_widget.setLayout(self.n_r_minerals_layout)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_area_m3_name_label, 0, 0)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_area_m3_value_label, 0, 1)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_extraction_name_label, 1, 0)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_extraction_value_label, 1, 1)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_market_value_name_label, 2, 0)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_market_value_value_label, 2, 1)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_date_name_label, 3, 0)
    self.n_r_minerals_statistics_layout.addWidget(self.n_r_minerals_date_value_label, 3, 1)
    self.n_r_minerals_statistics_layout.setSpacing(0)
    self.n_r_minerals_statistics_layout.setContentsMargins(0,0,0,0)
    self.n_r_minerals_statistics_widget.setLayout(self.n_r_minerals_statistics_layout)
    """ Water """
    self.n_r_water_layout.addWidget(self.n_r_water_title_label, 0, 0, 20, 100)
    self.n_r_water_layout.addWidget(self.n_r_water_map_label, 20, 5, 80, 30)
    self.n_r_water_layout.addWidget(self.n_r_water_statistics_widget, 20, 55, 60, 40)
    self.n_r_water_layout.setSpacing(0)
    self.n_r_water_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.n_r_water_layout.setRowStretch(enc, 1)
        self.n_r_water_layout.setColumnStretch(enc, 1)
    self.n_r_water_widget.setLayout(self.n_r_water_layout)
    self.n_r_water_statistics_layout.addWidget(self.n_r_water_area_ha_name_label, 0, 0)
    self.n_r_water_statistics_layout.addWidget(self.n_r_water_area_ha_value_label, 0, 1)
    self.n_r_water_statistics_layout.addWidget(self.n_r_water_area_percent_name_label, 1, 0)
    self.n_r_water_statistics_layout.addWidget(self.n_r_water_area_percent_value_label, 1, 1)
    self.n_r_water_statistics_layout.addWidget(self.n_r_water_date_name_label, 2, 0)
    self.n_r_water_statistics_layout.addWidget(self.n_r_water_date_value_label, 2, 1)
    self.n_r_water_statistics_layout.setSpacing(0)
    self.n_r_water_statistics_layout.setContentsMargins(0,0,0,0)
    self.n_r_water_statistics_widget.setLayout(self.n_r_water_statistics_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.main_scroll.setWidget(self.scroll_widget)
    self.n_r_forests_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
    self.n_r_forests_statistics_widget.setAttribute(Qt.WA_TransparentForMouseEvents)    
    self.n_r_agroculture_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
    self.n_r_agriculture_statistics_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
    self.n_r_minerals_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
    self.n_r_minerals_statistics_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
    self.n_r_water_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
    self.n_r_water_statistics_widget.setAttribute(Qt.WA_TransparentForMouseEvents)
#______________________________________________________________________________________________________________________
    """ Set label """
    """ Forests """
    self.n_r_forests_title_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_area_ha_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_area_ha_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_area_percent_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_area_percent_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_logging_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_logging_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_growth_rate_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_growth_rate_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_market_value_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_market_value_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_date_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_forests_date_value_label.setAlignment(Qt.AlignCenter)
    """ Agroculture """
    self.n_r_agroculture_title_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_area_ha_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_area_ha_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_area_percent_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_area_percent_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_harvastering_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_harvastering_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_market_value_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_market_value_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_date_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_agriculture_date_value_label.setAlignment(Qt.AlignCenter)
    """ Minerals """
    self.n_r_minerals_title_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_area_m3_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_area_m3_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_extraction_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_extraction_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_market_value_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_market_value_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_date_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_minerals_date_value_label.setAlignment(Qt.AlignCenter)
    """ Water """
    self.n_r_water_title_label.setAlignment(Qt.AlignCenter)
    self.n_r_water_area_ha_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_water_area_ha_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_water_area_percent_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_water_area_percent_value_label.setAlignment(Qt.AlignCenter)
    self.n_r_water_date_name_label.setAlignment(Qt.AlignCenter)
    self.n_r_water_date_value_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size  """
    self.scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Forests """
    self.n_r_forests_button.setFixedHeight(self.main_scroll.height())
    self.n_r_forests_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_widget.setGeometry(QRect(0, 0, self.n_r_forests_button.width(), self.n_r_forests_button.height()))
    self.n_r_forests_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_map_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_area_ha_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_area_ha_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_area_percent_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_area_percent_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_logging_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_logging_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_growth_rate_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_growth_rate_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_market_value_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_market_value_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_forests_date_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Agroculture """
    self.n_r_agroculture_button.setFixedHeight(self.main_scroll.height())
    self.n_r_agroculture_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agroculture_widget.setGeometry(QRect(0, 0, self.n_r_agroculture_button.width(), self.n_r_agroculture_button.height()))
    self.n_r_agroculture_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agroculture_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agroculture_map_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_area_ha_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_area_ha_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_area_percent_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_area_percent_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_harvastering_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_harvastering_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_market_value_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_market_value_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_agriculture_date_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Minerals """
    self.n_r_minerals_button.setFixedHeight(self.main_scroll.height())
    self.n_r_minerals_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_widget.setGeometry(QRect(0, 0, self.n_r_minerals_button.width(), self.n_r_minerals_button.height()))
    self.n_r_minerals_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_map_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_area_m3_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_area_m3_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_extraction_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_extraction_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_market_value_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_market_value_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_minerals_date_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Water """
    self.n_r_water_button.setFixedHeight(self.main_scroll.height())
    self.n_r_water_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_widget.setGeometry(QRect(0, 0, self.n_r_water_button.width(), self.n_r_water_button.height()))
    self.n_r_water_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_map_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_area_ha_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_area_ha_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_area_percent_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_area_percent_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_water_date_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    """ Forests """
    self.n_r_forests_title_label.setText('Forests')
    self.n_r_forests_area_ha_name_label.setText('Area in hectars:')
    self.n_r_forests_area_ha_value_label.setText(f'{n_r_forests_data[0]}')
    self.n_r_forests_area_percent_name_label.setText('Area in percent:')
    self.n_r_forests_area_percent_value_label.setText(f'{n_r_forests_data[1]}')
    self.n_r_forests_logging_name_label.setText('Logging:')
    self.n_r_forests_logging_value_label.setText(f'{n_r_forests_data[3]}')
    self.n_r_forests_growth_rate_name_label.setText('Growth rate:')
    self.n_r_forests_growth_rate_value_label.setText(f'{n_r_forests_data[4]}')
    self.n_r_forests_market_value_name_label.setText('Market value:')
    self.n_r_forests_market_value_value_label.setText(f'{n_r_forests_data[5]}')
    self.n_r_forests_date_name_label.setText('Date:')
    self.n_r_forests_date_value_label.setText(f'{n_r_forests_data[6]}')
    """ Agroculture """
    self.n_r_agroculture_title_label.setText('Agroculture')
    self.n_r_agriculture_area_ha_name_label.setText('Area in hectars:')
    self.n_r_agriculture_area_ha_value_label.setText(f'{n_r_agriculture_data[0]}')
    self.n_r_agriculture_area_percent_name_label.setText('Area in percent:')
    self.n_r_agriculture_area_percent_value_label.setText(f'{n_r_agriculture_data[1]}')
    self.n_r_agriculture_harvastering_name_label.setText('Harvastering:')
    self.n_r_agriculture_harvastering_value_label.setText(f'{n_r_agriculture_data[3]}')
    self.n_r_agriculture_market_value_name_label.setText('Market value:')
    self.n_r_agriculture_market_value_value_label.setText(f'{n_r_agriculture_data[4]}')
    self.n_r_agriculture_date_name_label.setText('Date:')
    self.n_r_agriculture_date_value_label.setText(f'{n_r_agriculture_data[5]}')
    """ Minerals """
    self.n_r_minerals_title_label.setText('Minerals')
    self.n_r_minerals_area_m3_name_label.setText('Area m3:')
    self.n_r_minerals_area_m3_value_label.setText(f'{n_r_minerals_data[0]}')
    self.n_r_minerals_extraction_name_label.setText('Extraction:')
    self.n_r_minerals_extraction_value_label.setText(f'{n_r_minerals_data[2]}')
    self.n_r_minerals_market_value_name_label.setText('Market value:')
    self.n_r_minerals_market_value_value_label.setText(f'{n_r_minerals_data[3]}')
    self.n_r_minerals_date_name_label.setText('Date:')
    self.n_r_minerals_date_value_label.setText(f'{n_r_minerals_data[4]}')
    """ Water """
    self.n_r_water_title_label.setText('Water')
    self.n_r_water_area_ha_name_label.setText('Area in hectars:')
    self.n_r_water_area_ha_value_label.setText(f'{n_r_water_data[0]}')
    self.n_r_water_area_percent_name_label.setText('Area in percent:')
    self.n_r_water_area_percent_value_label.setText(f'{n_r_water_data[1]}')
    self.n_r_water_date_name_label.setText('Date:')
    self.n_r_water_date_value_label.setText(f'{n_r_water_data[3]}')
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.n_r_forests_map_label.setPixmap(load_svg(self.main_path+'/TickerK8_app/APP_FILES/STYLE/IMG/map_forests'+n_r_forests_data[2]+f'/{self.global_config['__theme__']}.svg', int(self.n_r_forests_widget.height()//1.25), int(self.n_r_forests_widget.height()//1.25)))
    self.n_r_agroculture_map_label.setPixmap(load_svg(self.main_path+'/TickerK8_app/APP_FILES/STYLE/IMG/map_agriculture'+n_r_agriculture_data[2]+f'/{self.global_config['__theme__']}.svg', int(self.n_r_agroculture_widget.height()//1.25), int(self.n_r_agroculture_widget.height()//1.25)))
    self.n_r_minerals_map_label.setPixmap(load_svg(self.main_path+'/TickerK8_app/APP_FILES/STYLE/IMG/map_minerals'+n_r_minerals_data[1]+f'/{self.global_config['__theme__']}.svg', int(self.n_r_minerals_widget.height()//1.25), int(self.n_r_minerals_widget.height()//1.25)))
    self.n_r_water_map_label.setPixmap(load_svg(self.main_path+'/TickerK8_app/APP_FILES/STYLE/IMG/map_water'+n_r_water_data[2]+f'/{self.global_config['__theme__']}.svg', int(self.n_r_water_widget.height()//1.25), int(self.n_r_water_widget.height()//1.25)))
#######################################################################################################################
""" Open people """
def open_people(self):
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
