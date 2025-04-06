""" Import """
""" Import system and operating system packages """
import os  # OS-related operations (paths, directories, environment variables, etc.)
import sys # Sys operations (exit).
import shutil  # File and directory manipulation (copying, moving, deleting)
import subprocess  # Running external system processes
import traceback # For save error in logs
import socket # For ping.
#_______________________________________________________________________________________________________________________
""" Import date and time modules """
import datetime  # Handling dates and times
import time  # Time-related functions (delays, timestamps, etc.)
#_______________________________________________________________________________________________________________________
""" Import file handling modules """
import io  # Input/output operations (file and byte streams)
import zipfile  # Working with ZIP archives (compression and extraction)
#_______________________________________________________________________________________________________________________
""" Import network modules """
import urllib.request  # Fetching resources from the internet (files, web pages)
import requests  # Sending HTTP requests, retrieving and sending data
#_______________________________________________________________________________________________________________________
""" Import data processing modules """
import json  # Encoding and decoding JSON data
import hashlib  # Generating cryptographic hashes (e.g., SHA256, MD5)
#_______________________________________________________________________________________________________________________
""" Import database module """
import mysql.connector  # Connecting to a MySQL database and executing SQL queries
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Widgets """
from PyQt5.QtWidgets import (QWidget, # Widget, simple widget.
                             QVBoxLayout, # Vertical Layout.
                             QPushButton, # Button, simple button.
                             QSizePolicy, # Size policy.
                             QLabel) # Label, simple label.
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Core """
from PyQt5.QtCore import (QUrl, # Url.
                          Qt, # Qt.
                          QPoint, # Point.
                          QRect, # Rectangle.
                          QSize, # Size.
                          QTimer, # Timer.
                          QThread, # Thread.
                          pyqtSignal) # Signal.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QDesktopServices, # Desktop services.
                         QPixmap, # Graphic.
                         QIcon, # Icon.
                         QPainter) # Painter.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg """
