""" Import packages """
import json
import datetime
import sqlite3
import mysql
import requests
from io import BytesIO
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox,
    QGridLayout,
    QSizePolicy,
    QVBoxLayout
)
from PyQt5.QtCore import (
    Qt,
    QSize,
    QRect
)
from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QIcon,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
""" Import main modules """
from main_chart.structure import Main_chart
from main_news.structure import Main_news_widget
from main_news_list.structure import Main_news_list_widget
#______________________________________________________________________________________________________________________

def widget_background_painter(self):
    _colors = self.main_conf['background']
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    _x_1 = 0.0
    _x_2 = 1.0 
    """ Calculate index and precent """
    _now = datetime.datetime.now()
    _today_sec = _now.hour*3600+_now.minute*60+_now.second
    if _today_sec >=86400:
        _today_sec = 86399
    _index = _today_sec//8640
    _percent = (_today_sec/8640)-_index
    """ Set colors """
    if _percent <= 0.5:
        _x_1 = 1-(_percent*2)
        _x_2 = 1.0
        _alpha_1 = 'ff'
        _alpha_2 = f'{int(255 *(_percent / 0.5)):02X}'
        _color_0 = f'#ff{_colors[_index-1]}'
    else:
        _x_1 = 0.0
        _x_2 = 1-(_percent-0.5)*2
        _alpha_1 = f'{255-int(255 *(_percent - 0.5) / 0.5):02X}'
        _alpha_2 = 'ff'
        _color_0 = f'#ff{_colors[_index]}' 
    _color_1 = f'#{_alpha_1}{_colors[_index-1]}'
    _color_2 = f'#{_alpha_2}{_colors[_index]}'
    """ Paint background """
    pixmap = QPixmap(self.size())
    pixmap.fill(QColor(_color_0))
    painter = QPainter(pixmap)
    gradient = QLinearGradient(0,0,self.width(), 0)
    gradient.setColorAt(_x_1, QColor(_color_1))
    gradient.setColorAt(_x_2, QColor(_color_2))
    painter.fillRect(self.rect(), gradient)
    painter.end()
    palette = self.palette()
    palette.setBrush(QPalette.Window, QBrush(pixmap))
    self.setAutoFillBackground(True)
    self.setPalette(palette)
#______________________________________________________________________________________________________________________

