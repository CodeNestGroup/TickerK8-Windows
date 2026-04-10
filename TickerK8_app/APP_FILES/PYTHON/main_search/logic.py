""" Import packages """
import json
import sqlite3
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
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

def text_changed(self):
    """ Get config """
    _text = self.panel_search_lineedit.text()
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    _active_filters = _global_config['search_filters']
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    all_data = []
    all_data_id = []
    if _active_filters[0]:
        if _text != '':
            where = f'WHERE stock.name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT stock.id, stock.icon, stock.name, market.icon, market.name FROM stock JOIN market ON stock.id_market=market.id {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
            for d in database_data: all_data_id.append({"stock": d[0]})
    if _active_filters[1]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM etf WHERE name like "%{_text}%";
        ''').fetchall()[0])
        all_data.append(database_data)
    if _active_filters[2]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM WHERE name like "%{_text}%";
        ''').fetchall()[0])
        all_data.append(database_data)
    if _active_filters[3]:
        if _text != '':
            where = f'WHERE market_index.name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT market_index.id, market_index.icon, market_index.name, market.icon, market.name FROM market_index JOIN market ON market_index.id_market=market.id {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
            for d in database_data: all_data_id.append({"market_index": d[0]})
    if _active_filters[4]: 
        if _text != '':
            where = f'WHERE name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT market.id, market.icon, market.name FROM market {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
            for d in database_data: all_data_id.append({"market": d[0]})
    if _active_filters[5]:
        if _text != '':
            where = f'WHERE name like "%{_text}%"'
        else:
            where = ''
        database_data = cursor.execute(f'''
            SELECT country.id, country.icon, country.name FROM country {where};
        ''').fetchall()
        if database_data:
            for e in database_data: all_data.append(e)
            for d in database_data: all_data_id.append({"country": d[0]})
    cursor.close()
    database.close()
    """ Set up """
    if self.panel_scroll_widget:
        self.panel_scroll_widget.deleteLater()
        self.panel_scroll_widget = None 
    """ Create widget """
    self.panel_scroll_widget = QWidget(self.panel_scroll)
    self.panel_scroll_widget.setObjectName('panel_scroll_widget')
    self.panel_scroll_widget.setProperty('class', 'panel_scroll_widget_class')
    self.panel_scroll.setWidget(self.panel_scroll_widget)
    self.panel_scroll_widget.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
    self.panel_scroll_layout = QGridLayout(self.panel_scroll_widget)
    self.panel_scroll_layout.setSpacing(0)
    self.panel_scroll_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_scroll_layout.setRowStretch(enc, 1)
        self.panel_scroll_layout.setColumnStretch(enc, 1)
    self.panel_scroll_widget.setLayout(self.panel_scroll_layout)
    for i, list_object in enumerate(all_data, start=1):
        index_button = QPushButton(self.panel_widget)
        object_logo_label = QLabel(self.panel_widget)
        object_name_button = QPushButton(self.panel_widget)
        market_logo_label = QLabel(self.panel_widget)
        market_name_label = QLabel(self.panel_widget)
        index_button.setObjectName('index_button')
        object_logo_label.setObjectName('object_logo_label')
        object_name_button.setObjectName('object_name_button')
        market_logo_label.setObjectName('market_logo_label')
        market_name_label.setObjectName('market_name_label')
        self.panel_scroll_layout.addWidget(index_button, i, 2, 1, 5)
        self.panel_scroll_layout.addWidget(object_logo_label, i, 7, 1, 16)
        self.panel_scroll_layout.addWidget(object_name_button, i, 23, 1, 29)
        self.panel_scroll_layout.addWidget(market_logo_label, i, 52, 1, 16)
        self.panel_scroll_layout.addWidget(market_name_label, i, 68, 1, 29)
        object_logo_label.setAlignment(Qt.AlignCenter)
        market_logo_label.setAlignment(Qt.AlignCenter)
        market_name_label.setAlignment(Qt.AlignCenter)
        index_button.setMaximumHeight(50)
        index_button.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        object_logo_label.setMaximumHeight(50)
        object_logo_label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        object_name_button.setMaximumHeight(50)
        object_name_button.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        market_logo_label.setMaximumHeight(50)
        market_logo_label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        market_name_label.setMaximumHeight(50)
        market_name_label.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding)
        index_button.setText(f' {i}')
        object_name_button.setText(f'{list_object[2]}')
        object_logo_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+list_object[1]+'.svg', int(object_logo_label.height()), int(object_logo_label.height())))
        if len(list_object) > 3:
            market_name_label.setText(f'{list_object[4]}')
            market_logo_label.setPixmap(load_svg(self.main_path+'/STYLE/IMG/'+list_object[3]+'.svg', int(market_logo_label.height()), int(market_logo_label.height())))
        index_button.clicked.connect(lambda _, o=all_data_id[i-1]: add_object__lists(self, a_o=o))