from PyQt5.QtSvg import QSvgRenderer # Render Svg.
########################################################################################################################
""" Controller main"""
class controller_main:
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try:
            super().__init__() # Call class.
            self.main_self = main_self # Main self, main objects of application.
            self.main_self.controller_settings.set_translate()  # Setup text.
            self.main_self.controller_settings.set_theme() # Setup theme.
            self.main_setup_changelog_thread = None # Set defoult
            self.main_self.controller_download = None # Set defoult
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Main changelog controller """
    def main_changelog_controller(self, signal):
        try: # Try
            try:
                self.main_self.main_changelog_scroll_widget.deleteLater() # Delte main changelog scroll widget if exists.
            except:
                pass
            if not signal: # Call error setup
                self.main_self.main_changelog_error_widget.controller_error() # No connection.
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][3]) # Set text of notification
                if self.main_self.controller_download == None: # Check if download thread is active
                    self.main_self.main_start_button.setText(self.main_self.settings_translate_file['main_start_button'][3][self.main_self.settings_config_file['__language__']]) # Set text of main start button
                    self.main_self.main_start_button.setDisabled(True) # Disabled button
                    self.main_self.settings_update_option_check_button.setDisabled(True) # Disabled button
                    self.main_self.update_changelog_download_button.setDisabled(True) # Disabled button
                self.main_self.controller_notification.open() # Open notification
                self.main_self.main_settings_social_media_discord_button.setDisabled(True) # Disabled button
                self.main_self.main_settings_social_media_github_button.setDisabled(True) # Disabled button
                self.main_self.main_settings_social_media_instagram_button.setDisabled(True) # Disabled button
                self.main_self.report_send_button.setDisabled(True) # Disabled button
            else: # Call setup changelog
                self.main_self.main_changelog_error_widget.controller_loading() # Loading changelog.
                self.main_self.main_start_button.setText(self.main_self.settings_translate_file['main_start_button'][0][self.main_self.settings_config_file['__language__']]) # Set text of main start button
                self.main_self.main_settings_social_media_discord_button.setDisabled(False) # Enabled button
                self.main_self.main_settings_social_media_github_button.setDisabled(False) # Enabled button
                self.main_self.main_settings_social_media_instagram_button.setDisabled(False) # Enabled button
                self.main_self.main_start_button.setDisabled(False) # Enabled button
                self.main_self.settings_update_option_check_button.setDisabled(False) # Enabled button
                self.main_self.report_send_button.setDisabled(False) # Enabled button
                self.main_self.update_changelog_download_button.setDisabled(False) # Enabled button
                self.main_setup_changelog_thread = self.main_self.controller_update.get_releses() # Create thread get release
                self.main_setup_changelog_thread.changelog_fetched.connect(self.setup_main_changelog) # Connect func to setup Widget
                self.main_setup_changelog_thread.finished.connect(self.setup_thread_clean) # Connect cleanup function
                self.main_setup_changelog_thread.start() # Start Thread
            self.main_self.main_changelog_scroll.setHidden(True) # Hide main changelog scroll.
            self.main_self.main_changelog_error_widget.setHidden(False) # Show main changelog error widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Setup main changelog """
    def setup_main_changelog(self):
        try: # Try setup widget
            self.main_self.main_changelog_scroll_widget = QWidget(self.main_self.main_changelog_scroll) # Create widget for main changelog scroll
            self.main_self.main_changelog_scroll_widget_layout = QVBoxLayout(self.main_self.main_changelog_scroll_widget) # Create layout for widget.
            self.main_self.main_changelog_scroll_widget_layout.setSpacing(0)
            self.main_self.main_changelog_scroll_widget_layout.setContentsMargins(0,0,0,0)
            self.main_self.main_changelog_scroll_widget.setLayout(self.main_self.main_changelog_scroll_widget_layout) # Set Layout for main changlog widget.
            for release in date_releses: # Get releses from github.
                button = QPushButton(self.main_self.main_changelog_scroll_widget) # Create button.
                button.setProperty('class', 'main_changelog_buttons') # Create class for button.
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Set size of button.
                button.setText(release['name']) # Set text from.
                button.clicked.connect(lambda _, r=release: self.main_to_changlog(r)) # Open changelog
                self.main_self.main_changelog_scroll_widget_layout.addWidget(button) # Add button to layout.
            self.main_self.main_changelog_scroll.setWidget(self.main_self.main_changelog_scroll_widget) # Set widget to scroll.
            self.main_self.main_changelog_scroll.setHidden(False) # Hide main changelog scroll.
            self.main_self.main_changelog_error_widget.setHidden(True) # Show main changelog error widget.
        except Exception: # Except if problem with code
            try: # If widget was created, delete
                self.main_self.main_changelog_scroll_widget.deleteLater() # Delete widget
            except: # If not pass
                pass
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Setup thread clean """
    def setup_thread_clean(self):
        self.main_setup_changelog_thread.deleteLater() # Delete thread get release
        self.main_setup_changelog_thread = None # Set deafoult
#_______________________________________________________________________________________________________________________
    """ Open Discord """
    def open_discord(self):
        try:  # Try open.
            url = QUrl("https://discord.gg/twZ3SNcC")  # Set url for discord url adress.
            try:
                QDesktopServices.openUrl(url)  # Open url adress in user browser.
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][2])
                self.main_self.controller_notification.open()
            except:
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][1])
                self.main_self.controller_notification.open()
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
    # _______________________________________________________________________________________________________________________
    """ Open Instagram """
    def open_instagram(self):
        try:  # Try open.
            url = QUrl("https://www.instagram.com/codenestgroup/")  # Set url for instagram url adress.
            try:
                QDesktopServices.openUrl(url)  # Open url adress in user browser.
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][2])
                self.main_self.controller_notification.open()
            except:
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][1])
                self.main_self.controller_notification.open()
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
    # _______________________________________________________________________________________________________________________
    """ Open Github """
    def open_github(self):
        try:  # Try open.
            url = QUrl("https://github.com/CodeNestGroup")  # Set url for gitHub url adress.
            try:
                QDesktopServices.openUrl(url)  # Open url adress in user browser.
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][2])
                self.main_self.controller_notification.open()
            except:
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][1])
                self.main_self.controller_notification.open()
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Open TcikerK8 App """
    def open_TickerK8(self):
        try:  # Try open app
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(
                self.main_self.main_path+'/TickerK8.bat',
                startupinfo=startupinfo,
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            sys.exit(0)
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Main to settings """
    def main_to_settings(self):
        try: # Try go from main widget to settings widget.
            self.main_self.main_widget.setHidden(True) # Hide main widget.
            self.main_self.settings_widget.setHidden(False) # Show settings widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Settings to main """
    def settings_to_main(self):
        try: # Try go from settings to main widget.
            self.main_self.settings_widget.setHidden(True) # Hide settings widget.
            self.main_self.main_widget.setHidden(False) # Show main widget
            self.main_self.controller_settings.reset() # Set settings widget deafult.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Main to changlog """
    def main_to_changlog(self, release):
        try: # Try go from main to changlog widget.
            self.main_self.controller_update.set_data(release) # Set data of releses to setup changlog.
            self.main_self.controller_update.setup_changelog() # Set changlog widget.
            self.main_self.update_changelog_exit_button.disconnect() # Debug, deisconnect functions from buttons.
            self.main_self.update_changelog_exit_button.clicked.connect(self.changlog_to_main) # Connect function, go from changlog to main.
            self.main_self.main_widget.setHidden(True) # Hide main widget.
            self.main_self.update_background_widget.setHidden(False) #  Show update window.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Changlog to main """
    def changlog_to_main(self):
        try: # Try go from changelog to main widget.
            try: # If update changlog widget exsists, delete
                self.main_self.update_changlog_scroll_widget.deleteLater() # Delete widget from scroll when exit from changlog.
            except: # If no, pass
                pass
            self.main_self.update_background_widget.setHidden(True) # Hide update widget.
            self.main_self.main_widget.setHidden(False) # Show main widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Settings to changlog """
    def settings_to_changlog(self):
        try: # Try go from settings to changelog widget.
            self.main_self.controller_update.set_data(self.main_self.changelog_file)  # Set date to changelog
            self.main_self.controller_update.setup_changelog()  # Open update changelog
            self.main_self.update_changelog_exit_button.disconnect() # Debug, deisconnect functions from buttons.
            self.main_self.update_changelog_exit_button.clicked.connect(self.changlog_to_settings) # Connect function, go from changlog to main.
            self.main_self.update_changelog_download_button.setHidden(True) # Hide update download buttom, becouse this is current update.
            self.main_self.settings_widget.setHidden(True) # Hide settings widget.
            self.main_self.update_background_widget.setHidden(False) # Show update widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Changlog to settings """
    def changlog_to_settings(self):
        try: # Try go from changelog to settings widget.
            try: # If update changlog widget exsists, delete
                self.main_self.update_changlog_scroll_widget.deleteLater() # Delete widget from scroll when exit from changlog.
            except: # If no, pass
                pass
            self.main_self.update_changelog_download_button.setHidden(False) # Show dwonload buttom, reset update widget.
            self.main_self.update_background_widget.setHidden(True) # Hide update widget.
            self.main_self.settings_widget.setHidden(False) # Show settings widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Settings to report """
    def settings_to_report(self):
        try: # Try go from settings to report widget.
            self.main_self.report_widget.setHidden(False) # Show report widget.
            self.main_self.settings_widget.setHidden(True) # Hide settings widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Report to settings """
    def report_to_settings(self):
        try: # Try go from report to settings widget.
            self.main_self.settings_widget.setHidden(False) # Show settings widget.
            self.main_self.report_widget.setHidden(True) # Hide report widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Alert to changlog """
    def alert_to_changlog(self):
        try: # Try go from alert to changelog widget.
            self.main_self.alert_download_button.setHidden(True) # Hide alert download button
            self.main_self.controller_update.setup_changelog()  # Open update changelog
            self.main_self.update_changelog_exit_button.disconnect() # Debug, deisconnect functions from buttons.
            self.main_self.update_changelog_exit_button.clicked.connect(self.changlog_to_settings) # Connect function, go from changlog to main.
            self.main_self.settings_widget.setHidden(True)  # Hide settings widget.
            self.main_self.alert_background_widget.setHidden(True) # Hide alet widget.
            self.main_self.update_background_widget.setHidden(False) # Show update widget.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################
""" Controller settings """
class controller_settings:
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try:
            self.main_self = main_self # Main self, main objects of application.
            self.opened_widget = None # Variable that keep withone of sub widgets is opened
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Open Close sub widget"""
    def open_close_sub_widgets(self, to_open):
        try: # Try change opened widget.
            if self.opened_widget: # Check if opened widget is not none
                self.opened_widget.setHidden(True) # Hide opened widget
            to_open.setHidden(False) # Show Widget
            self.opened_widget = to_open # Save opened widget
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Reset """
    def reset(self):
        try: # Try to set deafoult setting.
            if self.opened_widget: # Check if was opened widget
                self.opened_widget.setHidden(True) # Hide opened widget
                self.opened_widget = None # Reset to deafult
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Change language, change and save in json, call function to retranslate application """
    def change_language(self):
        try: # Try open json file, debug
            self.main_self.settings_config_file['__language__'] = int(self.main_self.settings_language_type_combobox.currentIndex())  # Change language index
            json.dump(self.main_self.settings_config_file, open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'), indent=4) # Save changes
            self.main_self.settings_config_file = json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r')) # Reload settings config file
            self.set_translate() # Call funcation that retranslate application
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Change theme, change and save in json, call function to set theme of application """
    def change_theme(self):
        try: # Try change theme in application
            self.main_self.settings_config_file['__theme__'] = int(self.main_self.settings_theme_list_combobox.currentIndex()) # Change theme index
            json.dump(self.main_self.settings_config_file, open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'), indent=4) # Save changes
            self.main_self.settings_config_file = json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))  # Reload settings config file
            self.set_theme() # Call func that change theme
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Change day night mode """
    def change_day_night(self):
        try: # Try change theme from day to night or night to day
            _index = self.main_self.settings_theme_list_combobox.currentIndex() # Get index of lis
            if _index%2: # Check
                self.main_self.settings_theme_list_combobox.setCurrentIndex(int(_index-1)) # Set and call function thaht change the theme
            else: # Check
                self.main_self.settings_theme_list_combobox.setCurrentIndex(int(_index+1)) # Set and call function thaht change the theme
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Translate, function that retranslate application """
    def set_translate(self):
        try: # Try retranslate application
            index_language = self.main_self.settings_config_file['__language__'] # Set local variable of config language value