def objects_list_open(self):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _list_object = _global_config['object_list']
    _open_list_data = _global_config['object_lists'][_list_object]
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    """ Setup widget """
    if self.objects_list_widget:
        self.objects_list_widget.deleteLater()
        self.objects_list_widget = None 
    """ Create object """
    self.objects_list_widget = QWidget(self.objects_list_scroll)
    self.objects_list_layout = QVBoxLayout(self.objects_list_widget)
    """ Set object name """
    self.objects_list_widget.setObjectName('objects_list_widget')
    """ Set layout """
    self.objects_list_layout.setSpacing(0)
    self.objects_list_layout.setContentsMargins(10,10,10,10)
    self.objects_list_widget.setLayout(self.objects_list_layout)
    """ Set widget """
    self.objects_list_scroll.setWidget(self.objects_list_widget)
    """ Set size """
    self.objects_list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set texts """
    self.objects_list_title_label.setText(f'{_list_object}')
    """ Add items """
    for section_index, section in enumerate(_open_list_data, start=0):
        """ Section data """
        section_dict = dict(section)
        for key, value in section_dict.items():
            """ Create widget """
            objects_list_section_widget = QWidget(self.objects_list_widget)
            objects_list_section_layout = QGridLayout(objects_list_section_widget)
            objects_list_section_open_button = QPushButton(objects_list_section_widget)
            objects_list_items_widget = QWidget(objects_list_section_widget)
            objects_list_items_layout = QGridLayout(objects_list_items_widget)
            objects_list_items_hash_tag = QLabel(objects_list_items_widget)
            """ Set object name """
            objects_list_section_widget.setObjectName(f'objects_list_section_{key}_widget')
            objects_list_section_open_button.setObjectName(f'objects_list_section_{key}_open_button')
            objects_list_items_widget.setObjectName(f'objects_list_section_{key}_widget')
            objects_list_items_hash_tag.setObjectName(f'objects_list_section_{key}hash_tag')
            """ Set property """
            objects_list_section_widget.setProperty('class', 'objects_list_section_widget')
            objects_list_section_open_button.setProperty('class', 'objects_list_section_open_button')
            objects_list_items_widget.setProperty('class', 'objects_list_items_widget')
            objects_list_items_hash_tag.setProperty('class', 'objects_list_items_hash_tag')
            """ Set layout """
            self.objects_list_layout.addWidget(objects_list_section_widget)
            objects_list_section_layout.addWidget(objects_list_section_open_button,0,0)
            objects_list_section_layout.addWidget(objects_list_items_widget,1,0)
            objects_list_section_layout.setSpacing(0)
            objects_list_section_layout.setContentsMargins(0,0,0,0)
            objects_list_section_widget.setLayout(objects_list_section_layout)
            objects_list_items_layout.addWidget(objects_list_items_hash_tag, 0, 0)
            objects_list_items_layout.setSpacing(0)
            objects_list_items_layout.setContentsMargins(0,0,0,0)
            objects_list_items_widget.setLayout(objects_list_items_layout)
            """ Set widget """
            objects_list_items_widget.setHidden(False)
            """ Set label """
            objects_list_items_hash_tag.setAlignment(Qt.AlignCenter)
            """ Set size """
            objects_list_section_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            objects_list_section_open_button.setFixedHeight(int(self.height()*0.1))
            objects_list_section_open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            objects_list_items_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            objects_list_items_hash_tag.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            """ Set text """
            objects_list_section_open_button.setText(f'{key}')
            objects_list_items_hash_tag.setText('#')
            """ Connect """
            objects_list_section_open_button.clicked.connect(lambda _, widget=objects_list_items_widget: widget.setHidden(not widget.isHidden()))
            """ Create tags """
            for index, tag in enumerate(_global_config['object_list_tags'], start=1):
                objects_list_tag_label = QLabel(objects_list_items_widget)
                objects_list_tag_label.setObjectName(f'objects_list_tag_label_{index}')
                objects_list_tag_label.setProperty('class', 'objects_list_tag_label')
                objects_list_items_layout.addWidget(objects_list_tag_label, 0, index)
                objects_list_tag_label.setAlignment(Qt.AlignCenter)
                objects_list_tag_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                objects_list_tag_label.setText(f'{_t['objects_list_tags'][f'{tag}'][_global_config['language']]}')
            """ Create items """
            database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
            cursor = database.cursor()
            if value:
                for row, item in enumerate(value, start=1):
                    objects_list_index_button = QPushButton(objects_list_items_widget)
                    objects_list_index_button.setObjectName(f'objects_list_index_{row}_button')
                    objects_list_index_button.setProperty('class', 'objects_list_index_button')
                    objects_list_items_layout.addWidget(objects_list_index_button, row, 0)
                    objects_list_index_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    objects_list_index_button.setText(f'{row}')
                    objects_list_index_button.clicked.connect(lambda _, s_i=section_index, s_n=key, i=row-1: objects_list_delete_object(self, section_index=s_i, section_name=s_n, index=i))
                    for table, id_id in dict(item).items():
                        for column, tag in enumerate(_global_config['object_list_tags'], start=1):
                            try:
                                text = cursor.execute(f'SELECT {tag} FROM {table} WHERE id={id_id};').fetchall()[0][0]
                            except:
                                text = '---'
                            if tag == 'name':
                                objects_list_data_object = QPushButton(objects_list_items_widget)
                                objects_list_data_object.setObjectName(f'objects_list_data_{tag}_{id_id}_button')
                                objects_list_data_object.setProperty('class', 'objects_list_data_button')
                                objects_list_data_object.setText(str(text))
                                objects_list_data_object.clicked.connect(lambda _, t=table, i=id_id: object_set(self, [t, i]))
                            else:
                                objects_list_data_object = QLabel(objects_list_items_widget)
                                objects_list_data_object.setObjectName(f'objects_list_data_{tag}_{id_id}_label')
                                objects_list_data_object.setProperty('class', 'objects_list_data_label')
                                objects_list_data_object.setAlignment(Qt.AlignCenter)
                                if tag == 'icon' and text != '---':
                                    objects_list_data_object.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+text+'.svg', objects_list_data_object.height(), objects_list_data_object.height()))
                                else:
                                    objects_list_data_object.setText(str(text))
                            objects_list_data_object.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                            objects_list_items_layout.addWidget(objects_list_data_object, row, column)
#______________________________________________________________________________________________________________________

def objects_list_delete_object(self, section_index, section_name, index):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    object_name = _global_config['object_list']
    object_in_section = _global_config['object_lists'][object_name][section_index][section_name]
    object_in_section.pop(index)
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    objects_list_open(self)
#______________________________________________________________________________________________________________________

def object_set(self, object_info):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _global_config['object'] = object_info
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    """ Reload object """
    object_setup(self)
#______________________________________________________________________________________________________________________

def object_list_lists_scroll_setup(self):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    """ Add lists items """
    for keys, values in _global_config['object_lists'].items():
        objects_list_lists_button = QPushButton(self.objects_list_lists_widget)
        objects_list_lists_button.setObjectName(f'objects_list_lists_{keys}_button')
        objects_list_lists_button.setProperty('class', 'objects_list_lists_button')
        self.objects_list_lists_layout.addWidget(objects_list_lists_button)
        objects_list_lists_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        objects_list_lists_button.setText(f'{keys}')
        objects_list_lists_button.clicked.connect(lambda _, name=keys: object_list_set_list(self, name=name))
#______________________________________________________________________________________________________________________

def object_list_lists_exit(self):
    """ Set config """
    self.objects_list_title_label.show()
    self.objects_list_scroll.show()
    self.type_list_button.show()
    self.data_list_button.show()
    self.objects_list_lists_title_label.deleteLater()
    self.objects_list_lists_scroll.deleteLater()
    self.objects_list_lists_exit_button.deleteLater()
#______________________________________________________________________________________________________________________

def object_list_set_list(self, name):
    """ Set local data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _global_config['mid_object_list'] = name
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    objects_list_open(self)
    object_list_lists_exit(self)
#______________________________________________________________________________________________________________________

