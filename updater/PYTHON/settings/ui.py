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

def settings_ui(self):
    """ Set object name """
    self.setObjectName('settings_widget')
    self.menu_scroll.setObjectName('menu_scroll')
    self.menu_scroll_widget.setObjectName('menu_scroll_widget')
    self.menu_theme_button.setObjectName('menu_theme_button')
    self.menu_sound_button.setObjectName('menu_sound_button')
    self.menu_update_button.setObjectName('menu_update_button')
    self.menu_language_button.setObjectName('menu_language_button')
    self.exit_button.setObjectName('exit_button')
    """ Set property """
    self.menu_theme_button.setProperty('class', 'menu_buttons')
    self.menu_sound_button.setProperty('class', 'menu_buttons')
    self.menu_update_button.setProperty('class', 'menu_buttons')
    self.menu_language_button.setProperty('class', 'menu_buttons')
    """ Set layout """
    self.layout.addWidget(self.menu_scroll, 0, 0, 90, 30)
    self.layout.addWidget(self.exit_button, 90, 0, 10, 30)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    self.menu_scroll_layout.addWidget(self.menu_theme_button)
    self.menu_scroll_layout.addWidget(self.menu_sound_button)
    self.menu_scroll_layout.addWidget(self.menu_update_button)
    self.menu_scroll_layout.addWidget(self.menu_language_button)
    self.menu_scroll_layout.setSpacing(0)
    self.menu_scroll_layout.setContentsMargins(0,0,0,0)
    self.menu_scroll_widget.setLayout(self.menu_scroll_layout)
    """ Set widget """
    self.setHidden(False)
    self.menu_scroll.setWidgetResizable(True)
    self.menu_scroll.setWidget(self.menu_scroll_widget)
    self.menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    """ Set label """
    """ Set button """
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_theme_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_sound_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_update_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.menu_language_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def settings_reload_style(self):
    g = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    t = g['theme']
    self.setStyleSheet(open(str(self.main_path+'/updater/STYLE/CSS/settings/'+t+'.css')).read())
    self.exit_button.setIcon(QIcon(load_svg(str(self.main_path+'/updater/STYLE/IMG/icons/settings/exit_vintage_elegance_d.svg'), 256, 256)))

def settings_retranslate(self):
    t = json.load(open(self.main_path+'/updater/CONFIG/settings/menu_translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.menu_theme_button.setText(t['menu_theme_button'][l])
    self.menu_sound_button.setText(t['menu_sound_button'][l])
    self.menu_update_button.setText(t['menu_update_button'][l])
    self.menu_language_button.setText(t['menu_language_button'][l])
#______________________________________________________________________________________________________________________

def sub_menu_ui(self):
    """ Set object name """
    self.sub_menu_scroll.setObjectName('sub_menu_scroll')
    self.sub_menu_widget.setObjectName('sub_menu_widget')
    self.title_label.setObjectName('title_label')
    """ Set layout """
    self.layout.addWidget(self.sub_menu_scroll, 0, 30, 100, 70)
    self.sub_menu_layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.sub_menu_layout.setSpacing(0)
    self.sub_menu_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.sub_menu_layout.setRowStretch(enc, 1)
        self.sub_menu_layout.setColumnStretch(enc, 1)
    self.sub_menu_widget.setLayout(self.sub_menu_layout)
    """ Set widget """
    self.sub_menu_scroll.setWidgetResizable(True)
    self.sub_menu_scroll.setWidget(self.sub_menu_widget)
    self.sub_menu_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    """ Set label """
    self.title_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.sub_menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sub_menu_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________

def theme_ui(self):
    """ Set object name """
    self.day_night_label.setObjectName('day_night_label')
    self.day_night_button.setObjectName('day_night_button')
    self.list_label.setObjectName('list_label')
    self.list_combobox.setObjectName('list_combobox')
    """ Set property """
    self.day_night_label.setProperty('class', 'name_label')
    self.day_night_button.setProperty('class', 'value_button')
    self.list_label.setProperty('class', 'name_label')
    self.list_combobox.setProperty('class', 'value_combobox')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.day_night_label, 20, 0, 30, 50)
    self.sub_menu_layout.addWidget(self.day_night_button, 20, 50, 30, 50)
    self.sub_menu_layout.addWidget(self.list_label, 60, 0, 30, 50)
    self.sub_menu_layout.addWidget(self.list_combobox, 60, 50, 30, 50)
    """ Set widget """
    """ Set label """
    self.day_night_label.setAlignment(Qt.AlignCenter)
    self.list_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.day_night_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.day_night_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.list_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.list_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def theme_retranslate(self):
    t = json.load(open(self.main_path+'/updater/CONFIG/settings/theme_translate.json', 'r', encoding='utf-8'))
    g = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    l = g['language']
    d = g['theme_index']
    self.title_label.setText(t['title_label'][l])
    self.day_night_label.setText(t['day_night_label'][l])
    self.day_night_button.setText(t['day_night_button'][l][d])
    self.list_combobox.setCurrentIndex(d)
    self.list_label.setText(t['list_label'][l])
#______________________________________________________________________________________________________________________

def sound_ui(self):
    """ Set object name """
    self.button_label.setObjectName('button_label')
    self.button_button.setObjectName('button_button')
    """ Set property """
    self.button_label.setProperty('class', 'name_label')
    self.button_button.setProperty('class', 'value_button')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.button_label, 20, 0, 15, 50)
    self.sub_menu_layout.addWidget(self.button_button, 20, 50, 15, 50)
    """ Set widget """
    """ Set label """
    self.button_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.button_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.button_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def sound_retranslate(self):
    t = json.load(open(self.main_path+'/updater/CONFIG/settings/sound_translate.json', 'r', encoding='utf-8'))
    g = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    l = g['language']
    s = g['sound']
    self.title_label.setText(t['title_label'][l])
    self.button_label.setText(t['button_label'][l])
    self.button_button.setText(t['button_button'][l][s['button']])