#_______________________________________________________________________________________________________________________
            """ Self items """
#_______________________________________________________________________________________________________________________
            """ Main widget """
#_______________________________________________________________________________________________________________________
            """ Main changelog """
            self.main_self.main_changelog_error_widget.loading_message_label.setText(self.main_self.settings_translate_file['main_changelog_error_widget'][0][self.main_self.settings_config_file['__language__']])
#_______________________________________________________________________________________________________________________
            """ Main logo """
#_______________________________________________________________________________________________________________________
            """ Main settings"""
#_______________________________________________________________________________________________________________________
            """ Main update """
#_______________________________________________________________________________________________________________________
            """ Main start button"""
            self.main_self.main_start_button.setText(self.main_self.settings_translate_file['main_start_button'][0][index_language])
#_______________________________________________________________________________________________________________________
            """ Settings widget"""
#_______________________________________________________________________________________________________________________
            """ Settings exit button """
            self.main_self.settings_exit_button.setText(self.main_self.settings_translate_file['settings_exit_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Settings menu scroll """
            self.main_self.settings_menu_theme_button.setText(self.main_self.settings_translate_file['settings_menu_theme_button'][index_language])
            self.main_self.settings_menu_sound_button.setText(self.main_self.settings_translate_file['settings_menu_sound_button'][index_language])
            self.main_self.settings_menu_update_button.setText(self.main_self.settings_translate_file['settings_menu_update_button'][index_language])
            self.main_self.settings_mneu_language_button.setText(self.main_self.settings_translate_file['settings_mneu_language_button'][index_language])
            self.main_self.settings_menu_report_button.setText(self.main_self.settings_translate_file['settings_menu_report_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Settings sub scroll """
#_______________________________________________________________________________________________________________________
            """ Settings sub theme widget """
            self.main_self.settings_theme_title_label.setText(self.main_self.settings_translate_file['settings_theme_title_label'][index_language])
            self.main_self.settings_theme_d_n_label.setText(self.main_self.settings_translate_file['settings_theme_d_n_label'][index_language])
            self.main_self.settings_theme_d_n_button.setText(self.main_self.settings_translate_file['settings_theme_d_n_button'][index_language][self.main_self.settings_config_file['__theme__']])
            self.main_self.settings_theme_list_label.setText(self.main_self.settings_translate_file['settings_theme_list_label'][index_language])
#_______________________________________________________________________________________________________________________
            """ Settings sub sound widget"""
            self.main_self.settings_sound_title_label.setText(self.main_self.settings_translate_file['settings_sound_title_label'][index_language])
            self.main_self.settings_sound_button_label.setText(self.main_self.settings_translate_file['settings_sound_button_title_label'][index_language])
            self.main_self.settings_sound_button_button.setText(self.main_self.settings_translate_file['settings_sound_button_button'][index_language][self.main_self.settings_config_file['__sound_button__']])
            self.main_self.settings_sound_alert_label.setText(self.main_self.settings_translate_file['settings_sound_alert_title_label'][index_language])
            self.main_self.settings_sound_alert_button.setText(self.main_self.settings_translate_file['settings_sound_alert_button'][index_language][self.main_self.settings_config_file['__sound_alert__']])
            self.main_self.settings_sound_notification_label.setText(self.main_self.settings_translate_file['settings_sound_notification_title_label'][index_language])
            self.main_self.settings_sound_notification_button.setText(self.main_self.settings_translate_file['settings_sound_notification_button'][index_language][self.main_self.settings_config_file['__sound_notification__']])
#_______________________________________________________________________________________________________________________
            """ Settings sub update widget """
            self.main_self.settings_update_title_label.setText(self.main_self.settings_translate_file['settings_update_title_label'][index_language])
            self.main_self.settings_update_version_subtitle_label.setText(self.main_self.settings_translate_file['settings_update_version_subtitle_label'][index_language])
            self.main_self.settings_update_version_desc_title_label.setText(self.main_self.settings_translate_file['settings_update_version_desc_title_label'][index_language])
            self.main_self.settings_update_version_desc_label.setText(self.main_self.changelog_file['name'])
            self.main_self.settings_update_version_changelog_title_label.setText(self.main_self.settings_translate_file['settings_update_version_changlog_title_label'][index_language])
            self.main_self.settings_update_version_changelog_button.setText(self.main_self.settings_translate_file['settings_update_version_changlog_button'][index_language])
            self.main_self.settings_update_option_subtitle_label.setText(self.main_self.settings_translate_file['settings_update_option_subtitle_label'][index_language])
            self.main_self.settings_update_option_autoupdate_title_label.setText(self.main_self.settings_translate_file['settings_update_option_autoupdate_title_label'][index_language])
            self.main_self.settings_update_option_autoupdate_button.setText(self.main_self.settings_translate_file['settings_update_option_autoupdate_button'][index_language][self.main_self.settings_config_file['__auto_update__']])
            self.main_self.settings_update_option_check_title_label.setText(self.main_self.settings_translate_file['settings_update_option_check_title_label'][index_language])
            self.main_self.settings_update_option_check_button.setText(self.main_self.settings_translate_file['settings_update_option_check_button'][0][index_language])
            self.main_self.settings_update_advanced_subtitle_label.setText(self.main_self.settings_translate_file['settings_update_advanced_subtitle_label'][index_language])
            self.main_self.settings_update_advanced_capacity_title_label.setText(self.main_self.settings_translate_file['settings_update_advanced_capacity_title_label'][index_language])
            self.main_self.settings_update_advanced_capacity_combobox.setCurrentIndex(self.main_self.settings_config_file['__capacity__'])
            self.main_self.settings_update_advanced_verification_title_label.setText(self.main_self.settings_translate_file['settings_update_advanced_verification_title_label'][index_language])
            self.main_self.settings_update_advanced_verification_button.setText(self.main_self.settings_translate_file['settings_update_advanced_verification_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Settings sub language widget """
            self.main_self.settings_language_title_label.setText(self.main_self.settings_translate_file['settings_language_title_label'][index_language])
            self.main_self.settings_language_type_label.setText(self.main_self.settings_translate_file['settings_language_type_label'][index_language])
            self.main_self.settings_language_type_combobox.setCurrentIndex(index_language)
#_______________________________________________________________________________________________________________________
            """ Settings sub report widget """
            self.main_self.settings_report_title_label.setText(self.main_self.settings_translate_file['settings_report_title_label'][index_language])
            self.main_self.settings_report_autoreport_title_label.setText(self.main_self.settings_translate_file['settings_report_autoreport_title_label'][index_language])
            self.main_self.settings_report_autoreport_button.setText(self.main_self.settings_translate_file['settings_report_autoreport_button'][index_language][self.main_self.settings_config_file['__auto_report__']])
            self.main_self.settings_report_sendreport_title_label.setText(self.main_self.settings_translate_file['settings_report_sendreport_title_label'][index_language])
            self.main_self.settings_report_sendreport_button.setText(self.main_self.settings_translate_file['settings_report_sendreport_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Report widget """
            self.main_self.report_send_button.setText(self.main_self.settings_translate_file['report_send_button'][index_language])
            self.main_self.report_clear_button.setText(self.main_self.settings_translate_file['report_clear_button'][index_language])
            self.main_self.report_exit_button.setText(self.main_self.settings_translate_file['report_exit_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Update widget """
            self.main_self.update_changelog_title_label.setText(self.main_self.settings_translate_file['update_changlog_title_label'][index_language])
            self.main_self.update_changelog_download_button.setText(self.main_self.settings_translate_file['update_changlog_download_button'][index_language])
            self.main_self.update_changelog_exit_button.setText(self.main_self.settings_translate_file['update_changlog_exit_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Notification widget """
            self.main_self.notification_exit_button.setText(self.main_self.settings_translate_file['notification_exit_button'][index_language])
#_______________________________________________________________________________________________________________________
            """ Alert widget """
            self.main_self.alert_download_button.setText(self.main_self.settings_translate_file['alert_download_button'][index_language])
            self.main_self.alert_exit_button.setText(self.main_self.settings_translate_file['alert_exit_button'][index_language])
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Theme, function that set theme for application """
    def set_theme(self):
        try: # Try set theme
            index_theme = self.main_self.settings_config_file['__theme__'] # Set local variable of config theme value
            self.main_self.settings_theme_d_n_button.setText(self.main_self.settings_translate_file['settings_theme_d_n_button'][self.main_self.settings_config_file['__language__']][index_theme]) # Set text of button
            self.main_self.settings_theme_list_combobox.setCurrentIndex(index_theme) # Set index of theme
            self.main_self.setStyleSheet(open(self.main_self.main_path+self.main_self.settings_theme_file[index_theme]).read()) # Set style for self (widget)
#_______________________________________________________________________________________________________________________
            # Main Logo
            #self.main_self.main_logo_c_n_g_label.setPixmap(self.load_svg(self.main_self.file_app_path+_path_icon_file['main_logo_c_n_g_label'], self.main_self.main_logo_c_n_g_label.size()))
            #self.main_self.main_logo_ticker_label.setPixmap(QIcon(self.main_self.file_app_path+_path_icon_file['main_logo_ticker_label']).pixmap(self.main_self.main_logo_ticker_label.size()))
#_______________________________________________________________________________________________________________________
            """ Set iocns for buttons"""
            self.main_self.main_changelog_error_widget.icon_label.setPixmap(self.load_svg(self.main_self.main_path+self.main_self.settings_icon_file['icon_label'][self.main_self.settings_config_file['__theme__']], 192, 192))
            self.main_self.main_settings_open_button.setIcon(QIcon(self.main_self.main_path+self.main_self.settings_icon_file['main_settings_open_button'][index_theme]))
            self.main_self.main_settings_open_button.setIconSize(self.main_self.main_settings_button_size)
            self.main_self.main_settings_social_media_instagram_button.setIcon(QIcon(self.main_self.main_path+self.main_self.settings_icon_file['main_settings_social_media_instagram_button'][index_theme]))
            self.main_self.main_settings_social_media_instagram_button.setIconSize(self.main_self.main_settings_button_size)
            self.main_self.main_settings_social_media_github_button.setIcon(QIcon(self.main_self.main_path+self.main_self.settings_icon_file['main_settings_social_media_github_button'][index_theme]))
            self.main_self.main_settings_social_media_github_button.setIconSize(self.main_self.main_settings_button_size)
            self.main_self.main_settings_social_media_discord_button.setIcon(QIcon(self.main_self.main_path+self.main_self.settings_icon_file['main_settings_social_media_discord_button'][index_theme]))
            self.main_self.main_settings_social_media_discord_button.setIconSize(self.main_self.main_settings_button_size)
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Load svg script """
    def load_svg(self, svg_path, size):
        try: # Try create svg graphics
            renderer = QSvgRenderer(svg_path) # Render svg
            pixmap = QPixmap(width, height) # Create pixmap
            pixmap.fill(Qt.transparent) # Transparent
            painter = QPainter(pixmap) # Render graphic 
            renderer.render(painter) # Render graphic
            painter.end() # Render graphic
            scaled_pixmap = pixmap.scaled(QSize(width, height), Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scal pixmap
            return scaled_pixmap
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Set sound disabled and enabled """
    def set_sound_d_e(self, _type):
        try: # Try set config
            self.main_self.settings_config_file[_type] = not self.main_self.settings_config_file[_type] # Change config
            json.dump(self.main_self.settings_config_file, open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'), indent=4) # Save config
            self.main_self.settings_config_file = json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r')) # Reload settings config file
            button = None # Set deafoult
            if _type == '__sound_button__':
                button = self.main_self.settings_sound_button_button
            elif _type == '__sound_alert__':
                button = self.main_self.settings_sound_alert_button
            elif _type == '__sound_notification__':
                button = self.main_self.settings_sound_notification_button
            if button:
                button.setText(self.main_self.settings_translate_file[f'settings{_type[1:-1]}button'][self.main_self.settings_config_file['__language__']][self.main_self.settings_config_file[_type]]) # Change text of button
            self.main_self.notification_background_widget.setHidden(False) # Show notification widget
            self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][4]) # Set text
            self.main_self.controller_notification.open() # Open notification
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Set auto update """
    def set_auto_update(self):
        try: # Try set config
            self.main_self.settings_config_file['__auto_update__'] = not self.main_self.settings_config_file['__auto_update__'] # Change config
            json.dump(self.main_self.settings_config_file, open(self.main_self.main_path + '/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'),indent=4)  # Save config
            self.main_self.settings_config_file = json.load(open(self.main_self.main_path + '/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))  # Reload settings config file
            self.main_self.settings_update_option_autoupdate_button.setText(self.main_self.settings_translate_file['settings_update_option_autoupdate_button'][self.main_self.settings_config_file['__language__']][self.main_self.settings_config_file['__auto_update__']]) # Set translate
            self.main_self.notification_background_widget.setHidden(False)  # Show notification widget
            self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][4]) # Set text
            self.main_self.controller_notification.open() # Open notification
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Update, check updates """
    def check_updates(self):
        try: # Try check and setup update if is.
            self.main_self.settings_update_option_check_button.setText(self.main_self.settings_translate_file['settings_update_option_check_button'][1][self.main_self.settings_config_file['__language__']])
            self.settings_check_updates_thread = self.main_self.controller_update.get_releses() # Create thread get release
            self.settings_check_updates_thread.changelog_fetched.connect(self.check_updates_controller) # Connect func to setup Widget
            self.settings_check_updates_thread.finished.connect(self.setup_thread_clean) # Connect cleanup function
            self.settings_check_updates_thread.start() # Start Thread
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#______________________________________________________________________________________________________________________
    """ Check updates controller """
    def check_updates_controller(self, github_version):
        try:
            if self.main_self.changelog_file['name'] != github_version[0]['name']: # If not updated
                self.main_self.controller_update.set_data(github_version[0]) # Set date for update controller
                self.main_self.controller_alert.open() # Open alet
                self.main_self.alert_download_button.setHidden(False) # Show download button
                self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][1]) # Set message of alert
            else: # If updated
                self.main_self.notification_background_widget.setHidden(False) # Show notification
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][5]) # Set text for notification
                self.main_self.controller_notification.open() # Call funcation for open notification
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Setup thread clean """
    def setup_thread_clean(self):
        self.main_self.settings_update_option_check_button.setText(self.main_self.settings_translate_file['settings_update_option_check_button'][0][self.main_self.settings_config_file['__language__']])
        self.settings_check_updates_thread.deleteLater() # Delete thread get release
        self.settings_check_updates_thread = None # Set deafoult
#_______________________________________________________________________________________________________________________
    """ Update, set capacity """
    def set_capacity(self):
       try: # Try set config
            self.main_self.settings_config_file['__capacity__'] = self.main_self.settings_update_advanced_capacity_combobox.currentIndex() # Set new value
            json.dump(self.main_self.settings_config_file, open(self.main_self.main_path + '/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'), indent=4) # Save config
            self.main_self.settings_config_file = json.load(open(self.main_self.main_path + '/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))  # Reload settings config file
       except Exception:  # Except if problem with code
           self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
           self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
           self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Report, set auto report enabled """
    def set_auto_report(self):
        try: # Try ser config
            self.main_self.settings_config_file['__auto_report__'] = not self.main_self.settings_config_file['__auto_report__']  # Change config
            json.dump(self.main_self.settings_config_file, open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'w'), indent=4) # Save config
            self.main_self.settings_config_file = json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r')) # Reload settings config file
            self.main_self.settings_report_autoreport_button.setText(self.main_self.settings_translate_file['settings_report_autoreport_button'][self.main_self.settings_config_file['__language__']][self.main_self.settings_config_file['__auto_report__']])  # Set translate
            self.main_self.notification_background_widget.setHidden(False) # Show notification widget
            self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][4]) # Set text
            self.main_self.controller_notification.open() # Open notification
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################
""" Controller udapte """
class controller_update:
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try: # Try set deafoult
            self.main_self = main_self # Main self, main objects of application.
            self._data = None # Set deafoult
            self.auto_update_releases_thread = None # Set defoult
            self.auto_update() # Call auto update on startup of application
            self.update_time_sec = 5 # Set defoult
        except Exception:  # Except if problem with code.
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Get relaeses """
    class get_releses(QThread):
        changelog_fetched = pyqtSignal(list)
        """ Init, creating items, set base variables like paths, screen size, etc. """
        def __init__(self):
            super().__init__()
            self.start() # start function automatic.
        def run(self):
            try:
                release = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Windows/releases') # Get latest relaeses from github
                self.changelog_fetched.emit(json.loads(release.read().decode())) # Emir signal with json list
            except:
                self.changelog_fetched.emit([])
#_______________________________________________________________________________________________________________________
    """ Set data """
    def set_data(self, data):
        try: # Try set update date
            self._data = data # Set data
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Open changelog """
    def setup_changelog(self):
        try: # Try setup changelog
            """ Update background """
            self.main_self.update_background_widget.setGeometry(QRect(0,0,self.main_self.width(), self.main_self.height())) # Set geometry of background
#_______________________________________________________________________________________________________________________
            """ Setup changlog """
            self.main_self.update_changlog_scroll_widget = QWidget(self.main_self.update_changelog_scroll)
            self.main_self.update_changlog_scroll_layout = QVBoxLayout(self.main_self.update_changlog_scroll_widget)
            self.main_self.update_changlog_scroll_title_label = QLabel(self.main_self.update_changlog_scroll_widget)
            self.main_self.update_changlog_scroll_date_label = QLabel(self.main_self.update_changlog_scroll_widget)
            self.main_self.update_changlog_scroll_text_label = QLabel(self.main_self.update_changlog_scroll_widget)
#_______________________________________________________________________________________________________________________
            """ Set ObjectName """
            self.main_self.update_changlog_scroll_widget.setObjectName('update_changlog_scroll_widget')
            self.main_self.update_changlog_scroll_title_label.setObjectName('update_changlog_scroll_title_label')
            self.main_self.update_changlog_scroll_date_label.setObjectName('update_changlog_scroll_date_label')
            self.main_self.update_changlog_scroll_text_label.setObjectName('update_changlog_scroll_text_label')
#_______________________________________________________________________________________________________________________
            """ Set Layout """
            self.main_self.update_changlog_scroll_layout.addWidget(self.main_self.update_changlog_scroll_title_label)
            self.main_self.update_changlog_scroll_layout.addWidget(self.main_self.update_changlog_scroll_date_label)
            self.main_self.update_changlog_scroll_layout.addWidget(self.main_self.update_changlog_scroll_text_label)
            self.main_self.update_changlog_scroll_layout.setSpacing(0)
            self.main_self.update_changlog_scroll_layout.setContentsMargins(0,0,0,0)
            self.main_self.update_changlog_scroll_widget.setLayout(self.main_self.update_changlog_scroll_layout)
#_______________________________________________________________________________________________________________________
            """ Set Label """
            self.main_self.update_changlog_scroll_title_label.setAlignment(Qt.AlignCenter)
            self.main_self.update_changlog_scroll_date_label.setAlignment(Qt.AlignCenter)
            self.main_self.update_changlog_scroll_text_label.setWordWrap(True)
#_______________________________________________________________________________________________________________________
            """ Set Size """
            self.main_self.update_changlog_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.main_self.update_changlog_scroll_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.main_self.update_changlog_scroll_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.main_self.update_changlog_scroll_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
            """ Set Text """
            self.main_self.update_changlog_scroll_title_label.setText(self._data['name'])
            self.main_self.update_changlog_scroll_date_label.setText(str(self._data['published_at']).replace('T', ' ').replace('Z', ''))
            self.main_self.update_changlog_scroll_text_label.setText(self._data['body'])
#_______________________________________________________________________________________________________________________
            """ Set Scroll """
            self.main_self.update_changelog_scroll.setWidget(self.main_self.update_changlog_scroll_widget)
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Update """
    def update(self):
        try: # Try setup download.
            self.main_self.controller_download = controller_download(self.main_self, self._data['zipball_url']) # Create download thread, controller
            self.main_self.controller_download.progress_index.connect(self.update_progress) # Connect function of progress
            self.main_self.controller_download.progress_bar_value.connect(self.update_progress_bar) # Connect function of progerss bar
            self.main_self.controller_download.start() # Start udapte function
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Update progress """
    def update_progress(self, value):
        try: # Try do steps of update
            if value == 0: # Setup, creta backup
                self.main_self.main_start_button.setDisabled(True) # Set open button disabled
                self.main_self.settings_update_version_changelog_button.setDisabled(True) # Set open changelog button disabled
                self.main_self.settings_update_option_check_button.setDisabled(True) # Set check update button disabled
                self.main_self.main_start_button.setText(self.main_self.settings_translate_file['main_start_button'][1][self.main_self.settings_config_file['__language__']]) # Set text 
                self.main_self.controller_main.changlog_to_main() # Open Main page
                self.main_self.main_update_label.setHidden(False) # Show message label
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][0][self.main_self.settings_config_file['__language__']]) # Set message
                self.main_self.main_update_progress.setValue(0) # Reset progress bar
                self.main_self.main_update_progress.setHidden(False) # Show progress bar
            elif value == 1: # Download
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][1][self.main_self.settings_config_file['__language__']]) # Set message
            elif value == 2: # Unzip
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][2][self.main_self.settings_config_file['__language__']]) # Set message
            elif value == 3: # Update compatibility
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][3][self.main_self.settings_config_file['__language__']]) # Set message
            elif value == 4: # Install
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][4][self.main_self.settings_config_file['__language__']]) # Set message
            elif value == 5: # Finalizng, delet backup folder
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][5][self.main_self.settings_config_file['__language__']]) # Set message
            elif value == 6: # Final setup, restart
                self.main_self.main_update_progress.setValue(0)  # Reset progress bar
                self.main_self.main_update_progress.setHidden(True)  # Set hidden
                self.main_self.main_start_button.setDisabled(False)  # Set button enabled
                self.main_self.main_start_button.setText(self.main_self.settings_translate_file['main_start_button'][0][self.main_self.settings_config_file['__language__']])  # Set button
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][6][self.main_self.settings_config_file['__language__']])  # Set message
                self.main_self.controller_download.quit() # Quit 
                self.main_self.controller_download.wait() # Wait
                self.main_self.controller_download.deleteLater() # Delete
                self.main_self.controller_download = None # Set defoult 
                self.restart() # Call restart fucntion.
            elif value == 10: # Error 
                self.main_self.main_update_progress.setValue(0) # Reset progress bar
                self.main_self.main_update_progress.setHidden(True)  # Set hidden
                self.main_self.main_start_button.setText(self.main_self.settings_translate_file['main_start_button'][2][self.main_self.settings_config_file['__language__']])  # Set button
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][7][self.main_self.settings_config_file['__language__']])  # Set message
                self.main_self.controller_download.quit() # Quit 
                self.main_self.controller_download.wait() # Wait
                self.main_self.controller_download.deleteLater() # Delete update controller
                self.main_self.controller_download = None # Set defoult
            elif value == 11: # No connection, waiting for reconnect.
                self.main_self.main_update_label.setText(self.main_self.settings_translate_file['main_update_label'][8][self.main_self.settings_config_file['__language__']])  # Set message
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Update progeress bar """
    def update_progress_bar(self, value):
        try: # Try set progress bar value
            self.main_self.main_update_progress.setValue(value) # Set new value
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Restart """
    def restart(self):
        try:
            subprocess.Popen(['/bin/bash', self.main_self.main_path+'/Launcher.sh'])  # Open app.
            sys.exit(0) # Exit application
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Auto update """
    def auto_update(self):
        try: # Try check if auto update enabled
            if self.main_self.settings_config_file['__auto_update__']: # Check if auto update is enable or disabled
                self.auto_update_releases_thread = self.get_releses() # Get latest version
                self.auto_update_releases_thread.changelog_fetched.connect(self.set_data) # Connect 
                self.auto_update_releases_thread.finished.connect(self.auto_update_check) # Clean and call update function
                self.auto_update_releases_thread.start() # Start thread
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Auto update check """
    def auto_update_check(self):
        if self.main_self.changelog_file['name'] != self._data[0]['name']:
            self._data = self._data[0] # Set data of update 
            self.update() # Call update function
        self.auto_update_releases_thread.deleteLater() # Delete auto update relese check thread
        self.auto_update_releases_thread = None # Ser defoult
#_______________________________________________________________________________________________________________________
    """ Check compatibility """
    def check_compatibility(self):
        try: # Try check comptibility
            compatibility = True
            for file, value in self.main_self.settings_app_file_list_file.items():
                if value == 'config':
                    continue
                elif value != self.calculate_sha256(self.main_self.main_path+file):
                    print(file, self.calculate_sha256(self.main_self.main_path+file))
                    compatibility = False # Set not compatibility in files
            if compatibility:
                self.main_self.controller_report.write_log(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][7])
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][7])
                self.main_self.controller_notification.open()
            else:
                self.main_self.controller_report.write_log(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][2])
                self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][2])
                self.main_self.controller_alert.open()
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()

#_______________________________________________________________________________________________________________________
        """ Check sum control """
    def calculate_sha256(self, file):
        try:  # Try check sum
            sha256 = hashlib.sha256()  # Get sha
            f = open(file, "rb")  # Open file
            while chunk := f.read(4096):
                sha256.update(chunk)
            return sha256.hexdigest()  # return check sum
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################
""" Controller download """
class controller_download(QThread):
    """ Signals """
    progress_index = pyqtSignal(int) # Progress, return actuall stage of update
    progress_bar_value = pyqtSignal(int) # Progress, return value to progress bar
#_______________________________________________________________________________________________________________________
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self, url):
        super().__init__()
        self.url = url # URL adress
        self.main_self = main_self # Main self
        self.update_folder = None # Name of update folder
        self.update_json_file_list = None # Update file list
        self.zip_buffer = io.BytesIO() # Zip
#_______________________________________________________________________________________________________________________
    """ Run """
    def run(self):
        try:
            self.backup() # Startup, show main page,
            time.sleep(0.2)
            self.download() # Download update
            time.sleep(0.2)
            self.un_zip() # Unzip downloded zip file
            time.sleep(0.2)
            self.update_compatibility() # Update compatibility
            time.sleep(0.2)
            self.install() # Install update
            time.sleep(0.2)
            self.delete_backup() # Delte backup 
            time.sleep(0.2)
            self.restart() # Restart application
        except:
            pass
#_______________________________________________________________________________________________________________________
    """ Backup """
    def backup(self):
        try:
            self.progress_index.emit(0) # Emit signal 0
            self.backup_folder = os.path.join(self.main_self.main_path, '.backup') # Set backup folder
            if not os.path.exists(self.backup_folder): # Check if backup folder exists
                os.mkdir(self.backup_folder) # Create backup folder if does not exists
                for item in os.listdir(self.main_self.main_path): # Copy files
                    if item == '.backup':
                        continue  # Pass folder .backup
                    source_item = os.path.join(self.main_self.main_path, item) # Set source item
                    backup_item = os.path.join(self.backup_folder, item) # Set backup item
                    if os.path.isdir(source_item): # Check if source item is folder
                        shutil.copytree(source_item, backup_item) # Copy folder
                    else:
                        shutil.copy2(source_item, backup_item) # Copy file
        except:
            self.progress_index.emit(10) # Emit signal 10
            if os.path.exists(self.backup_folder): # Check if backup folder exists
                shutil.rmtree(self.backup_folder) # Delte backup folder
            raise
#_______________________________________________________________________________________________________________________
    """ Download """
    def download(self):
        try: # Try download update
            self.progress_index.emit(1) # Emit signal 1
            chunk_size = 8192 # Chunk siize
            downloaded = 0 # Set deafoult
            total_length = 533*1024*1024 # Set defoult
            headers = {} # Set headers
            while True: # Loop
                try:
                    if downloaded > 0:
                        headers['Range'] = f'bytes={downloaded}-' # Set headers, downloaded
                    response = requests.get(self.url, stream=True, timeout=10, headers=headers) # Connect 
                    response.raise_for_status() # Reise error
                    self.progress_index.emit(1) # Emit signal 1 
                    chunk_generator = response.iter_content(chunk_size=chunk_size) # Set chunk generator
                    for chunk in chunk_generator: # Create chunk 
                        if not chunk: # Check if chunk
                            continue
                        self.zip_buffer.write(chunk) # Save file in zip 
                        downloaded += len(chunk) # Set download size
                        self.progress_index.emit(1) # Emit signal 1
                        self.progress_bar_value.emit(int((downloaded / total_length) * 100)) # Set progressbar value
                        time.sleep(len(chunk) / (self.set_speed(self.main_self.settings_config_file['__capacity__']) * 1024)) # Set download speed
                    break
                except (requests.RequestException, ConnectionError, TimeoutError): # Except for errors with connection 
                    self.progress_index.emit(11) # Emit signal 11
                    time.sleep(3) # Time sleepset_data
        except Exception:
            print(f"{Exception} \n {traceback.format_exc()}", headers)
            self.progress_index.emit(10) # Emit signal 10
            if os.path.exists(self.backup_folder): # Check if backup folder exists
                shutil.rmtree(self.backup_folder) # Delte backup folder
            if self.zip_buffer: # Check if zip exists
                self.zip_buffer.seek(0) # Delete zip file
                self.zip_buffer.truncate(0) # Delete zip file
            raise
#_______________________________________________________________________________________________________________________
    """ Unzip """
    def un_zip(self):
        try: # Try unzip file
            self.progress_index.emit(2) # Emit signal 2
            with zipfile.ZipFile(self.zip_buffer, 'r') as zip_ref: # Open zip file
                self.update_folder = f'/{zip_ref.namelist()[0]}' # Get name of update folder
                list_files = zip_ref.namelist() # Get list of files
                total_files = len(list_files) # Get number of files
                extracted_files = 0 # Number of extracted files
                for file in list_files:
                    zip_ref.extract(file, self.main_self.main_path) # Extract file to folder
                    extracted_files += 1 # Add extracted file number
                    self.progress_bar_value.emit(int((extracted_files/total_files)*100)) # Update progress bar
                self.progress_bar_value.emit(100) # Debug, update progress bar to 100
                self.zip_buffer.seek(0) # Delte zip file
                self.zip_buffer.truncate(0) # Delte zip file
        except:
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder): # Check if backup folder exists
                shutil.rmtree(self.backup_folder) # Delte backup folder
            if self.zip_buffer: # Check if zip exists
                self.zip_buffer.seek(0) # Delete zip file
                self.zip_buffer.truncate(0) # Delte zip file
            if os.path.exists(self.main_self.main_path+self.update_folder): # Check if update folder exists
                shutil.rmtree(self.main_self.main_path+self.update_folder) # Delete update folder
            raise
#_______________________________________________________________________________________________________________________
    """ Update compatibility """
    def update_compatibility(self):
        try: # Try check compatibility
            self.progress_index.emit(3) # Emit signal 3
            self.update_json_file_list = json.load(open(self.main_self.main_path+self.update_folder+'TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json', 'r')) # Set update file list
            total_files = len(self.update_json_file_list) # Get number of files
            checked_file = 0 # Number of checked files
            for file, check_sum in self.update_json_file_list.items(): # Check compatibility
                if os.path.exists(self.main_self.main_path+self.update_folder[:-1]+file):
                    if check_sum != 'config':
                        if check_sum != self.main_self.controller_update.calculate_sha256(self.main_self.main_path+self.update_folder[:-1]+file):
                            raise
                        checked_file += 1 # Add checked file
                        self.progress_bar_value.emit(int((checked_file/total_files)*100)) # Update progress bar
            self.progress_bar_value.emit(100) # Debug, update progress bar to 100
        except:
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder): # Check if backup folder exists
                shutil.rmtree(self.backup_folder) # Delte backup folder
            if os.path.exists(self.main_self.main_path+self.update_folder): # Check if update folder exists
                shutil.rmtree(self.main_self.main_path+self.update_folder) # Delete update folder
            raise
#_______________________________________________________________________________________________________________________
    """ Install """
    def install(self):
        try: # Try install update
            self.progress_index.emit(4) # Emit signal 4
            total_files = len(self.update_json_file_list) # Get number of files
            installed_files = 0 # Number of installed files
            for path, check_sum in self.update_json_file_list.items():
                installed_files += 1 # Add plus one to installed files
                self.progress_bar_value.emit(int((installed_files / total_files) * 100))  # Update progress bar
                if os.path.exists(self.main_self.main_path+path): # Check if file from update exists in main folder
                    if self.main_self.settings_app_file_list_file[path] == check_sum: # Check if file from update was changed, if no continue
                        continue
                shutil.copy(self.main_self.main_path+self.update_folder[:-1]+path, self.main_self.main_path+path) # Copy, add file, if file form update was changed
            for path in self.main_self.settings_app_file_list_file.keys():
                if path not in self.update_json_file_list.keys(): # Check if old file is in update
                    os.remove(self.main_self.main_path+path)  # Remove old file, if no in update
            shutil.copy(self.main_self.main_path+self.update_folder[:-1]+'/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json', self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json') # Change settings app list to this from update
            self.progress_bar_value.emit(100) # Debug, update progress bar to 100
            self.main_self.settings_app_file_list_file = json.load(open(self.main_self.main_path + '/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json','r'))  # Reload settings app file list
            shutil.rmtree(self.main_self.main_path + self.update_folder[:-1]) # Remove update folder
            self.main_self.controller_update.check_compatibility() # Call funcation that check compatibility of all files
        except:
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder): # Check if backup folder exists
                self.restore_backup() # Call restore func
            if os.path.exists(self.main_self.main_path+self.update_folder): # Check if update folder exists
                shutil.rmtree(self.main_self.main_path+self.update_folder) # Delete update folder
            raise
#______________________________________________________________________________________________________________________
    """ Delete backup """
    def delete_backup(self):
        self.progress_index.emit(5)
        if os.path.exists(self.backup_folder): # Check if backup folder exists
            shutil.rmtree(self.backup_folder) # Delete backup folder
#______________________________________________________________________________________________________________________
    def restart(self):
        self.progress_index.emit(6)
#______________________________________________________________________________________________________________________
    """ Restore backup """
    def restore_backup(self):
        for item in os.listdir(self.backup_folder):
            source_item = os.path.join(self.main_self.main_path, item)
            backup_item = os.path.join(self.backup_folder, item)
            if os.path.exists(source_item): # Check if source item exists
                if os.path.isdir(source_item): # Check if source item is folder
                    shutil.rmtree(source_item) # Delete source item
                else:
                    os.remove(source_item) # Delete source item
            if os.path.isdir(backup_item): # Check if backup item is folder
                shutil.copytree(backup_item, source_item) # Restore file
            else:
                shutil.copy2(backup_item, source_item) # Restore file
        if os.path.exists(self.backup_folder): # Check if backup folder exists
            shutil.rmtree(self.backup_folder) # Delete backup folder
#_______________________________________________________________________________________________________________________
    """ Set capacity """
    def set_speed(self, index):
        try: # Try set download speed
            capacity = 0 # Set deafoult
            if index == 0:
                capacity = 500
            elif index == 1:
                capacity = 1000
            elif index == 2:
                capacity = 2000
            elif index== 3:
                capacity = 5000
            elif index == 4:
                capacity = float('inf')
            return capacity # Return capacity
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
""" Controller report """
class controller_report:
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try: # Try get sql login data
            self.main_self = main_self # Main self
            self.host = 'localhost'
            self.user = 'launcherclient'
            self.password = 'qwerty'
            self.database = 'TickerK8'
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Write log and send """
    def write_log(self, message):
        try: # Try write a log
            log_file = open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/log.txt', 'a') # Open log file
            log_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error: {message} \n\n") # Write error
            if self.main_self.settings_config_file['__auto_report__']: # Check if auto report to database
                try: # Try send report to database
                    connect = mysql.connector.connect(  # Set Connect
                        host=self.host,  # Set host
                        user=self.user,  # Set user
                        password=self.password,  # Set password
                        database=self.database  # Select database
                    )
                    cursor = connect.cursor()  # Cusrosr
                    cursor.execute(f'INSERT INTO report (date, message) VALUES ("{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}", "{message}");')  # Do query to database
                    connect.commit()  # Save
                    connect.close()  # Close connection
                except: # Execpet if something wrong with sending to database
                    self.main_self.ping.single_ping()
        except Exception:  # Except if problem with code
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Send report """
    def send_report(self):
        try: # Try send report
            message = self.main_self.report_textfield_textarea.toPlainText() # Get message
            try:
                connect = mysql.connector.connect( # Set Connect
                    host=self.host, # Set host
                    user=self.user, # Set user
                    password=self.password, # Set password
                    database=self.database # Select database
                    )
                cursor = connect.cursor() # Cusrosr
                cursor.execute(f'INSERT INTO report (date, message) VALUES ("{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}", "{message}");') # Do query to database
                connect.commit() # Save
                connect.close() # Close connection
                self.clear()  # Call func, clear text field
                self.main_self.notification_background_widget.setHidden(False)  # Show notification
                self.main_self.notification_text_label.setText(self.main_self.settings_translate_file['notification_text_label'][self.main_self.settings_config_file['__language__']][6])  # Set notification message
                self.main_self.controller_notification.open()  # Open notification
            except: # Execpet if something wrong with sending to database
                self.main_self.ping.single_ping()
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Clear report textarea """
    def clear(self):
        try: # Try clear report.
            self.main_self.report_textfield_textarea.setText('') # Clear text field
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################
""" Controller notification """
class controller_notification:
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try: # Setup deafolut
            self.main_self = main_self  # Main self, main objects of application.
            self._opened = False # Variable for opened or hidden
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Open """
    def open(self):
        try: # Try open notification
            if not self._opened: # Check if not opened
                self.main_self.notification_background_widget.setHidden(False)
                self.main_self.notification_background_widget.setFixedSize(QSize(self.main_self.width(), self.main_self.height()//5)) # Set background widget size
                self.main_self.notification_background_label.setGeometry(QRect(0, 0, self.main_self.notification_background_widget.width(), self.main_self.notification_background_widget.height())) # Set label blur size
                self.main_self.notification_anim.stop() # Stop anim, debug
                self.main_self.notification_anim.setDuration(400) # Set duration
                self.main_self.notification_anim.setStartValue(QPoint(0, self.main_self.height())) # Set start value
                self.main_self.notification_anim.setEndValue(QPoint(0, int(self.main_self.height()//1.25))) # Set end value
                try: # Check if some function is connected
                    self.main_self.notification_anim.finished.disconnect() # Disconnect connected funcations, debug
                except: # If no pass
                    pass
                self.main_self.notification_anim.finished.connect(self.auto_close) # Connect auto_close funcation when anim finished
                self.main_self.notification_anim.start() # Start aniamtion
                self._opened = not self._opened # Change open
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Close """
    def close(self):
        try: # Try clsoe nootification.
            if self._opened: # Debug
                self.main_self.notification_background_widget.setFixedSize(QSize(self.main_self.width(), self.main_self.height() // 5)) # Set background widget size
                self.main_self.notification_anim.stop()  # Stop anim, debug
                self.main_self.notification_anim.setDuration(400) # Set duration
                self.main_self.notification_anim.setStartValue(QPoint(0, self.main_self.notification_background_widget.y())) # Set start value
                self.main_self.notification_anim.setEndValue(QPoint(0, int(self.main_self.height()))) # Set end value
                self.main_self.notification_anim.finished.disconnect() # Disconnect connected funcations, debug
                self.main_self.notification_anim.finished.connect(self.hide)  # Connect auto_close funcation when anim finished
                self.main_self.notification_anim.start() # Start aniamtion
                self._opened = not self._opened # Change open
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Auto close """
    def auto_close(self):
        try: # Setuop auto close
            timer = QTimer(self.main_self) # Create timer
            timer.setSingleShot(True) # Set single shot
            timer.timeout.connect(lambda: self.close()) # Connect function, when timeout
            timer.start(2500) # Start timer
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Hide """
    def hide(self):
        try: # Try hide notification
            self.main_self.notification_background_widget.setHidden(True) # Hide notification background widget
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################
""" Controller alert """
class controller_alert:
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try: # Setup deafolut
            self.main_self = main_self # Main self, main objects of application.
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Open """
    def open(self):
        try: # Try open alert
            self.main_self.alert_background_widget.setGeometry(QRect(0,0,self.main_self.width(), self.main_self.height())) # Set geometry for alert background
            self.main_self.alert_background_widget.setHidden(False) # Show alert
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Close """
    def close(self):
        try: # Try close alet
            self.main_self.alert_background_widget.setHidden(True) # Hide alert
        except Exception:  # Except if problem with code
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################
""" Controller ping """
class controller_ping(QThread):
    signal = pyqtSignal(bool) # Signal of connect.
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        try:
            super().__init__() # Call functions.
            self.is_connect = None # Is connect variable.
            self.main_self = main_self # Main self.
        except Exception:
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
#_______________________________________________________________________________________________________________________
    """ Run ping loop """
    def run(self): # Run function.
        while True: # Loop
            self.single_ping()
            time.sleep(5) # Wait 5s.
#_______________________________________________________________________________________________________________________
    """ Single ping """
    def single_ping(self):
        try:
            try: # Try
                socket.setdefaulttimeout(3) # Set socket time out
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53)) # Send ping
                if self.is_connect == False or self.is_connect == None: # Check if already has no connection.
                    self.is_connect = True # Set True.
                    self.signal.emit(self.is_connect) # Emit signal.
            except socket.error: # Exception.
                if self.is_connect == True or self.is_connect == None: # Check if already has connection.
                    self.is_connect = False # Set False .
                    self.signal.emit(self.is_connect) # Emit signal.
        except Exception:
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()
########################################################################################################################