def object_list_edit_check_selected(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    for val in _global_config['object_list_tags']:
        if val == 'name':
            pass
        else:
            button = getattr(self, f'object_list_edit_{val}_button')       
            button.setStyleSheet('background-color: #282828;')
#______________________________________________________________________________________________________________________

def object_list_edit_save(self, val):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    button = getattr(self, f'object_list_edit_{val}_button')
    if val not in _global_config['object_list_tags']:
        _global_config['object_list_tags'].append(val)       
        button.setStyleSheet('background-color: #282828;')
    else:
        _global_config['object_list_tags'].remove(val)       
        button.setStyleSheet('background-color: #1a1a1a;')
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
#______________________________________________________________________________________________________________________

def object_list_edit_exit(self):
    """ Set config """
    self.objects_list_title_label.show()
    self.objects_list_scroll.show()
    self.type_list_button.show()
    self.data_list_button.show()
    """ Delete objects """
    self.object_list_edit_title_label.deleteLater()
    self.object_list_edit_scroll.deleteLater()
    self.object_list_edit_exit_button.deleteLater()
    objects_list_open(self)
#______________________________________________________________________________________________________________________

def object_setup(self):
    """ Set dafoult """
    if self.object_time_widget:
        self.object_time_widget.deleteLater()
        self.object_time_widget = None
    if self.object_chart_widget:
        self.object_chart_widget.deleteLater()
        self.object_chart_widget = None
    if self. object_info_widget:
        self.object_info_widget.deleteLater()
        self.object_info_widget = None
    if self.object_statistics_widget:
        self.object_statistics_widget.deleteLater()
        self.object_statistics_widget = None
    self.object_ticker_label.setText('')
    self.object_ticker_label.setHidden(True)
    self.object_name_label.setText('')
    self.object_name_label.setHidden(True)
    """ Create new object """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    if _global_config['object'][0] == 'country':
        object_country(self)
    elif _global_config['object'][0] == 'market':
        object_market(self)
    elif _global_config['object'][0] == 'market_index':
        object_index(self)
    elif _global_config['object'][0] == 'stock':
        object_stock(self)
#______________________________________________________________________________________________________________________

def object_country(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    country_data = cursor.execute(f'''
    SELECT
    country.name, 
    country.icon, 
    country.capital, 
    country.currency_code, 
    timezone.name, 
    population.number
    FROM country 
    JOIN timezone ON country.id_timezone=timezone.id
    JOIN population ON country.id=population.id_country
    WHERE country.id=={_global_config['object'][1]};''').fetchall()[0]
    country_stocks_data = cursor.execute(f'''
    SELECT 
    stock.name,
    stock.capitalization
    FROM stock 
    JOIN market ON stock.id_market=market.id
    JOIN country ON market.id_country=country.id
    WHERE country.id=={_global_config['object'][1]} ORDER BY stock.capitalization DESC LIMIT 5
    ''').fetchall()
    cursor.close()
    database.close()
    """ Create """
    self.object_time_widget = QWidget(self)
    self.object_info_widget = QWidget(self)
    self.object_info_layout = QGridLayout(self.object_info_widget)
    info_population_name_label = QLabel(self.object_info_widget)
    info_population_value_label = QLabel(self.object_info_widget)
    info_capital_name_label = QLabel(self.object_info_widget)
    info_capital_value_label = QLabel(self.object_info_widget)
    info_timezone_name_label = QLabel(self.object_info_widget)
    info_timezone_value_label = QLabel(self.object_info_widget)
    info_currency_name_label = QLabel(self.object_info_widget)
    info_currency_value_label = QLabel(self.object_info_widget)
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    statistics_title_label = QLabel(self.object_statistics_widget)
    statistics_index_name_label = QLabel(self.object_statistics_widget)
    statistics_name_name_label = QLabel(self.object_statistics_widget)
    statistics_capitalization_name_label = QLabel(self.object_statistics_widget)
    """ Set object name """
    self.object_time_widget.setObjectName('object_time_widget')
    self.object_info_widget.setObjectName('object_info_widget')
    info_population_name_label.setObjectName('info_population_name_label')
    info_population_value_label.setObjectName('info_population_value_label')
    info_capital_name_label.setObjectName('info_capital_name_label')
    info_capital_value_label.setObjectName('info_capital_value_label')
    info_timezone_name_label.setObjectName('info_timezone_name_label')
    info_timezone_value_label.setObjectName('info_timezone_value_label')
    info_currency_name_label.setObjectName('info_currency_name_label')
    info_currency_value_label.setObjectName('info_currency_value_label')
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    statistics_title_label.setObjectName('statistics_title_label')
    statistics_index_name_label.setObjectName('statistics_index_name_label')
    statistics_name_name_label.setObjectName('statistics_name_name_label')
    statistics_capitalization_name_label.setObjectName('statistics_capitalization_name_label')
    """ Set property """
    info_population_name_label.setProperty('class', 'object_info_name_label')
    info_capital_name_label.setProperty('class', 'object_info_name_label')
    info_timezone_name_label.setProperty('class', 'object_info_name_label')
    info_currency_name_label.setProperty('class', 'object_info_name_label')
    info_population_value_label.setProperty('class', 'object_info_value_label')
    info_capital_value_label.setProperty('class', 'object_info_value_label')
    info_timezone_value_label.setProperty('class', 'object_info_value_label')
    info_currency_value_label.setProperty('class', 'object_info_value_label')
    """ Set layout """
    self.layout.addWidget(self.object_time_widget, 16, 15, 2, 42)
    self.layout.addWidget(self.object_info_widget, 26, 15, 32, 42)
    self.layout.addWidget(self.object_statistics_widget, 60, 15, 32, 42)
    self.object_statistics_layout.addWidget(statistics_title_label, 5, 0, 10, 100)
    self.object_statistics_layout.addWidget(statistics_index_name_label, 20, 0, 10, 10)
    self.object_statistics_layout.addWidget(statistics_name_name_label, 20, 10, 10, 45)
    self.object_statistics_layout.addWidget(statistics_capitalization_name_label, 20, 55, 10, 45)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.object_statistics_layout.setRowStretch(enc, 1)
        self.object_statistics_layout.setColumnStretch(enc, 1)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
    self.object_info_layout.addWidget(info_population_name_label,0,0)
    self.object_info_layout.addWidget(info_population_value_label,0,1)
    self.object_info_layout.addWidget(info_capital_name_label,1,0)
    self.object_info_layout.addWidget(info_capital_value_label,1,1)
    self.object_info_layout.addWidget(info_timezone_name_label,2,0)
    self.object_info_layout.addWidget(info_timezone_value_label,2,1)
    self.object_info_layout.addWidget(info_currency_name_label,3,0)
    self.object_info_layout.addWidget(info_currency_value_label,3,1)
    self.object_info_layout.setSpacing(0)
    self.object_info_layout.setContentsMargins(0,0,0,0)
    self.object_info_widget.setLayout(self.object_info_layout)
    """ Set widget """
    self.object_name_label.setHidden(False)
    """ Set label """
    statistics_title_label.setAlignment(Qt.AlignCenter)
    statistics_index_name_label.setAlignment(Qt.AlignCenter)
    statistics_name_name_label.setAlignment(Qt.AlignCenter)
    statistics_capitalization_name_label.setAlignment(Qt.AlignCenter)
    info_population_name_label.setAlignment(Qt.AlignCenter)
    info_population_value_label.setAlignment(Qt.AlignCenter)
    info_capital_name_label.setAlignment(Qt.AlignCenter)
    info_capital_value_label.setAlignment(Qt.AlignCenter)
    info_timezone_name_label.setAlignment(Qt.AlignCenter)
    info_timezone_value_label.setAlignment(Qt.AlignCenter)
    info_currency_name_label.setAlignment(Qt.AlignCenter)
    info_currency_value_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.object_time_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_info_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_index_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_name_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_population_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_population_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_capital_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_capital_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_timezone_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_timezone_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_currency_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_currency_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.object_name_label.setText(country_data[0])
    statistics_title_label.setText(f'{_t['statistics_title_top_label'][_l]}:')
    statistics_index_name_label.setText('#')
    statistics_name_name_label.setText(f'{_t['statistics_name_name_label'][_l]}:')
    statistics_capitalization_name_label.setText(f'{_t['capitalization_name_label'][_l]}:')
    info_population_name_label.setText(f'{_t['population_name_label'][_l]}:')
    info_population_value_label.setText(str(country_data[5]))
    info_capital_name_label.setText(f'{_t['capital_name_label'][_l]}:')
    info_capital_value_label.setText(str(country_data[2]))
    info_timezone_name_label.setText(f'{_t['timezone_name_label'][_l]}:')
    info_timezone_value_label.setText(str(country_data[4]))
    info_currency_name_label.setText(f'{_t['currency_name_label'][_l]}:')
    info_currency_value_label.setText(str(country_data[3]))
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+country_data[1]+'.svg', int(self.object_icon_label.height()), int(self.object_icon_label.height())))
    """ Create info list """
    for index, stock_data in enumerate(country_stocks_data, start=1):
        _row = (index*10)+25
        """ Create """
        index_label = QLabel(self.object_statistics_widget)
        name_label = QLabel(self.object_statistics_widget)
        capitalization_label = QLabel(self.object_statistics_widget)
        """ Set object name """
        index_label.setObjectName(f'index_{index}_label')
        name_label.setObjectName(f'name_{index}_label')
        capitalization_label.setObjectName(f'capitalization_{index}_label')
        """ Set property """
        index_label.setProperty('class', 'object_statistics_index_label')
        name_label.setProperty('class', 'object_statistics_name_label')
        capitalization_label.setProperty('class', 'object_statistics_value_label')
        """ Set layout """
        self.object_statistics_layout.addWidget(index_label, _row, 0, 10, 10)
        self.object_statistics_layout.addWidget(name_label, _row, 10, 10, 45)
        self.object_statistics_layout.addWidget(capitalization_label, _row, 55, 10, 45)
        """ Set Label """
        index_label.setAlignment(Qt.AlignCenter)
        name_label.setAlignment(Qt.AlignCenter)
        capitalization_label.setAlignment(Qt.AlignCenter)
        """ Set size """
        index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        capitalization_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        """ Set text """
        index_label.setText(f'{index}.')
        name_label.setText(f'{stock_data[0]}')
        capitalization_label.setText(f'{stock_data[1]}')