#______________________________________________________________________________________________________________________

def filters_changed(self, index):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    """ Get data """
    _global_config['search_filters'][index] = not _global_config['search_filters'][index] 
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4) 
    filters_load(self)
    text_changed(self)
#______________________________________________________________________________________________________________________

def filters_load(self):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    _active_filters = _global_config['search_filters']
    for index, f in enumerate(_active_filters, start=0):
        if f:
            self.button_list[index].setStyleSheet('background-color: #282828;')
        else:
            self.button_list[index].setStyleSheet('background-color: #1a1a1a;')
#______________________________________________________________________________________________________________________

def add_object__lists(self, a_o):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    """ Set deafoult  """
    self.add_object = a_o
    if self.panel_add_widget:
        self.panel_add_widget.deleteLater()
        self.panel_add_widget = None
    """ Create objects """ 
    self.panel_add_widget = QWidget(self.panel_scroll)
    self.panel_add_layout = QGridLayout(self.panel_add_widget)
    self.panel_add_exit_button = QPushButton(self.panel_add_widget)
    self.panel_add_title_label = QLabel(self.panel_add_widget)
    self.panel_add_path_label = QLabel(self.panel_add_widget)
    self.panel_add_scroll = QScrollArea(self.panel_add_widget)
    self.panel_add_scroll_widget = QWidget(self.panel_add_scroll)
    self.panel_add_scroll_layout = QVBoxLayout(self.panel_add_scroll_widget)
    """ Set object name """
    self.panel_add_widget.setObjectName('panel_add_widget')
    self.panel_add_exit_button.setObjectName('panel_add_exit_button')
    self.panel_add_title_label.setObjectName('panel_add_title_label')
    self.panel_add_path_label.setObjectName('panel_add_path_label')
    self.panel_add_scroll.setObjectName('panel_add_scroll')
    self.panel_add_scroll_widget.setObjectName('panel_add_scroll_widget')
    """ Set property """
    self.panel_add_scroll.setProperty('class', 'panel_scroll_class')
    self.panel_add_scroll_widget.setProperty('class', 'panel_scroll_widget_class')
    self.panel_add_exit_button.setProperty('class', 'panel_exit_button_class')
    """ Set Layout """
    self.panel_layout.addWidget(self.panel_add_widget)
    self.panel_add_layout.addWidget(self.panel_add_exit_button, 2, 5, 6, 5)
    self.panel_add_layout.addWidget(self.panel_add_title_label, 5, 30, 5, 40)
    self.panel_add_layout.addWidget(self.panel_add_path_label, 15, 5, 3, 90)
    self.panel_add_layout.addWidget(self.panel_add_scroll, 20, 5, 75, 90)
    self.panel_add_layout.setSpacing(0)
    self.panel_add_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.panel_add_layout.setRowStretch(enc, 1)
        self.panel_add_layout.setColumnStretch(enc, 1)
    self.panel_add_widget.setLayout(self.panel_add_layout)
    self.panel_add_scroll_layout.setSpacing(0)
    self.panel_add_scroll_layout.setContentsMargins(0,0,0,0)
    self.panel_add_scroll_widget.setLayout(self.panel_add_scroll_layout)
    """ Set widget """
    self.panel_search_widget.setHidden(True)
    self.panel_add_widget.setHidden(False)
    self.panel_add_scroll.setWidgetResizable(True)
    self.panel_add_scroll.setWidget(self.panel_add_scroll_widget)
    """ Set label """
    self.panel_add_title_label.setAlignment(Qt.AlignCenter)
    self.panel_add_path_label.setAlignment(Qt.AlignCenter)
    """ Set size """
    self.panel_add_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_path_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = json.load(open(self.main_path+'/CONFIG/main_search/translate.json', 'r', encoding='utf-8'))
    _l = _global_config['language']
    self.panel_add_title_label.setText(_t['panel_add_title_label'][_l])
    self.panel_add_path_label.setText(f"{_t['panel_add_path_label'][_l]}")
    """ Set graphics """
    self.panel_add_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg', 256, 256)))
    """ Connect functions """
    self.panel_add_exit_button.clicked.connect(lambda: add_object_lists_exit(self))
    """ Create scroll objects  """
    for keys in _global_config['object_lists'].keys():
        button = QPushButton(self.panel_add_widget)
        button.setObjectName(f'panel_add_{keys}_button')
        button.setProperty('class', 'panel_add_button')
        self.panel_add_scroll_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{keys}')
        button.clicked.connect(lambda _, c_l=keys: add_object_section(self, choosen_list=c_l))
