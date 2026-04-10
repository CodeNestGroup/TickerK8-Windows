""" Import """
import json # For json files
import sqlite3 # For database data 
from PyQt5.QtWidgets import (
    QWidget,
    QTableWidget,
    QComboBox,
    QLabel,
    QPushButton,
    QGridLayout,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QGraphicsTextItem,
    QSizePolicy
)
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont, QColor
from PyQt5.QtCore import QRectF, Qt, QPointF
#______________________________________________________________________________________________________________________
""" Charts types import """
from .candle_chart import Candle_chart
#######################################################################################################################
""" Create chart """
def create_chart(self):
    """ Get data """
    chart_object = self.global_config['mid_object']
    chart_data = list(json.load(open(self.main_path+'/test_chart_data/AGX100/agx100_1min.json', 'r', encoding='utf-8')))
    _background_config = self.background_config # Get background config
    _chart_config = self.chart_config # Get chart config
#______________________________________________________________________________________________________________________
    """ Object info data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    object_data = cursor.execute(f'SELECT name FROM {chart_object[0]} WHERE id={chart_object[1]};').fetchall()[0] # Get data 
    cursor.close() # Close cursor connection  
    database.close() # Close database connection
#______________________________________________________________________________________________________________________
    """ Create and set scene """
    self.main_chart_graphics_scene = QGraphicsScene(self.main_chart_graphics_view) # Create scene 
    self.main_chart_graphics_scene.setObjectName('main_chart_graphics_scene') # Set scene name
    self.main_chart_graphics_view.setScene(self.main_chart_graphics_scene) # Set scene to view
    self.main_chart_graphics_view.setBackgroundBrush(QColor(_background_config['background_color'])) # Set background color for view
    """ Get size of scene """
    _scene_width = int((len(chart_data)*(_chart_config['size']+_chart_config['x_offest']))+250) # Width in int
    _scene_height = 864 # Height in int
    self.main_chart_graphics_scene.setSceneRect(0, 0, _scene_width, _scene_height) # Set scene rect 
    """ Get time range """
    start_time, stop_time, interval = chart_data[0]['d'][10:], chart_data[-1]['d'][10:], chart_data[0]['i'][:-1] # Get start, stop and interval time
    """ Get price range """
    price_list = [] 
    max_price = int
    min_price = int 
    for s in chart_data: price_list += [s['h'], s['l']]# Loop for data, serch highest and lowest price
    max_price, min_price = max(price_list), min(price_list) # Get highest, lowest price 
#______________________________________________________________________________________________________________________
    """ Create no more data info """
    no_more_data_item = QGraphicsTextItem("No more data")
    no_more_data_item.setFont(QFont("Arial", 20))
    no_more_data_item.setDefaultTextColor(QColor(_background_config['net_color']))
    no_more_data_item.setPos(10, int((_scene_height//2)-10))
    self.main_chart_graphics_scene.addItem(no_more_data_item)
#______________________________________________________________________________________________________________________
    """ Create grid, scale time """
    if _background_config['net_type'] == 1 or _background_config['net_type'] == 3:
        pen = QPen(QColor(_background_config['net_color']))
        _x_pos = 250
        for line in chart_data[::10]:
            _date_text = line['d'][10:16]
            self.main_chart_graphics_scene.addLine(_x_pos, 0, _x_pos,int(_scene_height-20), QColor(_background_config['net_color']))
            self.main_chart_graphics_scene.addText(_date_text).setPos(_x_pos-35, _scene_height-10)
            _x_pos += int((_chart_config['size']+_chart_config['x_offest'])*10)



#______________________________________________________________________________________________________________________
    """ Create price chart """
#______________________________________________________________________________________________________________________
    """ Create vol chart """
#______________________________________________________________________________________________________________________
    """ Set char title """
    self.top_title_label.setText(f'{object_data[0]}')
#######################################################################################################################
""" Settings """
def settings_widget(self):
    """ Config data """
    _main_config = self.main_config
    _sheets = self.sheets
    _background_config = self.background_config
    _chart_config = self.chart_config
    _price_config = self.price_config
    _volume_config = self.volume_config if self.volume_config else None
    _translate = self.chart_translate
    _language = self.global_config['__language__']
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.settings_background_widget = QWidget(self)
    self.settings_background_layout = QGridLayout(self.settings_background_widget)
    self.settings_widget = QWidget(self.settings_background_widget)
    self.settings_layout = QGridLayout(self.settings_widget)
    self.settings_title_label = QLabel(self.settings_widget)
    self.settings_tab_widget = QTabWidget(self.settings_widget)
    self.settings_theme_widget = QWidget(self.settings_tab_widget)
    self.settings_theme_layout = QGridLayout(self.settings_theme_widget)
    self.settings_theme_label = QLabel(self.settings_theme_widget)
    self.settings_theme_combo = QComboBox(self.settings_theme_widget)
    self.settings_background_background_widget = QWidget(self.settings_tab_widget)
    self.settings_background_background_layout = QGridLayout(self.settings_background_background_widget)
    self.settings_background_background_exemple_item = QGraphicsItem(self.settings_background_background_widget)
    self.settings_background_background_color_label = QLabel(self.settings_background_background_widget)
    self.settings_background_background_color_line = QLineEdit(self.settings_background_background_widget)
    self.settings_background_net_type_label = QLabel(self.settings_background_background_widget)
    self.settings_background_net_type_combo = QComboBox(self.settings_background_background_widget)
    self.settings_background_net_color_label = QLabel(self.settings_background_background_widget)
    self.settings_background_net_color_line = QLineEdit(self.settings_background_background_widget)
    self.settings_price_widget = QWidget(self.settings_tab_widget)
    self.settings_price_layout = QGridLayout(self.settings_price_widget)
    self.settings_price_exemple_item = QGraphicsItem(self.settings_price_widget)
    self.settings_price_background_color_label = QLabel(self.settings_price_widget)
    self.settings_price_background_color_line = QLineEdit(self.settings_price_widget)
    self.settings_price_font_color_label = QLabel(self.settings_price_widget)
    self.settings_price_font_color_line = QLineEdit(self.settings_price_widget)
    self.settings_price_font_size_label = QLabel(self.settings_price_widget)
    self.settings_price_font_size_line = QLineEdit(self.settings_price_widget)
    self.settings_candle_widget = QWidget(self.settings_tab_widget)
    self.settings_candle_layout = QGridLayout(settings_candle_widget)
    self.settings_candle_exemple_p_item = QGraphicsItem(settings_candle_widget)
    self.settings_candle_exemple_m_item = QGraphicsItem(settings_candle_widget)
    self.settings_candle_size_label = QLabel(settings_candle_widget)
    self.settings_candle_size_line = QLineEdit(settings_candle_widget)
    self.settings_candle_border_label = QLabel(settings_candle_widget)
    self.settings_candle_p_border_line = QLineEdit(settings_candle_widget)
    self.settings_candle_m_border_line = QLineEdit(settings_candle_widget)
    self.settings_candle_fill_label = QLabel(settings_candle_widget)
    self.settings_candle_p_fill_line = QLineEdit(settings_candle_widget)
    self.settings_candle_m_fill_line = QLineEdit(settings_candle_widget)
    self.settings_vol_widget = QWidget(self.settings_tab_widget)
    self.settings_vol_layout = QGridLayout(self.settings_vol_widget)
    self.settings_vol_exemple_p_item = QGraphicsItem(self.settings_vol_widget)
    self.settings_vol_exemple_m_item = QGraphicsItem(self.settings_vol_widget)
    self.settings_vol_size_label = QLabel(self.settings_vol_widget)
    self.settings_vol_size_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_border_label = QLabel(self.settings_vol_widget)
    self.settings_vol_p_border_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_m_border_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_fill_label = QLabel(self.settings_vol_widget)
    self.settings_vol_p_fill_line = QLineEdit(self.settings_vol_widget)
    self.settings_vol_m_fill_line = QLineEdit(self.settings_vol_widget)
    self.settings_exit_button = QPushButton(self.settings_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.settings_background_widget.setObjectName('settings_background_widget')
    self.settings_widget.setObjectName('settings_widget')
    self.settings_title_label.setObjectName('settings_title_label')
    self.settings_tab_widget.setObjectName('settings_tab_widget')
    self.settings_theme_widget.setObjectName('settings_theme_widget')
    self.settings_theme_label.setObjectName('settings_theme_label')
    self.settings_theme_combo.setObjectName('settings_theme_combo')
    self.settings_background_background_widget.setObjectName('settings_background_background_widget')
    self.settings_background_background_exemple_item.setObjectName('settings_background_background_exemple_item')
    self.settings_background_background_color_label.setObjectName('settings_background_background_color_label')
    self.settings_background_background_color_line.setObjectName('settings_background_background_color_line')
    self.settings_background_net_type_label.setObjectName('settings_background_net_type_label')
    self.settings_background_net_type_combo.setObjectName('settings_background_net_type_combo')
    self.settings_background_net_color_label.setObjectName('settings_background_net_color_label')
    self.settings_background_net_color_line.setObjectName('settings_background_net_color_line')
    self.settings_price_widget.setObjectName('settings_price_widget')
    self.settings_price_exemple_item.setObjectName('settings_price_exemple_item')
    self.settings_price_background_color_label.setObjectName('settings_price_background_color_label')
    self.settings_price_background_color_line.setObjectName('settings_price_background_color_line')
    self.settings_price_font_color_label.setObjectName('settings_price_font_color_label')
    self.settings_price_font_color_line.setObjectName('settings_price_font_color_line')
    self.settings_price_font_size_label.setObjectName('settings_price_font_size_label')
    self.settings_price_font_size_line.setObjectName('settings_price_font_size_line')
    self.settings_candle_widget.setObjectName('settings_candle_widget')
    self.settings_candle_exemple_p_item.setObjectName('settings_candle_exemple_p_item')
    self.settings_candle_exemple_m_item.setObjectName('settings_candle_exemple_m_item')
    self.settings_candle_size_label.setObjectName('settings_candle_size_label')
    self.settings_candle_size_line.setObjectName('settings_candle_size_line')
    self.settings_candle_border_label.setObjectName('settings_candle_border_label')
    self.settings_candle_p_border_line.setObjectName('settings_candle_p_border_line')
    self.settings_candle_m_border_line.setObjectName('settings_candle_m_border_line')
    self.settings_candle_fill_label.setObjectName('settings_candle_fill_label')
    self.settings_candle_p_fill_line.setObjectName('settings_candle_p_fill_line')
    self.settings_candle_m_fill_line.setObjectName('settings_candle_m_fill_line')
    self.settings_vol_widget.setObjectName('settings_vol_widget')
    self.settings_vol_exemple_p_item.setObjectName('settings_vol_exemple_p_item')
    self.settings_vol_exemple_m_item.setObjectName('settings_vol_exemple_m_item')
    self.settings_vol_size_label.setObjectName('settings_vol_size_label')
    self.settings_vol_size_line.setObjectName('settings_vol_size_line')
    self.settings_vol_border_label.setObjectName('settings_vol_border_label')
    self.settings_vol_p_border_line.setObjectName('settings_vol_p_border_line')
    self.settings_vol_m_border_line.setObjectName('settings_vol_m_border_line')
    self.settings_vol_fill_label.setObjectName('settings_vol_fill_label')
    self.settings_vol_p_fill_line.setObjectName('settings_vol_p_fill_line')
    self.settings_vol_m_fill_line.setObjectName('settings_vol_m_fill_line')
    self.settings_exit_button.setObjectName('settings_exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.settings_theme_widget.setProperty('class', 'settings_sub_widget')
    self.settings_theme_label.setProperty('class', 'settings_label')
    self.settings_background_background_widget.setProperty('class', 'settings_sub_widget')
    self.settings_background_background_color_label.setProperty('class', 'settings_label')
    self.settings_background_background_color_line.setProperty('class', 'settings_line')
    self.settings_background_net_type_label.setProperty('class', 'settings_label')
    self.settings_background_net_color_label.setProperty('class', 'settings_label')
    self.settings_background_net_color_line.setProperty('class', 'settings_line')
    self.settings_price_widget.setProperty('class', 'settings_sub_widget')
    self.settings_price_background_color_label.setProperty('class', 'settings_label')
    self.settings_price_background_color_line.setProperty('class', 'settings_line')
    self.settings_price_font_color_label.setProperty('class', 'settings_label')
    self.settings_price_font_color_line.setProperty('class', 'settings_line')
    self.settings_price_font_size_label.setProperty('class', 'settings_label')
    self.settings_price_font_size_line.setProperty('class', 'settings_line')
    self.settings_candle_widget.setProperty('class', 'settings_sub_widget')
    self.settings_candle_size_label.setProperty('class', 'settings_label')
    self.settings_candle_size_line.setProperty('class', 'settings_line')
    self.settings_candle_border_label.setProperty('class', 'settings_label')
    self.settings_candle_p_border_line.setProperty('class', 'settings_line')
    self.settings_candle_m_border_line.setProperty('class', 'settings_line')
    self.settings_candle_fill_label.setProperty('class', 'settings_label')
    self.settings_candle_p_fill_line.setProperty('class', 'settings_line')
    self.settings_candle_m_fill_line.setProperty('class', 'settings_line')
    self.settings_vol_widget.setProperty('class', 'settings_sub_widget')
    self.settings_vol_size_label.setProperty('class', 'settings_label')
    self.settings_vol_size_line.setProperty('class', 'settings_line')
    self.settings_vol_border_label.setProperty('class', 'settings_label')
    self.settings_vol_p_border_line.setProperty('class', 'settings_line')
    self.settings_vol_m_border_line.setProperty('class', 'settings_line')
    self.settings_vol_fill_label.setProperty('class', 'settings_label')
    self.settings_vol_p_fill_line.setProperty('class', 'settings_line')
    self.settings_vol_m_fill_line.setProperty('class', 'settings_line')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.settings_background_layout.addWidget(self.settings_widget, 25, 25, 50, 50)
    self.settings_background_layout.setSpacing(0)
    self.settings_background_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.settings_background_layout.setRowStretch(enc, 1)
        self.settings_background_layout.setColumnStretch(enc, 1)
    self.settings_background_widget.setLayout(self.settings_background_layout)
    self.settings_layout.addWidget(self.settings_title_label, 5, 0, 10, 100)
    self.settings_layout.addWidget(self.settings_tab_widget, 20, 0, 65, 100)
    self.settings_layout.addWidget(self.settings_exit_button, 90, 40, 5, 20)
    self.settings_layout.setSpacing(0)
    self.settings_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.settings_layout.setRowStretch(enc, 1)
        self.settings_layout.setColumnStretch(enc, 1)
    self.settings_widget.setLayout(self.settings_layout)
    self.settings_theme_layout.addWidget(self.settings_theme_label, 0, 0)
    self.settings_theme_layout.addWidget(self.settings_theme_combo, 0, 1)
    self.settings_theme_layout.setSpacing(0)
    self.settings_theme_layout.setContentsMargins(0,0,0,0)
    self.settings_theme_widget.setLayout(self.settings_theme_layout)
    self.settings_background_background_layout.addWidget(self.settings_background_background_exemple_item, 0, 0)
    self.settings_background_background_layout.addWidget(self.settings_background_background_color_label, 1, 0)
    self.settings_background_background_layout.addWidget(self.settings_background_background_color_line, 1, 1)
    self.settings_background_background_layout.addWidget(self.settings_background_net_type_label, 2, 0)
    self.settings_background_background_layout.addWidget(self.settings_background_net_type_combo, 2, 1)
    self.settings_background_background_layout.addWidget(self.settings_background_net_color_label, 3, 0)
    self.settings_background_background_layout.addWidget(self.settings_background_net_color_line, 3, 1)
    self.settings_background_background_layout.setSpacing(0)
    self.settings_background_background_layout.setContentsMargins(0,0,0,0)
    self.settings_background_background_widget.setLayout(self.settings_background_background_layout)
    self.settings_price_layout.addWidget(self.settings_price_exemple_item, 0, 0, 1, 2)
    self.settings_price_layout.addWidget(self.settings_price_background_color_label, 1, 0)
    self.settings_price_layout.addWidget(self.settings_price_background_color_line, 1, 1)
    self.settings_price_layout.addWidget(self.settings_price_font_color_label, 2, 0)
    self.settings_price_layout.addWidget(self.settings_price_font_color_line, 2, 1)
    self.settings_price_layout.addWidget(self.settings_price_font_size_label, 3, 0)
    self.settings_price_layout.addWidget(self.settings_price_font_size_line, 3, 1)
    self.settings_price_layout.setSpacing(0)
    self.settings_price_layout.setContentsMargins(0,0,0,0)
    self.settings_price_widget.setLayout(self.settings_price_layout)
    self.settings_candle_layout.addWidget(self.settings_candle_exemple_p_item, 0, 0)
    self.settings_candle_layout.addWidget(self.settings_candle_exemple_m_item, 0, 1)
    self.settings_candle_layout.addWidget(self.settings_candle_size_label, 1, 0)
    self.settings_candle_layout.addWidget(self.settings_candle_size_line, 1, 1)
    self.settings_candle_layout.addWidget(self.settings_candle_border_label, 2, 0)
    self.settings_candle_layout.addWidget(self.settings_candle_p_border_line, 2, 1)
    self.settings_candle_layout.addWidget(self.settings_candle_m_border_line, 2, 2)
    self.settings_candle_layout.addWidget(self.settings_candle_fill_label, 3, 0)
    self.settings_candle_layout.addWidget(self.settings_candle_p_fill_line, 3, 1)
    self.settings_candle_layout.addWidget(self.settings_candle_m_fill_line, 3, 2)
    self.settings_candle_layout.setSpacing(0)
    self.settings_candle_layout.setContentsMargins(0,0,0,0)
    self.settings_candle_widget.setLayout(self.settings_candle_layout)
    self.settings_vol_layout.addWidget(self.settings_vol_exemple_p_item, 0, 0)
    self.settings_vol_layout.addWidget(self.settings_vol_exemple_m_item, 0, 1)
    self.settings_vol_layout.addWidget(self.settings_vol_size_label, 1, 0)
    self.settings_vol_layout.addWidget(self.settings_vol_size_line, 1, 1)
    self.settings_vol_layout.addWidget(self.settings_vol_border_label, 2, 0)
    self.settings_vol_layout.addWidget(self.settings_vol_p_border_line, 2, 1)
    self.settings_vol_layout.addWidget(self.settings_vol_m_border_line, 2, 2)
    self.settings_vol_layout.addWidget(self.settings_vol_fill_label, 3, 0)
    self.settings_vol_layout.addWidget(self.settings_vol_p_fill_line, 3, 1)
    self.settings_vol_layout.addWidget(self.settings_vol_m_fill_line, 3, 2)
    self.settings_vol_layout.setSpacing(0)
    self.settings_vol_layout.setContentsMargins(0,0,0,0)
    self.settings_vol_widget.setLayout(self.settings_vol_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.settings_background_widget.setHidden(False)
    self.settings_tab_widget.addTab(self.settings_theme_widget, str(_t['settings_theme_widget'][_l]))
    self.settings_tab_widget.addTab(self.settings_background_background_widget, str(_t['settings_background_background_widget'][_l]))
    self.settings_tab_widget.addTab(self.settings_price_widget, str(_t['settings_price_widget'][_l]))
    self.settings_tab_widget.addTab(self.settings_candle_widget, str(_t['settings_candle_widget'][_l]))
    self.settings_tab_widget.addTab(self.settings_vol_widget, str(_t['settings_vol_widget'][_l]))
#______________________________________________________________________________________________________________________
    """ Set label """
    self.settings_title_label.setAlignment(Qt.AlignCenter)
    self.settings_theme_label.setAlignment(Qt.AlignCenter)
    self.settings_background_background_color_label.setAlignment(Qt.AlignCenter)
    self.settings_background_net_type_label.setAlignment(Qt.AlignCenter)
    self.settings_background_net_color_label.setAlignment(Qt.AlignCenter)
    self.settings_price_background_color_label.setAlignment(Qt.AlignCenter)
    self.settings_price_font_color_label.setAlignment(Qt.AlignCenter)
    self.settings_price_font_size_label.setAlignment(Qt.AlignCenter)
    self.settings_candle_size_label.setAlignment(Qt.AlignCenter)
    self.settings_candle_border_label.setAlignment(Qt.AlignCenter)
    self.settings_candle_fill_label.setAlignment(Qt.AlignCenter)
    self.settings_vol_size_label.setAlignment(Qt.AlignCenter)
    self.settings_vol_border_label.setAlignment(Qt.AlignCenter)
    self.settings_vol_fill_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
    self.settings_background_background_color_line.setText(_background_config['background_color'])
    #self.settings_background_background_color_line.textChanged.connect()
    self.settings_background_net_color_line.setText(_m['net_color'])
    #self.settings_background_net_color_line.textChanged.connect()
    self.settings_price_background_color_line.setText(_m['price_info_background_color'])
    #self.settings_price_background_color_line.textChanged.connect()
    self.settings_price_font_color_line.setText(_m['price_info_font_color'])
    #self.settings_price_font_color_line.textChanged.connect()
    self.settings_price_font_size_line.setText(_m['price_info_font_size'])
    #self.settings_price_font_size_line.textChanged.connect()
    self.settings_candle_size_line.setText(_m['size'])
    #self.settings_candle_size_line.textChanged.connect()
    self.settings_candle_p_border_line.setText(_m['+_border_color'])
    #self.settings_candle_p_border_line.textChanged.connect()
    self.settings_candle_m_border_line.setText(_m['-_border_color'])
    #self.settings_candle_m_border_line.textChanged.connect()
    self.settings_candle_p_fill_line.setText(_m['+_fill_color'])
    #self.settings_candle_p_fill_line.textChanged.connect()
    self.settings_candle_m_fill_line.setText(_m['-_fill_color'])
    #self.settings_candle_m_fill_line.textChanged.connect()
    self.settings_vol_size_line.setText(_m['size'])
    #self.settings_vol_size_line.textChanged.connect()
    self.settings_vol_p_border_line.setText(_m['+_border_color'])
    #self.settings_vol_p_border_line.textChanged.connect()
    self.settings_vol_m_border_line.setText(_m['-_border_color'])
    #self.settings_vol_m_border_line.textChanged.connect()
    self.settings_vol_p_fill_line.setText(_m['+_fill_color'])
    #self.settings_vol_p_fill_line.textChanged.connect()
    self.settings_vol_m_fill_line.setText(_m['-_fill_color'])
    #self.settings_vol_m_fill_line.textChanged.connect()
#______________________________________________________________________________________________________________________
    """ Set combo box """
    for theme in _sheets: self.settings_theme_combo.addItem(theme[_language])
    self.settings_theme_combo.setCurrentIndex(_main_config['theme'])
    #self.settings_theme_combo.currentIndexChanged.connect()
    for net in _translate['settings_background_net_type_combo']: self.settings_background_net_type_combo.addItem(net[_language])
    self.settings_background_net_type_combo.setCurrentIndex(_main_config['net'])
    #self.settings_theme_combo.currentIndexChanged.connect()
#______________________________________________________________________________________________________________________
    """ Set push button """
    self.settings_exit_button.clicked.connect(exit_settings_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.settings_background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_tab_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_background_exemple_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_background_color_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_background_color_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_net_type_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_net_type_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_net_color_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_background_net_color_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_exemple_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_background_color_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_background_color_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_font_color_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_font_color_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_font_size_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_price_font_size_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_exemple_p_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_exemple_m_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_size_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_size_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_border_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_p_border_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_m_border_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_fill_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_p_fill_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_candle_m_fill_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_exemple_p_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_exemple_m_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_size_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_size_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_border_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_p_border_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_m_border_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_fill_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_p_fill_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_vol_m_fill_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set translate """
    self.settings_title_label.setText(_t['settings_title_label'][_l])
    self.settings_theme_label.setText(_t['settings_theme_label'][_l])
    self.settings_background_background_color_label.setText(_t['settings_background_background_color_label'][_l])
    self.settings_background_net_type_label.setText(_t['settings_background_net_type_label'][_l])
    self.settings_background_net_color_label.setText(_t['settings_background_net_color_label'][_l])
    self.settings_price_background_color_label.setText(_t['settings_price_background_color_label'][_l])
    self.settings_price_font_color_label.setText(_t['settings_price_font_color_label'][_l])
    self.settings_price_font_size_label.setText(_t['settings_price_font_size_label'][_l])
    self.settings_candle_size_label.setText(_t['settings_candle_size_label'][_l])
    self.settings_candle_border_label.setText(_t['settings_candle_border_label'][_l])
    self.settings_candle_fill_label.setText(_t['settings_candle_fill_label'][_l])
    self.settings_vol_size_label.setText(_t['settings_vol_size_label'][_l])
    self.settings_vol_border_label.setText(_t['settings_vol_border_label'][_l])
    self.settings_vol_fill_label.setText(_t['settings_vol_fill_label'][_l])
    self.settings_exit_button.setText(_t['settings_exit_button'][_l])