#______________________________________________________________________________________________________________________

def object_market(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    market_data = cursor.execute(f'''
    SELECT
    market.name, 
    market.short_name,
    market.icon,
    market.city, 
    market.website, 
    market.founded_date,
    market.capitalization,
    market.pre_open_time,
    market.open_time,
    market.close_time,
    market.post_close_time,
    timezone.id
    FROM market
    JOIN country ON market.id_country=country.id
    JOIN timezone ON country.id_timezone=timezone.id
    WHERE market.id={_global_config['object'][1]};''').fetchall()[0]
    cursor.close()
    database.close()
    """ Create """
    self.object_time_widget = QWidget(self)
    self.object_time_layout = QGridLayout(self)
    time_close_1_label = QLabel(self.object_time_widget)
    time_pre_open_label = QLabel(self.object_time_widget)
    time_open_label = QLabel(self.object_time_widget)
    time_post_close_label = QLabel(self.object_time_widget)
    time_close_2_label = QLabel(self.object_time_widget)
    #time_dot_label = QLabel(self.object_time_widget)
    self.object_info_widget = QWidget(self)
    self.object_info_layout = QGridLayout(self.object_info_widget)
    info_city_name_label = QLabel(self.object_statistics_widget)
    info_city_value_label = QLabel(self.object_statistics_widget)
    info_founded_date_name_label = QLabel(self.object_statistics_widget)
    info_founded_data_value_label = QLabel(self.object_statistics_widget)
    info_website_name_label = QLabel(self.object_statistics_widget)
    info_website_value_label = QLabel(self.object_statistics_widget)
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    statistics_capitalization_name_label = QLabel(self.object_statistics_widget)
    statistics_capitalization_value_label = QLabel(self.object_statistics_widget)
    """ Set object name """
    self.object_time_widget.setObjectName('object_time_widget')
    time_close_1_label.setObjectName('time_close_1_label')
    time_pre_open_label.setObjectName('time_pre_open_label')
    time_open_label.setObjectName('time_open_label')
    time_post_close_label.setObjectName('time_post_close_label')
    time_close_2_label.setObjectName('time_close_2_label')
    #time_dot_label.setObjectName('time_dot_label')
    self.object_info_widget.setObjectName('object_info_widget')
    info_city_name_label.setObjectName('info_city_name_label')
    info_city_value_label.setObjectName('info_city_value_label')
    info_founded_date_name_label.setObjectName('info_founded_date_name_label')
    info_founded_data_value_label.setObjectName('info_founded_data_value_label')
    info_website_name_label.setObjectName('info_website_name_label')
    info_website_value_label.setObjectName('info_website_value_label')
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    statistics_capitalization_name_label.setObjectName('capitalization_name_label')
    statistics_capitalization_value_label.setObjectName('capitalization_value_label')
    """ Set property """
    info_city_name_label.setProperty('class', 'object_info_name_label')
    info_founded_date_name_label.setProperty('class', 'object_info_name_label')
    info_website_name_label.setProperty('class', 'object_info_name_label')
    info_city_value_label.setProperty('class', 'object_info_value_label')
    info_founded_data_value_label.setProperty('class', 'object_info_value_label')
    info_website_value_label.setProperty('class', 'object_info_value_label')
    statistics_capitalization_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_capitalization_value_label.setProperty('class', 'object_statistics_value_label')
    """ Set layout """
    self.layout.addWidget(self.object_time_widget, 16, 15, 2, 42)
    self.layout.addWidget(self.object_info_widget, 26, 15, 32, 42)
    self.layout.addWidget(self.object_statistics_widget, 60, 15, 32, 42)
    self.object_time_layout.setSpacing(0)
    self.object_time_layout.setContentsMargins(0,0,0,0)
    for enc in range(86400):
        self.object_time_layout.setColumnStretch(enc, 1)
    self.object_time_widget.setLayout(self.object_time_layout)
    self.object_info_layout.addWidget(info_city_name_label, 0, 0)
    self.object_info_layout.addWidget(info_city_value_label, 0, 1)
    self.object_info_layout.addWidget(info_founded_date_name_label, 1, 0)
    self.object_info_layout.addWidget(info_founded_data_value_label, 1, 1)
    self.object_info_layout.addWidget(info_website_name_label, 2, 0)
    self.object_info_layout.addWidget(info_website_value_label, 2, 1)
    self.object_info_layout.setSpacing(0)
    self.object_info_layout.setContentsMargins(0,0,0,0)
    self.object_info_widget.setLayout(self.object_info_layout)
    self.object_statistics_layout.addWidget(statistics_capitalization_name_label,0,0)
    self.object_statistics_layout.addWidget(statistics_capitalization_value_label,0,1)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
    """ Set widget """
    self.object_ticker_label.setHidden(False)
    self.object_name_label.setHidden(False)
    """ Set label """
    info_city_name_label.setAlignment(Qt.AlignCenter)
    info_city_value_label.setAlignment(Qt.AlignCenter)
    info_founded_date_name_label.setAlignment(Qt.AlignCenter)
    info_founded_data_value_label.setAlignment(Qt.AlignCenter)
    info_website_name_label.setAlignment(Qt.AlignCenter)
    info_website_value_label.setAlignment(Qt.AlignCenter)
    statistics_capitalization_name_label.setAlignment(Qt.AlignCenter)
    statistics_capitalization_value_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.object_time_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_info_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    time_close_1_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    time_pre_open_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    time_open_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    time_post_close_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    time_close_2_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #time_dot_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_city_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_city_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_founded_date_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_founded_data_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_website_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    info_website_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capitalization_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.object_ticker_label.setText(market_data[1])
    self.object_name_label.setText(market_data[0])
    info_city_name_label.setText(f'{_t['city_name_label'][_l]}:')
    info_city_value_label.setText(f'{market_data[3]}')
    info_founded_date_name_label.setText(f'{_t['founded_date_name_label'][_l]}:')
    info_founded_data_value_label.setText(f'{market_data[5]}')
    info_website_name_label.setText(f'{_t['website_name_label'][_l]}:')
    info_website_value_label.setText(f'{market_data[4]}')
    statistics_capitalization_name_label.setText(f'{_t['capitalization_name_label'][_l]}:')
    statistics_capitalization_value_label.setText(f'{market_data[6]}')
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+market_data[2]+'.svg', int(self.object_icon_label.height()), int(self.object_icon_label.height())))
    """ Setup time widget """
    pre_open_time = int(market_data[7])
    open_time = int(market_data[8])
    close_time = int(market_data[9])
    post_close_time = int(market_data[10])

    self.object_time_layout.addWidget(time_close_1_label, 0, 0, 1, pre_open_time)
    self.object_time_layout.addWidget(time_pre_open_label, 0, pre_open_time, 1, open_time-pre_open_time)
    self.object_time_layout.addWidget(time_open_label, 0, open_time, 1, close_time-open_time)
    self.object_time_layout.addWidget(time_post_close_label, 0, close_time, 1, post_close_time-close_time)
    self.object_time_layout.addWidget(time_close_2_label, 0, post_close_time, 1, 86400-post_close_time)