#______________________________________________________________________________________________________________________

def add_object_lists_exit(self):
    self.panel_add_widget.deleteLater()
    self.panel_add_widget = None
    self.panel_search_widget.setHidden(False)
    self.add_object = None
#______________________________________________________________________________________________________________________

def add_object_section(self, choosen_list):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    """ Set deafoult """
    self.choosen_list = choosen_list
    """ Create objects """
    self.panel_add_section_scroll = QScrollArea(self.panel_add_widget)
    self.panel_add_section_widget = QWidget(self.panel_add_section_scroll)
    self.panel_add_section_layout = QVBoxLayout(self.panel_add_section_widget)
    self.panel_add_section_exit_button = QPushButton(self.panel_add_widget)
    """ Set object name """
    self.panel_add_section_scroll.setObjectName('panel_add_section_scroll')
    self.panel_add_section_widget.setObjectName('panel_add_section_widget')
    self.panel_add_section_exit_button.setObjectName('panel_add_section_exit_button')
    """ Set property """
    self.panel_add_section_scroll.setProperty('class', 'panel_scroll_class')
    self.panel_add_section_widget.setProperty('class', 'panel_scroll_widget_class')
    self.panel_add_section_exit_button.setProperty('class', 'panel_exit_button_class')
    """ Set layout """
    self.panel_add_layout.addWidget(self.panel_add_section_scroll, 20, 5, 75, 90)
    self.panel_add_layout.addWidget(self.panel_add_section_exit_button, 2, 5, 6, 5)
    self.panel_add_section_layout.setSpacing(0)
    self.panel_add_section_layout.setContentsMargins(0,0,0,0)
    self.panel_add_section_widget.setLayout(self.panel_add_section_layout)
    """ Set widget """
    self.panel_add_scroll.setHidden(True)
    self.panel_add_exit_button.setHidden(True)
    self.panel_add_section_scroll.setHidden(False)
    self.panel_add_section_exit_button.setHidden(False)
    self.panel_add_section_scroll.setWidgetResizable(True)
    self.panel_add_section_scroll.setWidget(self.panel_add_section_widget)
    """ Set size """
    self.panel_add_section_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_section_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_section_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = self.panel_add_path_label.text()
    self.panel_add_path_label.setText(f'{_t} > {self.choosen_list}')
    """ Set Graphics """
    self.panel_add_section_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg', 256, 256)))
    """ Connect functions """
    self.panel_add_section_exit_button.clicked.connect(lambda: add_object_section_exit(self))
    """ Create scroll objects """
    for index, section in enumerate(_global_config['object_lists'][self.choosen_list], start=0):
        name = list(section.keys())[0]
        button = QPushButton(self.panel_add_section_widget)
        button.setObjectName(f'panel_add_{name}_button')
        button.setProperty('class', 'panel_add_button')
        self.panel_add_section_layout.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{name}')
        button.clicked.connect(lambda _, c_s=index: add_object_objects(self, choosen_section=c_s))
#______________________________________________________________________________________________________________________

def add_object_section_exit(self):
    self.panel_add_section_scroll.deleteLater()
    self.panel_add_section_exit_button.deleteLater()
    self.panel_add_section_scroll = None
    self.panel_add_section_exit_button = None 
    self.panel_add_scroll.setHidden(False)
    self.panel_add_exit_button.setHidden(False)
    _t = self.panel_add_path_label.text()
    self.panel_add_path_label.setText(str(_t)[:len(_t)-len(self.choosen_list)-3])
#______________________________________________________________________________________________________________________

