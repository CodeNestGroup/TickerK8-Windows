#
# Import
#

import json
import os
import sys

from PyQt5.QtCore import QSize, QRect, QPoint, QParallelAnimationGroup, QSequentialAnimationGroup, QPropertyAnimation, QTimer, Qt, QUrl, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
import pygame

from PyQt5.QtWidgets import QVBoxLayout, QPushButton
#-----------------------------------------------------------------------------------------------------------------------

#
# Window Control Functions
#

# Off
def app_off(app):
    sys.exit(app.exec_())

# Make Window
def app_set_screen_mode(self, app):
    if self.app_mode_fullscreen:
        app.showNormal()
        app.resize(app.app_size)
    else:
        app.showFullScreen()

    self.app_mode_fullscreen = not self.app_mode_fullscreen

# Main, Minimize
def app_minimize(app):
    app.showMinimized()

#-----------------------------------------------------------------------------------------------------------------------

#
# Sounds
#

# Button Sound
def buttons_sound():
    pygame.mixer.init()  # Initialize the mixer
    sound_file = os.path.abspath("../SOUND/button_clicked.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Notification Sound
def notification_sound():
    pygame.mixer.init()  # Initialize the mixer
    sound_file = os.path.abspath("../SOUND/notification_error.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def error_sound():
    pygame.mixer.init()  # Initialize the mixer
    sound_file = os.path.abspath("../SOUND/error.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

#----------------------------------------------------------------------------------------------------------------------

#
# Resize After Login
#

def resize_photo(photo, button):
    new_width = int(photo.height()*(button.width()/button.height()))
    scaled_pix = photo.copy((photo.width()-new_width) // 2, 0, new_width, photo.height())
    return scaled_pix.scaled(button.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)



def main_set_news_photo(self):
    pix_1 = QPixmap(os.getcwd()+'/TickerK8_app/app_files/PICTURES/UI/earth_background.png')
    pix_2 = QPixmap(os.getcwd()+'/TickerK8_app/app_files/PICTURES/UI/market_background.png')
    pix_3 = QPixmap(os.getcwd()+'/TickerK8_app/app_files/PICTURES/UI/country_background.png')

    self.main_down_right_button_world.setIcon(QIcon(resize_photo(pix_1, self.main_down_right_button_world)))
    self.main_down_right_button_world.setIconSize(self.main_down_right_button_world.size())
    self.main_down_right_button_market.setIcon(QIcon(resize_photo(pix_2, self.main_down_right_button_market)))
    self.main_down_right_button_market.setIconSize(self.main_down_right_button_market.size())
    self.main_down_right_button_country.setIcon(QIcon(resize_photo(pix_3, self.main_down_right_button_country)))
    self.main_down_right_button_country.setIconSize(self.main_down_right_button_country.size())

    self.main_down_right_label_world.setFixedSize(self.main_down_right_button_country.size())
    self.main_down_right_label_market.setFixedSize(self.main_down_right_button_country.size())
    self.main_down_right_label_country.setFixedSize(self.main_down_right_button_country.size())

def animate_icon(animation, target_size):
    #
    pass
#----------------------------------------------------------------------------------------------------------------------

from _15_CustomWidgets import news_main_widget, news_form_widget
import mysql.connector

class news_controller(object):
    def __init__(self, main_self):
        self.main_self = main_self
        self.window_widget = self.main_self.window_widget
        self._news_main_widget = None
        self._news_form_widget = None

    def get_news_main(self):
        _json_file = json.load(open(os.getcwd() + '/TickerK8_app/app_files/JSON/CONFIG/_00_main_config.json'))
        _connect = mysql.connector.connect(
            host=_json_file['__SQL__']['_host_'],
            user=_json_file['__SQL__']['_user_'],
            password=_json_file['__SQL__']['_password_'],
            database=_json_file['__SQL__']['_database_']
        )
        _cursor = _connect.cursor()
        _cursor.execute('SELECT id, json_file FROM news LIMIT 5;')
        _result = _cursor.fetchall()
        _connect.close()
        return _result

    def news_main_create_widget(self):
        self._news_main_widget = news_main_widget(self.main_self.main_center_right_widget, self.window_widget, self.get_news_main())
        self.main_self.main_center_right_widget_layout.addWidget(self._news_main_widget)
        self.main_self.main_center_right_deafoult_label.hide()
#-----------------------------------------------------------------------------------------------------------------------
