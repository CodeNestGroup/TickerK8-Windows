""" Import packages """
import json
import datetime
import sys
import os
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget
    )
from PyQt5.QtCore import (
    Qt,
    )
from PyQt5.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)
from PyQt5.QtSvg import (
    QSvgRenderer
)
#______________________________________________________________________________________________________________________

def login_widget_background_painter(self):
    _language = self.global_config['language']
    _texts_title = self.login_translate['login_welcome_title_label']
    _texts_sub = self.login_translate['login_welcome_sub_label']
    _colors = self.login_conf['background']
    _color_0 = '#000000'
    _color_1 = '#000000'
    _color_2 = '#000000'
    _alpha_1 = 'ff'
    _alpha_2 = 'ff'
    _x_1 = 0.0
    _x_2 = 1.0 
    _icons = self.login_conf['icon']
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
    """ Call text and icon change """
    if self.index_changed != _index:
        _icon = f'{self.main_path}/TickerK8_app/APP_FILES/STYLE/IMG/icons/login/{_icons[_index]}.svg'
        change_text_icon(self, _texts_title[_index][_language], _texts_sub[_index][_language], _icon)
        self.index_changed = _index
#______________________________________________________________________________________________________________________
""" change text icon"""
def change_text_icon(self, title='', sub='', icon=''):
    """ Variables """
    _title = title
    _sub = sub
    _icon = icon
    """ Set text """
    self.login_welcome_title_label.setText(_title)
    self.login_welcome_sub_label.setText(_sub)
    """ Set icon """
    render = QSvgRenderer(_icon)
    icon_pixmap = QPixmap(self.login_welcome_icon_label.height(), self.login_welcome_icon_label.height())
    icon_pixmap.fill(Qt.transparent)
    icon_painter = QPainter(icon_pixmap)
    render.render(icon_painter)
    icon_painter.end()
    self.login_welcome_icon_label.setPixmap(QPixmap(icon_pixmap))
#______________________________________________________________________________________________________________________
""" reset style """
def reset_style(self):
    self.login_login_lineedit.setStyleSheet('border: 0;')
    self.login_password_lineedit.setStyleSheet('border: 0;')
#______________________________________________________________________________________________________________________
