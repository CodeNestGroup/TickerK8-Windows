#   --- Import packages ---
import json
#   --- Import PyQt5 packages ---
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

def ui(self):
    self.setObjectName('Login_configuration_widget')
    self.title_label.setObjectName('title_label')
    self.info_label.setObjectName('info_label')
    self.left_button.setObjectName('left_button')
    self.exit_button.setObjectName('exit_button')
    self.right_button.setObjectName('right_button')
    self.accept_button.setObjectName('accept_button')
    self.navi_label.setObjectName('navi_label')
    self.left_button.setProperty('class', 'navi_button')
    self.exit_button.setProperty('class', 'navi_button')
    self.right_button.setProperty('class', 'navi_button')
    self.accept_button.setProperty('class', 'navi_button')
    self.layout.addWidget(self.title_label, 0, 0, 10, 100)
    self.layout.addWidget(self.info_label, 15, 0, 75, 100)
    self.layout.addWidget(self.left_button, 92, 10, 3, 10)
    self.layout.addWidget(self.exit_button, 97, 10, 3, 10)
    self.layout.addWidget(self.right_button, 92, 80, 3, 10)
    self.layout.addWidget(self.accept_button, 97, 80, 3, 10)
    self.layout.addWidget(self.navi_label, 92, 20, 6, 60)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.layout.setRowStretch(enc, 1)
        self.layout.setColumnStretch(enc, 1)
    self.setLayout(self.layout)
    self.show()
    self.accept_button.hide()
    self.title_label.setAlignment(Qt.AlignCenter)
    self.info_label.setAlignment(Qt.AlignCenter)
    self.navi_label.setAlignment(Qt.AlignCenter)
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.info_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.accept_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.navi_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def reload_style(self):
    self.setStyleSheet(self.main_path+'/PYTHON/login_config/c_style.css')
    # Dodać ikony

def retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r', encoding='utf-8'))['language']
    self.title_label.setText(t['title_label'][l])
    self.info_label.setText(t['info_label'][l][0])
    self.left_button.setText(t['left_button'][l])
    self.exit_button.setText(t['exit_button'][l])
    self.right_button.setText(t['right_button'][l])
    self.accept_button.setText(t['accept_button'][l])

def center_widget_setup_ui(self):
    self.center_widget.setObjectName('center_widget')
    self.center_layout.setSpacing(0)
    self.center_layout.setContentsMargins(0,0,0,0)
    self.center_widget.setLayout(self.center_layout)
    self.layout.addWidget(self.center_widget, 15, 0, 75, 100)
    self.center_widget.show()
    self.center_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def app_conf_ui(self):
    self.language_subtitle_label.setObjectName('language_subtitle_label')
    self.language_combobox.setObjectName('language_combobox')
    self.theme_subtitle_label.setObjectName('theme_subtitle_label')
    self.theme_combobox.setObjectName('theme_combobox')
    self.language_subtitle_label.setProperty('class', 'subtitle')
    self.theme_subtitle_label.setProperty('class', 'subtitle')
    self.language_combobox.setProperty('class', 'list')
    self.theme_combobox.setProperty('class', 'list')
    self.center_layout.addWidget(self.language_subtitle_label, 0, 0, 10, 50)
    self.center_layout.addWidget(self.language_combobox, 20, 20, 80, 20)
    self.center_layout.addWidget(self.theme_subtitle_label, 0, 50, 10, 50)
    self.center_layout.addWidget(self.theme_combobox, 20, 60, 80, 20)
    self.language_subtitle_label.setAlignment(Qt.AlignCenter)
    self.theme_subtitle_label.setAlignment(Qt.AlignCenter)
    self.accept_button.hide()
    self.language_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.language_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.theme_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    
def app_conf_retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_app_conf_translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r', encoding='utf-8'))['language']
    self.language_subtitle_label.setText(t['language_subtitle_label'][l])
    self.language_combobox.addItems(t['language_combobox'])
    self.language_combobox.setCurrentIndex(l)
    self.theme_subtitle_label.setText(t['theme_subtitle_label'][l])
    self.theme_combobox.addItems(t['theme_combobox'])

def sub_conf_ui(self):
    self.left_button.setObjectName('left_button')
    self.center_button.setObjectName('center_button')
    self.right_button.setObjectName('right_button')
    self.left_button.setProperty('class', 'sub_button')
    self.center_button.setProperty('class', 'sub_button')
    self.right_button.setProperty('class', 'sub_button')
    self.center_layout.addWidget(self.left_button, 0, 10, 100, 15)
    self.center_layout.addWidget(self.center_button, 0, 30, 100, 40)
    self.center_layout.addWidget(self.right_button, 0, 75, 100, 15)
    self.accept_button.hide()
    self.left_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.center_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.right_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def sub_conf_reload_style(self):
    s = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['subscription']
    l = [self.center_button, self.right_button, self.left_button]
    self.checked_button = l[s-1]
    self.checked_button.setStyleSheet('border: 2px solid green;')


def sub_conf_retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_sub_translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r', encoding='utf-8'))['language']
    self.left_button.setText(t['left_button'][l])
    self.center_button.setText(t['center_button'][l])
    self.right_button.setText(t['right_button'][l])

def accept_settings_ui(self):
    self.regulations_scroll.setObjectName('regulations_scroll')
    self.regulations_widget.setObjectName('regulations_widget')
    self.regulations_label.setObjectName('regulations_label')
    self.center_layout.addWidget(self.regulations_scroll, 0, 20, 100, 60)
    self.regulations_layout.addWidget(self.regulations_label, 0, 0)
    self.regulations_layout.setSpacing(0)
    self.regulations_layout.setContentsMargins(0,0,0,0)
    self.regulations_widget.setLayout(self.regulations_layout)
    self.accept_button.show()
    self.regulations_scroll.setWidget(self.regulations_widget)
    self.regulations_scroll.setWidgetResizable(True)
    self.regulations_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.regulations_label.setAlignment(Qt.AlignCenter)
    self.regulations_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.regulations_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.regulations_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

def accept_settings_reload_style(self):
    pass

def accept_settings_retranslate(self):
    t = json.load(open(self.main_path+'/PYTHON/login_config/j_accept_settings_translate.json', 'r', encoding='utf-8'))
    l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r', encoding='utf-8'))['language']
    self.regulations_label.setText(t['regulations_label'][l])