#______________________________________________________________________________________________________________________

def object_index(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    index_data = cursor.execute(f'''
    SELECT
    market_index.name, 
    market_index.icon 
    FROM market_index 
    WHERE market_index.id={_global_config['object'][1]};''').fetchall()[0]
    objects_of_index = cursor.execute(f'''
    SELECT 
    stock.icon, 
    stock.ticker
    FROM stock
    JOIN index_stock ON stock.id=index_stock.id_stock
    WHERE index_stock.id_index={_global_config['object'][1]};''').fetchall()
    cursor.close()
    database.close()
    """ Create """
    _chart_data = json.load(open(self.main_path+f'/CHART_DATA/{index_data[0]}_15.json', 'r'))
    self.object_chart_widget = Main_chart(self, _chart_data)
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    statistics_title_label = QLabel(self.object_statistics_widget)
    statistics_index_label = QLabel(self.object_statistics_widget)
    statistics_ticker_label = QLabel(self.object_statistics_widget)
    statistics_stocks_scroll = QScrollArea(self.object_statistics_widget)
    statistics_stocks_widget = QWidget(statistics_stocks_scroll)
    statistics_stocks_layout = QGridLayout(statistics_stocks_widget)
    """ Set object name """
    self.object_chart_widget.setObjectName('object_chart_widget')
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    statistics_title_label.setObjectName('statistics_title_label')
    statistics_index_label.setObjectName('statistics_index_label')
    statistics_ticker_label.setObjectName('statistics_ticker_label')
    statistics_stocks_scroll.setObjectName('statistics_stocks_scroll')
    statistics_stocks_widget.setObjectName('statistics_stocks_widget')
    """ Set layout """
    self.layout.addWidget(self.object_chart_widget, 26, 15, 32, 42)
    self.layout.addWidget(self.object_statistics_widget, 60, 15, 32, 42)
    self.object_statistics_layout.addWidget(statistics_title_label,5, 0, 10, 100)
    self.object_statistics_layout.addWidget(statistics_index_label, 20, 0, 10, 10)
    self.object_statistics_layout.addWidget(statistics_ticker_label, 20, 35, 10, 65)
    self.object_statistics_layout.addWidget(statistics_stocks_scroll, 35, 0, 60, 100)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.object_statistics_layout.setRowStretch(enc, 1)
        self.object_statistics_layout.setColumnStretch(enc,1)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
    statistics_stocks_layout.setSpacing(0)
    statistics_stocks_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        statistics_stocks_layout.setColumnStretch(enc, 1)
    statistics_stocks_widget.setLayout(statistics_stocks_layout)
    """ Set widget """
    self.object_name_label.setHidden(False)
    statistics_stocks_scroll.setWidgetResizable(True)
    statistics_stocks_scroll.setWidget(statistics_stocks_widget)
    """ Set label """
    statistics_title_label.setAlignment(Qt.AlignCenter)
    statistics_index_label.setAlignment(Qt.AlignCenter)
    statistics_ticker_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_stocks_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_stocks_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.object_name_label.setText(f'{index_data[0]}')
    statistics_title_label.setText(_t['statistics_title_stock_label'][_l])
    statistics_index_label.setText('#')
    statistics_ticker_label.setText(_t['statistics_name_name_label'][_l])
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+index_data[1]+'.svg', int(self.object_icon_label.height()), int(self.object_icon_label.height())))
    """ Creat stocks list"""
    for index, item_list in enumerate(objects_of_index, start=0):
        """ Create objects """
        index_label = QLabel(statistics_stocks_widget)
        logo_label = QLabel(statistics_stocks_widget)
        name_label = QLabel(statistics_stocks_widget)
        """ Set object name """
        index_label.setObjectName(f'index_{index}_label')
        logo_label.setObjectName(f'logo_{index}_label')
        name_label.setObjectName(f'name_{index}_label')
        """ Set property """
        index_label.setProperty('class', 'object_statistics_index_label')
        logo_label.setProperty('class', 'object_statistics_logo_label')
        name_label.setProperty('class', 'object_statistics_name_label')
        """ Set layout """
        statistics_stocks_layout.addWidget(index_label, index, 0, 1, 10)
        statistics_stocks_layout.addWidget(logo_label, index, 10, 1, 20)
        statistics_stocks_layout.addWidget(name_label, index, 35, 1, 65)
        """ Set label """
        index_label.setAlignment(Qt.AlignCenter)
        logo_label.setAlignment(Qt.AlignCenter)
        name_label.setAlignment(Qt.AlignCenter)
        """ Set size """
        index_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        logo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        """ Set text """
        index_label.setText(f'{index+1}.')
        name_label.setText(item_list[1])
        """ Set graphic """
        logo_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+item_list[0]+'.svg', logo_label.height(), logo_label.height()))