#______________________________________________________________________________________________________________________

#######################################################################################################################
""" Save setting """
def save_setting(self, conf, file, var):
    with open(self.main_path+'/CONFIG/chart/{file}.json', 'w', encoding='utf-8') as _w:
        json.dump(conf, _w, indent=4)
    var = json.load(open(self.main_path+'/CONFIG/chart/{file}.json', 'r', encoding='utf-8'))
#######################################################################################################################
""" Exit settings widget """
def exit_settings_widget(self):
    self.settings_background_widget.deleteLater()
    self.settings_background_widget = None
    create_chart(self)
#######################################################################################################################
""" Full screan """
def full_screan(self):
    flag = self.main_config['full_screan']
    flag_neg != int(flag)
    self.top_widget.setHidden(flag) 
    self.bottom_widget.setHidden(flag)
    for enc in range(0, 10):
        self.main_layout.setColumnStretch(enc, flag)
    for enc in range(90, 100):
        self.main_layout.setColumnStretch(enc, flag)
    self.main_config['full_screan'] = flag_neg
    reload_main_config(self)
#######################################################################################################################
""" Reload main config """
def reload_main_config(self):
    with open(self.main_path+'/CONFIG/chart/main.json', 'w', encoding='utf-8') as _w:
        json.dump(self.main_config, _w, indent=4)
    self.main_config = json.load(open(self.main_path+'/CONFIG/chart/main.json', 'r', encoding='utf-8')) # Get main config data
#######################################################################################################################