#______________________________________________________________________________________________________________________

def update_ui(self):
    """ Set object name """
    self.version_heading1_label.setObjectName('version_heading1_label')
    self.version_desc_label.setObjectName('version_desc_label')
    self.version_desc_value_label.setObjectName('version_desc_label')
    self.version_changelog_label.setObjectName('version_changelog_label')
    self.version_changelog_button.setObjectName('version_changelog_button')
    self.advanced_heading1_label.setObjectName('advanced_heading1_label')
    self.advanced_capacity_label.setObjectName('advanced_capacity_label')
    self.advanced_capacity_combobox.setObjectName('advanced_capacity_combobox')
    """ Set property """
    self.version_heading1_label.setProperty('class', 'heading1')
    self.version_desc_label.setProperty('class', 'name_label')
    self.version_desc_value_label.setProperty('class', 'value_label')
    self.version_changelog_label.setProperty('class', 'name_label')
    self.version_changelog_button.setProperty('class', 'value_button')
    self.advanced_heading1_label.setProperty('class', 'heading1')
    self.advanced_capacity_label.setProperty('class', 'name_label')
    self.advanced_capacity_combobox.setProperty('class', 'value_combobox')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.version_heading1_label, 20, 0, 10, 100)
    self.sub_menu_layout.addWidget(self.version_desc_label, 35, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.version_desc_value_label, 35, 50, 5, 50)
    self.sub_menu_layout.addWidget(self.version_changelog_label, 45, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.version_changelog_button, 45, 50, 5, 50)
    self.sub_menu_layout.addWidget(self.advanced_heading1_label, 90, 0, 10, 100)
    self.sub_menu_layout.addWidget(self.advanced_capacity_label, 105, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.advanced_capacity_combobox, 105, 50, 5, 50)
    """ Set widget """
    """ Set label """
    self.version_heading1_label.setAlignment(Qt.AlignCenter)
    self.version_desc_label.setAlignment(Qt.AlignCenter)
    self.version_desc_label.setWordWrap(True)
    self.version_desc_value_label.setAlignment(Qt.AlignCenter)
    self.version_desc_value_label.setWordWrap(True)
    self.version_changelog_label.setAlignment(Qt.AlignCenter)
    self.version_changelog_label.setWordWrap(True)
    self.advanced_heading1_label.setAlignment(Qt.AlignCenter)
    self.advanced_capacity_label.setAlignment(Qt.AlignCenter)
    self.advanced_capacity_label.setWordWrap(True)
    """ Set button """
    """ Set size """
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_heading1_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_desc_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_desc_value_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_changelog_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.version_changelog_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.advanced_heading1_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.advanced_capacity_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.advanced_capacity_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def update_retranslate(self):
    t = json.load(open(self.main_path+'/updater/CONFIG/settings/update_translate.json', 'r', encoding='utf-8'))
    g = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    d = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/changelog.json', 'r', encoding='utf-8'))['name']
    l = g['language']
    c = g['capacity']
    self.title_label.setText(t['title_label'][l])
    self.version_heading1_label.setText(t['version_heading1_label'][l])
    self.version_desc_label.setText(t['version_desc_label'][l])
    self.version_desc_value_label.setText(d)
    self.version_changelog_label.setText(t['version_changelog_label'][l])
    self.version_changelog_button.setText(t['version_changelog_button'][l])
    self.advanced_heading1_label.setText(t['advanced_heading1_label'][l])
    self.advanced_capacity_label.setText(t['advanced_capacity_label'][l])
    self.advanced_capacity_combobox.setCurrentIndex(c)
#______________________________________________________________________________________________________________________

def language_ui(self):
    """ Set object name """
    self.type_label.setObjectName('type_label')
    self.type_combobox.setObjectName('type_combobox')
    """ Set property """
    self.type_label.setProperty('class', 'name_label')
    self.type_combobox.setProperty('class', 'value_combobox')
    """ Set layout """
    self.sub_menu_layout.addWidget(self.type_label, 35, 0, 5, 50)
    self.sub_menu_layout.addWidget(self.type_combobox, 35, 50, 5, 50)
    """ Set widget """
    """ Set label """
    self.type_label.setAlignment(Qt.AlignCenter)
    """ Set button """
    """ Set size """
    self.type_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.type_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def language_retranslate(self):
    t = json.load(open(self.main_path+'/updater/CONFIG/settings/language_translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.title_label.setText(t['title_label'][l])
    self.type_label.setText(t['type_label'][l])
    self.type_combobox.setCurrentIndex(l)

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