#______________________________________________________________________________________________________________________

def object_stock(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    stock_data = cursor.execute(f'''
    SELECT
    stock.name,
    stock.ticker,
    stock.icon,
    stock.capitalization,
    stock.pe_ratio,
    stock.eps,
    stock.dividend_yield
    FROM stock
    WHERE stock.id={_global_config['object'][1]};''').fetchall()[0]
    cursor.close()
    database.close()
    """ Create """
    _chart_data = json.load(open(self.main_path+f'/CHART_DATA/{stock_data[1]}_15.json', 'r'))
    self.object_chart_widget = Main_chart(self, _chart_data)
    self.object_statistics_widget = QWidget(self)
    self.object_statistics_layout = QGridLayout(self.object_statistics_widget)
    statistics_capitalization_name_label = QLabel(self.object_statistics_widget)
    statistics_capitalization_value_label = QLabel(self.object_statistics_widget)
    statistics_pe_ratio_name_label = QLabel(self.object_statistics_widget)
    statistics_pe_ratio_value_label = QLabel(self.object_statistics_widget)
    statistics_eps_name_label = QLabel(self.object_statistics_widget)
    statistics_eps_value_label = QLabel(self.object_statistics_widget)
    statistics_dividend_yield_name_label = QLabel(self.object_statistics_widget)
    statistics_dividend_yield_value_label = QLabel(self.object_statistics_widget)
    """ Set object name """
    self.object_chart_widget.setObjectName('object_chart_widget')
    self.object_statistics_widget.setObjectName('object_statistics_widget')
    statistics_capitalization_name_label.setObjectName('statistics_capitalization_name_label')
    statistics_capitalization_value_label.setObjectName('statistics_capitalization_value_label')
    statistics_pe_ratio_name_label.setObjectName('statistics_pe_ratio_name_label')
    statistics_pe_ratio_value_label.setObjectName('statistics_pe_ratio_value_label')
    statistics_eps_name_label.setObjectName('statistics_eps_name_label')
    statistics_eps_value_label.setObjectName('statistics_eps_value_label')
    statistics_dividend_yield_name_label.setObjectName('statistics_dividend_yield_name_label')
    statistics_dividend_yield_value_label.setObjectName('statistics_dividend_yield_value_label')
    """ Set property """
    statistics_capitalization_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_pe_ratio_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_eps_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_dividend_yield_name_label.setProperty('class', 'object_statistics_name_label')
    statistics_capitalization_value_label.setProperty('class', 'object_statistics_value_label')
    statistics_pe_ratio_value_label.setProperty('class', 'object_statistics_value_label')
    statistics_eps_value_label.setProperty('class', 'object_statistics_value_label')
    statistics_dividend_yield_value_label.setProperty('class', 'object_statistics_value_label')
    """ Set layout """
    self.layout.addWidget(self.object_chart_widget, 26, 15, 32, 42)
    self.layout.addWidget(self.object_statistics_widget, 60, 15, 32, 42)
    self.object_statistics_layout.addWidget(statistics_capitalization_name_label,0,0)
    self.object_statistics_layout.addWidget(statistics_capitalization_value_label,0,1)
    self.object_statistics_layout.addWidget(statistics_pe_ratio_name_label,1,0)
    self.object_statistics_layout.addWidget(statistics_pe_ratio_value_label,1,1)
    self.object_statistics_layout.addWidget(statistics_eps_name_label,2,0)
    self.object_statistics_layout.addWidget(statistics_eps_value_label,2,1)
    self.object_statistics_layout.addWidget(statistics_dividend_yield_name_label,3,0)
    self.object_statistics_layout.addWidget(statistics_dividend_yield_value_label,3,1)
    self.object_statistics_layout.setSpacing(0)
    self.object_statistics_layout.setContentsMargins(0,0,0,0)
    self.object_statistics_widget.setLayout(self.object_statistics_layout)
    """ Set widget """
    self.object_ticker_label.setHidden(False)
    self.object_name_label.setHidden(False)
    """ Set label """
    statistics_capitalization_name_label.setAlignment(Qt.AlignCenter)
    statistics_capitalization_value_label.setAlignment(Qt.AlignCenter)
    statistics_pe_ratio_name_label.setAlignment(Qt.AlignCenter)
    statistics_pe_ratio_value_label.setAlignment(Qt.AlignCenter)
    statistics_eps_name_label.setAlignment(Qt.AlignCenter)
    statistics_eps_value_label.setAlignment(Qt.AlignCenter)
    statistics_dividend_yield_name_label.setAlignment(Qt.AlignCenter)
    statistics_dividend_yield_value_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.object_statistics_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capitalization_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_capitalization_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_pe_ratio_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_pe_ratio_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_eps_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_eps_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_dividend_yield_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    statistics_dividend_yield_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main/translate.json', 'r'))
    _l = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
    self.object_ticker_label.setText(f'{stock_data[1]}')
    self.object_name_label.setText(f'{stock_data[0]}')
    statistics_capitalization_name_label.setText(f'{_t['capitalization_name_label'][_l]}:')
    statistics_capitalization_value_label.setText(f'{stock_data[3]}')
    statistics_pe_ratio_name_label.setText(f'{_t['pe_ratio_name_label'][_l]}:')
    statistics_pe_ratio_value_label.setText(f'{stock_data[4]}')
    statistics_eps_name_label.setText(f'{_t['eps_name_label'][_l]}:')
    statistics_eps_value_label.setText(f'{stock_data[5]}')
    statistics_dividend_yield_name_label.setText(f'{_t['dividend_yield_name_label'][_l]}:')
    statistics_dividend_yield_value_label.setText(f'{stock_data[6]}')
    """ Set graphics """
    self.object_icon_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+stock_data[2]+'.svg', int(self.object_icon_label.height()), int(self.object_icon_label.height())))
