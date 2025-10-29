""" Import packages """
import pathlib
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox, 
    QGridLayout,
    QVBoxLayout 
)
from PyQt5.QtCore import (
    Qt
)
""" Import settings modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Settings_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.opened_sub_widget = None
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        """ Create objects """
        self.main_layout = QGridLayout(self)
        self.navi_scroll = QScrollArea(self)
        self.navi_widget = QWidget(self.navi_scroll)
        self.navi_layout = QVBoxLayout(self.navi_widget)
        self.navi_user_button = QPushButton(self.navi_widget)
        self.navi_style_button = QPushButton(self.navi_widget)
        self.navi_sound_button = QPushButton(self.navi_widget)
        self.navi_update_button = QPushButton(self.navi_widget)
        self.navi_language_button = QPushButton(self.navi_widget)
        self.navi_report_button = QPushButton(self.navi_widget)
        self.navi_exit_button  = QPushButton(self)
        self.panel_right_scroll = QScrollArea(self)
        self.panel_right_widget = QWidget(self.panel_right_scroll)
        self.panel_right_layout = QVBoxLayout(self.panel_right_widget)
        self.user_widget = QWidget(self.panel_right_widget)
        self.user_layout = QGridLayout(self.user_widget)
        self.user_title_label = QLabel(self.user_widget)
        self.user_image_button = QPushButton(self.user_widget)
        self.user_info_subtitle_label = QLabel(self.user_widget)
        self.user_name_name_label = QLabel(self.user_widget)
        self.user_name_content_label = QLabel(self.user_widget)
        self.user_email_name_label = QLabel(self.user_widget)
        self.user_email_content_label = QLabel(self.user_widget)
        self.user_create_date_name_label = QLabel(self.user_widget)
        self.user_create_date_content_label = QLabel(self.user_widget)
        self.style_widget = QWidget(self.panel_right_widget)
        self.style_layout = QGridLayout(self.style_widget)
        self.style_title_label = QLabel(self.style_widget)
        self.style_theme_subtitle_label = QLabel(self.style_widget)
        self.style_theme_d_n_name_label = QLabel(self.style_widget)
        self.style_theme_d_n_content_button = QPushButton(self.style_widget)
        self.style_theme_themes_name_label = QLabel(self.style_widget)
        self.style_theme_themes_content_combobox = QComboBox(self.style_widget)
        self.sound_widget = QWidget(self.panel_right_widget)
        self.sound_layout = QGridLayout(self.sound_widget)
        self.sound_title_label = QLabel(self.sound_widget)
        self.sound_button_name_label = QLabel(self.sound_widget)
        self.sound_button_content_button = QPushButton(self.sound_widget)
        self.sound_alert_name_label = QLabel(self.sound_widget)
        self.sound_alert_content_button = QPushButton(self.sound_widget)
        self.sound_notification_name_label = QLabel(self.sound_widget)
        self.sound_notification_content_button = QPushButton(self.sound_widget)
        self.update_widget = QWidget(self.panel_right_widget)
        self.update_layout = QGridLayout(self.update_widget)
        self.update_title_label = QLabel(self.update_widget)
        self.update_version_subtitle_label = QLabel(self.update_widget)
        self.update_version_description_name_label = QLabel(self.update_widget)
        self.update_version_description_content_label = QLabel(self.update_widget)
        self.update_version_changelog_name_label = QLabel(self.update_widget)
        self.update_version_changelog_content_button = QPushButton(self.update_widget)
        self.update_options_subtitle_label = QLabel(self.update_widget)
        self.update_options_auto_update_name_label = QLabel(self.update_widget)
        self.update_options_auto_update_content_button = QPushButton(self.update_widget)
        self.update_options_check_update_name_label = QLabel(self.update_widget)
        self.update_options_check_update_content_button = QPushButton(self.update_widget)
        self.update_advanced_subtitle_label = QLabel(self.update_widget)
        self.update_advanced_capacity_name_label = QLabel(self.update_widget)
        self.update_advanced_capacity_content_combobox = QComboBox(self.update_widget)
        self.update_advanced_file_verification_name_label = QLabel(self.update_widget)
        self.update_advanced_file_verification_content_button = QPushButton(self.update_widget)
        self.language_widget = QWidget(self.panel_right_widget)
        self.language_layout = QGridLayout(self.language_widget)
        self.language_title_label = QLabel(self.language_widget)
        self.language_langauge_name_label = QLabel(self.language_widget)
        self.language_langauge_content_combobox = QComboBox(self.language_widget)
        self.report_widget = QWidget(self.panel_right_widget)
        self.report_layout = QGridLayout(self.report_widget)
        self.report_title_label = QLabel(self.report_widget)
        self.report_auto_report_name_label = QLabel(self.report_widget)
        self.report_auto_report_content_button = QPushButton(self.report_widget)
        self.report_send_report_name_label = QLabel(self.report_widget)
        self.report_send_report_content_button = QPushButton(self.report_widget)
        """ Call functions """
        settings_ui(self)
        settings_reload_style(self)
        self.settings_reload_style = lambda: settings_reload_style(self)
        settings_retranslate(self)
        self.settings_retranslate = lambda: settings_retranslate(self)
        """ Connect functions """
        self.navi_user_button.clicked.connect(lambda: open_sub_widget(self, self.user_widget))
        self.navi_style_button.clicked.connect(lambda: open_sub_widget(self, self.style_widget))
        self.navi_sound_button.clicked.connect(lambda: open_sub_widget(self, self.sound_widget))
        self.navi_update_button.clicked.connect(lambda: open_sub_widget(self, self.update_widget))
        self.navi_language_button.clicked.connect(lambda: open_sub_widget(self, self.language_widget))
        self.navi_report_button.clicked.connect(lambda: open_sub_widget(self, self.report_widget))
        self.language_langauge_content_combobox.currentIndexChanged.connect(lambda: change_language(self))
        self.sound_button_content_button.clicked.connect(lambda: set_sound_d_e(self, '_button_'))
        self.sound_alert_content_button.clicked.connect(lambda: set_sound_d_e(self, '_alert_'))
        self.sound_notification_content_button.clicked.connect(lambda: set_sound_d_e(self, '_notification_'))
#______________________________________________________________________________________________________________________