def add_object_objects(self, choosen_section):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    """ Set deafoult """
    self.choosen_section_id = choosen_section
    self.choosen_section_name = list(_global_config['object_lists'][self.choosen_list][self.choosen_section_id].keys())[0]
    """ Create objectes """
    self.panel_add_object_scroll = QScrollArea(self.panel_add_widget)
    self.panel_add_object_widget = QWidget(self.panel_add_object_scroll)
    self.panel_add_object_layout = QVBoxLayout(self.panel_add_object_widget)
    self.panel_add_object_exit_button = QPushButton(self.panel_add_widget)
    """ Set object name """
    self.panel_add_object_scroll.setObjectName('panel_add_object_scroll')
    self.panel_add_object_widget.setObjectName('panel_add_object_widget')
    self.panel_add_object_exit_button.setObjectName('panel_add_object_exit_button')
    """ Set property """
    self.panel_add_object_scroll.setProperty('class', 'panel_scroll_class')
    self.panel_add_object_widget.setProperty('class', 'panel_scroll_widget_class')
    self.panel_add_object_exit_button.setProperty('class', 'panel_exit_button_class')
    """ Set layout """
    self.panel_add_layout.addWidget(self.panel_add_object_scroll, 20, 5, 75, 90)
    self.panel_add_layout.addWidget(self.panel_add_object_exit_button, 2, 5, 6, 5)
    self.panel_add_object_layout.setSpacing(0)
    self.panel_add_object_layout.setContentsMargins(0,0,0,0)
    self.panel_add_object_widget.setLayout(self.panel_add_object_layout)
    """ Set widget """
    self.panel_add_section_scroll.setHidden(True)
    self.panel_add_section_exit_button.setHidden(True)
    self.panel_add_object_scroll.setHidden(False)
    self.panel_add_object_exit_button.setHidden(False)
    self.panel_add_object_scroll.setWidgetResizable(True)
    self.panel_add_object_scroll.setWidget(self.panel_add_object_widget)
    """ Set size """
    self.panel_add_object_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_object_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.panel_add_object_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    """ Set text """
    _t = self.panel_add_path_label.text()
    self.panel_add_path_label.setText(f'{_t} > {self.choosen_section_name}')
    """ Set Graphics """
    self.panel_add_object_exit_button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/exit_'+_global_config['theme']+'.svg', 256, 256)))
    """ Connect functions """
    self.panel_add_object_exit_button.clicked.connect(lambda: add_object_objects_exit(self))
    """ Create scroll objects """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    button = QPushButton(self.panel_add_object_widget)
    button.setObjectName(f'panel_add_object_0_button')
    button.setProperty('class', 'panel_add_object_button')
    self.panel_add_object_layout.addWidget(button)
    button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/add_'+_global_config['theme']+'.svg', 256, 256)))
    button.clicked.connect(lambda _, index=0: add_object_to_list(self, place=index))
    for index, o in enumerate(_global_config['object_lists'][self.choosen_list][self.choosen_section_id][self.choosen_section_name], start=1):
        table = list(o.keys())[0]
        id_id = list(o.values())[0]
        label = QLabel(self.panel_add_object_widget)
        button = QPushButton(self.panel_add_object_widget)
        label.setObjectName(f'panel_add_object_{id_id}_label')
        button.setObjectName(f'panel_add_object_{id_id}_button')
        label.setProperty('class', 'panel_add_object_label')
        button.setProperty('class', 'panel_add_object_button')
        self.panel_add_object_layout.addWidget(label)
        self.panel_add_object_layout.addWidget(button)
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setText(cursor.execute(f'SELECT name FROM {table} WHERE id like "{id_id}";').fetchall()[0][0])
        button.setIcon(QIcon(load_svg(self.main_path+'/STYLE/IMG/icons/main/add_'+_global_config['theme']+'.svg', 256, 256)))
        button.clicked.connect(lambda _, index_x=index: add_object_to_list(self, place=index_x))
    cursor.close()
    database.close()
#______________________________________________________________________________________________________________________

def add_object_objects_exit(self):
    self.panel_add_object_scroll.deleteLater()
    self.panel_add_object_exit_button.deleteLater()
    self.panel_add_object_scroll = None
    self.panel_add_object_exit_button = None 
    self.panel_add_section_scroll.setHidden(False)
    self.panel_add_section_exit_button.setHidden(False)
    _t = self.panel_add_path_label.text()
    self.panel_add_path_label.setText(str(_t)[:len(_t)-len(self.choosen_section_name)-3])
#______________________________________________________________________________________________________________________

def add_object_to_list(self, place):
    """ Get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    conf = _global_config['object_lists'][self.choosen_list][self.choosen_section_id][self.choosen_section_name]
    conf.insert(place, self.add_object)
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4)
    self.parent.object_list_open()
    add_object_objects_exit(self)
    add_object_section_exit(self)
    add_object_lists_exit(self)
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