#______________________________________________________________________________________________________________________

def news_creator(self):
    _news_button_list = self.news_button_list
    connect = mysql.connector.connect(
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()
    cursor.execute('SELECT id, json_file FROM News ORDER BY date DESC LIMIT 5;')
    news_list = cursor.fetchall()
    cursor.close()
    connect.close()
    if news_list:
        for index, data in enumerate(news_list, start=1):
            json_data = json.loads(data[1])
            news_id = data[0]
            """ Create objects """
            news_button = QPushButton(self)
            news_layout = QVBoxLayout(news_button)
            news_text_label = QLabel(news_button)
            """ Set object name """
            news_button.setObjectName(f'news_button_{index}')
            news_text_label.setObjectName(f'text_label_{index}')
            """ Set property """
            news_button.setProperty('class', 'news_button')
            news_text_label.setProperty('class', 'news_text_label')
            """ Set layout """
            self.layout.addWidget(news_button, 2, 58, 85, 41)
            news_layout.addWidget(news_text_label)  
            news_layout.setContentsMargins(0,0,0,0)
            news_layout.setSpacing(0)
            """ Set Widget """
            news_button.setHidden(True)
            """ Set label """
            news_text_label.setAlignment(Qt.AlignCenter)
            news_text_label.setWordWrap(True)
            """ Set size """
            news_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            news_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            news_text_label.setGeometry(QRect(0,0,news_button.width(),news_button.height()))
            """ Set text """
            news_text_label.setText(json_data['title'])
            """ Set graphics """
            """ Set connect function for open """
            news_button.clicked.connect(lambda _, id_n=news_id: open_main_news(self, id_n))
            _news_button_list.append(news_button)
        self.news_button_list = _news_button_list
        self.news_button_list[self.news_button_index].setHidden(False)
        self.news_timer.timeout.connect(lambda: news_next(self))
        self.news_timer.start(5000)
    else:
        news_label = QLabel(self)
        news_label.setObjectName('news_label')
        self.layout.addWidget(news_label, 2, 58, 85, 41)
        news_label.setAlignment(Qt.AlignCenter)
        news_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        news_label.setText('...')
        self.news_next_left_button.setDisabled(True)
        self.news_next_right_button.setDisabled(True)
#______________________________________________________________________________________________________________________

def news_next(self):
    self.news_timer.stop()
    self.news_timer.start(5000)
    self.news_button_list[self.news_button_index].setHidden(True)
    self.news_button_index = (self.news_button_index+1)%len(self.news_button_list)
    self.news_button_list[self.news_button_index].setHidden(False)
#______________________________________________________________________________________________________________________

def news_previous(self):
    self.news_timer.stop()
    self.news_timer.start(5000)
    self.news_button_list[self.news_button_index].setHidden(True)
    self.news_button_index = (self.news_button_index-1)%len(self.news_button_list)
    self.news_button_list[self.news_button_index].setHidden(False)
#______________________________________________________________________________________________________________________

def open_main_news(self, id_news):
    self.main_news = Main_news_widget(self, id_news)
#______________________________________________________________________________________________________________________

def open_main_news_list(self, news_type_index):
    self.main_news_list = Main_news_list_widget(self, news_type_index)
    self.main_news_list.open_news.connect(lambda val: open_main_news(self, val))
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
