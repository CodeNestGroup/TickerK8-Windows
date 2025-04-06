""" Import """
""" Import system and operating system packages """
import sys # Sys package, access to system func.
import pathlib # Pathlib package, for get path to application
#_______________________________________________________________________________________________________________________
""" Import json control """
import json # Json package for control json files.
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Widgets """
from PyQt5.QtWidgets import (QApplication, # Application, define application
                             QWidget, # Widget, simple widget.
                             QVBoxLayout, # Vertical Layout.
                             QGridLayout, # Grid Layout.
                             QScrollArea, # Scroll widget, widget you can scroll.
                             QPushButton, # Button, simple button.
                             QLabel, # Label, simple label.
                             QComboBox, # Dropdown list.
                             QTextEdit, # Text Edit, field when you can type strings.
                             QGraphicsBlurEffect, # Blur Graphics effect.
                             QProgressBar) # Progrees bar.
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QGuiApplication, # Gui application, get primary screen.
                         QFontDatabase, # Font database for add new font to app.
                         QFont) # Font for add new font to app.
#_______________________________________________________________________________________________________________________
""" Import app sub files """
from _01_main_setObjectName import set_ObjectName # Func to set objects names.
from _02_main_setProperty import set_Property # Func to set class for css.
from _03_main_setLayout import set_Layout # Func to set up layouts.
from _04_main_setWidget import set_Widget # Func to set widgets.
from _05_main_setScrollArea import set_ScrollArea # Func to set scroll.
from _06_main_setLabel import set_Label # Func to set label.
from _07_main_setComboBox import set_ComboBox # Func to set and add items to list.
from _08_main_setConnect import set_Connect # Func to connect funcs from _13_main_Scripts to buttons.
from _09_main_setPushButton import set_Disabled # Func to disabled buttons.
from _10_main_setSize import set_Size # Func to set size.
from _11_main_Scripts import * # Import all scripts to manage main app etc.
from _12_main_customWidgets import * # Import all cutom widgets.
########################################################################################################################
""" Main window, widget """
class Main_window(QWidget): # Create main window, widget.
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self):
        super().__init__() # Call class.
        self.setWindowTitle('TickerK8 Launcher') # Set Window title.
        self.screen_size = QGuiApplication.primaryScreen().size() # Get screen size.
        self.main_settings_button_size = QSize(int(self.width() // 6), int(self.height() // 6)) # Set size for button icons.
        self.main_path = str(pathlib.Path(__file__).resolve().parents[3]) # Set main path, path to TickerK8 folder.
#_______________________________________________________________________________________________________________________
        """ Load json files, configs"""
        self.settings_config_file = json.load(open(self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r')) # Load settings config file, static.
        self.settings_translate_file = json.load(open(self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_01_settings_translate.json', 'r')) # Load settings translate file, static.
        self.settings_theme_file = json.load(open(self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_02_settings_theme.json', 'r')) # Load settings theme file, static.
        self.settings_icon_file = json.load(open(self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_03_settings_icon.json', 'r')) # Load settings icon file, static.
        self.settings_app_file_list_file = json.load(open(self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json', 'r')) # Load settings app file list file, static.
        self.changelog_file = json.load(open(self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/changlog.json', 'r')) # Load changelog file
#_______________________________________________________________________________________________________________________
        """ Self items """
        self.layout = QVBoxLayout(self) # Main vertical layout, for responsive.
#_______________________________________________________________________________________________________________________
        """ Main widget """
        self.main_widget = QWidget(self) # Main widget
        self.main_widget_layout = QGridLayout(self.main_widget) # Main widget grid layout.
#_______________________________________________________________________________________________________________________
        """ Main changelog """
        self.main_changelog_error_widget = main_changelog_error_widget(self)
        self.main_changelog_scroll = QScrollArea(self.main_widget) # Main changelog scroll.
        # Widget adding by script
#_______________________________________________________________________________________________________________________
        """ Main logo """
        self.main_logo_layout = QGridLayout(self.main_widget) # Main logo widget grid layout.
        self.main_logo_c_n_g_label = QLabel(self.main_widget) # Main logo company.
        self.main_logo_ticker_label = QLabel(self.main_widget) # Main logo app.
#_______________________________________________________________________________________________________________________
        """ Main settings"""
        self.main_settings_layout = QGridLayout(self.main_widget) # Main settings widget grid layout.
        self.main_settings_open_button = ShadowButton(self, self.main_widget) # Main settings open button, for open settings widget.
        self.main_settings_social_media_instagram_button = ShadowButton(self, self.main_widget) # Main settings open instagram.
        self.main_settings_social_media_github_button = ShadowButton(self, self.main_widget) # Main settings open gitHub.
        self.main_settings_social_media_discord_button = ShadowButton(self, self.main_widget) # Main settings open discord.
#_______________________________________________________________________________________________________________________
        """ Main update """
        self.main_update_layout = QGridLayout(self.main_widget) # Main update widget grid layout.
        self.main_update_progress = QProgressBar(self.main_widget) # Main update progressbar.
        self.main_update_label = QLabel(self.main_widget) # Main update label, for show info.
#_______________________________________________________________________________________________________________________
        """ Main start button"""
        self.main_start_button = ShadowButton(self, self.main_widget) # Main start button.
#_______________________________________________________________________________________________________________________
        """ Settings widget"""
        self.settings_widget = QWidget(self) # Settings widget
        self.settings_widget_layout = QGridLayout(self.settings_widget) # Settings widget grid layout.
#_______________________________________________________________________________________________________________________
        """ Settings exit button """
        self.settings_exit_button = QPushButton_sound(self, self.settings_widget) # Settings exit button, for exit from settings to main.
#_______________________________________________________________________________________________________________________
        """ Settings menu scroll """
        self.settings_menu_scroll = QScrollArea(self.settings_widget) # Settings menu scroll.
        self.settings_menu_scroll_widget = QWidget(self.settings_menu_scroll) # Settings menu scroll widget.
        self.settings_menu_scroll_widget_layout = QVBoxLayout(self.settings_menu_scroll_widget) # Settings menu scroll widget vertical layout.
        self.settings_menu_theme_button = QPushButton_sound(self, self.settings_menu_scroll_widget) # Settings menu theme button, for open sub widget with theme.
        self.settings_menu_sound_button = QPushButton_sound(self, self.settings_menu_scroll_widget) # Settings menu sound button, for open sub widget with sound.
        self.settings_menu_update_button = QPushButton_sound(self, self.settings_menu_scroll_widget) # Settings menu update button, for open sub widget with update.
        self.settings_mneu_language_button = QPushButton_sound(self, self.settings_menu_scroll_widget) # Settings menu language button, for open sub widget with language.
        self.settings_menu_report_button = QPushButton_sound(self, self.settings_menu_scroll_widget) # Settings menu report button, for open sub widget with report.
#_______________________________________________________________________________________________________________________
        """ Settings sub scroll """
        self.settings_sub_scroll = QScrollArea(self.settings_widget) # Settings sub scroll.
        self.settings_sub_scroll_widget = QWidget(self.settings_sub_scroll) # Settings sub scroll widget.
        self.settings_sub_scroll_widget_layout = QVBoxLayout(self.settings_sub_scroll_widget) # Settings sub scroll widget vertical layout.
#_______________________________________________________________________________________________________________________
        """ Settings sub theme widget """
        self.settings_theme_widget = QWidget(self.settings_sub_scroll_widget) # Settings sub theme widget.
        self.settings_theme_widget_layout = QGridLayout(self.settings_theme_widget) # Settings sub theme widget grid layout.
        self.settings_theme_title_label = QLabel(self.settings_theme_widget) # Settings theme title.
        self.settings_theme_d_n_label = QLabel(self.settings_theme_widget) # Settings theme day, night label (name).
        self.settings_theme_d_n_button = QPushButton_sound(self, self.settings_theme_widget) # Settings theme day, night button (set mode).
        self.settings_theme_list_label = QLabel(self.settings_theme_widget) # Settings theme list label (name).
        self.settings_theme_list_combobox = QComboBox(self.settings_theme_widget) # Settings theme list combobox (list od themes).
#_______________________________________________________________________________________________________________________
        """ Settings sub sound widget"""
        self.settings_sound_widget = QWidget(self.settings_sub_scroll_widget) # Settings sub sound widget.
        self.settings_sound_widget_layout = QGridLayout(self.settings_sound_widget) # Settings sub sound widget grid layout.
        self.settings_sound_title_label = QLabel(self.settings_sound_widget) # Settings sound title.
        self.settings_sound_button_label = QLabel(self.settings_sound_widget) # Settings sound button label (name).
        self.settings_sound_button_button = QPushButton_sound(self, self.settings_sound_widget) # Settings sound button, button (set enabled or disabled).
        self.settings_sound_alert_label = QLabel(self.settings_sound_widget) # Settings sound alert label (nsame).
        self.settings_sound_alert_button = QPushButton_sound(self, self.settings_sound_widget) # Settings sound alert button (set enabled or disabled).
        self.settings_sound_notification_label = QLabel(self.settings_sound_widget) # Settings sound notification label (name).
        self.settings_sound_notification_button = QPushButton_sound(self, self.settings_sound_widget) # Settings sound notification button (set enabled or disabled).
#_______________________________________________________________________________________________________________________
        """ Settings sub update widget """
        self.settings_update_widget = QWidget(self.settings_sub_scroll_widget) # Settings sub update widget.
        self.settings_update_widget_layout = QGridLayout(self.settings_update_widget) # Settings sub update widget grid layout.
        self.settings_update_title_label = QLabel(self.settings_update_widget) # Settings update title.
        self.settings_update_version_subtitle_label = QLabel(self.settings_update_widget) # Settings update version subtitle.
        self.settings_update_version_desc_title_label = QLabel(self.settings_update_widget) # Settings update version description label (name).
        self.settings_update_version_desc_label = QLabel(self.settings_update_widget) # Settings update version description label (description of current version).
        self.settings_update_version_changelog_title_label = QLabel(self.settings_update_widget) # Settings update version changleog label (name).
        self.settings_update_version_changelog_button = QPushButton_sound(self, self.settings_update_widget) # Settings update version changelog button, for open changelog widget.
        self.settings_update_option_subtitle_label = QLabel(self.settings_update_widget) # Settings update option subtitle.
        self.settings_update_option_autoupdate_title_label = QLabel(self.settings_update_widget) # Settings update option autoupdate label (name).
        self.settings_update_option_autoupdate_button = QPushButton_sound(self, self.settings_update_widget) # Settings update option autoupdate button (set enabled or disabled).
        self.settings_update_option_check_title_label = QLabel(self.settings_update_widget) # Settings update option check label (name).
        self.settings_update_option_check_button = QPushButton_sound(self, self.settings_update_widget) # Settings update option button (check update).
        self.settings_update_advanced_subtitle_label = QLabel(self.settings_update_widget) # Settings update advanced subtitle.
        self.settings_update_advanced_capacity_title_label = QLabel(self.settings_update_widget) # Settings update advanced capacity label (name).
        self.settings_update_advanced_capacity_combobox = QComboBox(self.settings_update_widget) # Settings update advanced capacity list (set capacity of downloading).
        self.settings_update_advanced_verification_title_label = QLabel(self.settings_update_widget) # Settings update advanced verification label (name).
        self.settings_update_advanced_verification_button = QPushButton_sound(self, self.settings_update_widget) # Settings update advanced verification button (check app files).
#_______________________________________________________________________________________________________________________
        """ Settings sub language widget """
        self.settings_lanquage_widget = QWidget(self.settings_sub_scroll_widget) # Settings language widget.
        self.settings_lanquage_widget_layout = QGridLayout(self.settings_lanquage_widget) # Settings language widget grid layout.
        self.settings_language_title_label = QLabel(self.settings_lanquage_widget) # Settings language title.
        self.settings_language_type_label = QLabel(self.settings_lanquage_widget) # Settings language type label (name).
        self.settings_language_type_combobox = QComboBox(self.settings_lanquage_widget) # Settings language type list (set language).
#_______________________________________________________________________________________________________________________
        """ Settings sub report widget """
        self.settings_report_widget = QWidget(self.settings_sub_scroll_widget) # Settings report widget.
        self.settings_report_widget_layout = QGridLayout(self.settings_report_widget) # Settings report widget grid layout.
        self.settings_report_title_label =  QLabel(self.settings_report_widget) # Settings report title.
        self.settings_report_autoreport_title_label = QLabel(self.settings_report_widget) # Settings report autoreport label (name).
        self.settings_report_autoreport_button = QPushButton_sound(self, self.settings_report_widget) # Settings report autoreport button (set enabled or disabled).
        self.settings_report_sendreport_title_label = QLabel(self.settings_report_widget) # Settings report sendreport label (name).
        self.settings_report_sendreport_button = QPushButton_sound(self, self.settings_report_widget) # Settings report sendreport button, for open report widget.
#_______________________________________________________________________________________________________________________
        """ Report widget """
        self.report_widget = QWidget(self) # Report widget.
        self.report_widget_layout = QGridLayout(self.report_widget) # Report widget grid layout.
        self.report_textfield_textarea = QTextEdit(self.report_widget) # Report text area (to write message).
        self.report_send_button = QPushButton_sound(self, self.report_widget) # Report send button, for send message to database.
        self.report_clear_button = QPushButton_sound(self, self.report_widget) # Report clear button, for clear text area.
        self.report_exit_button = QPushButton_sound(self, self.report_widget) # Report exit button, for exit from report to main.
#_______________________________________________________________________________________________________________________
        """ Update widget """
        self.update_background_widget = QWidget(self) # Update background widget.
        self.update_background_widget_layout = QGridLayout(self.update_background_widget) # Update background widget grid layout.
        self.update_changelog_widget = QWidget(self.update_background_widget) # Update changelog widget.
        self.update_changelog_widget_layout = QGridLayout(self.update_changelog_widget) # Update changelog widget grid layout.
        self.update_changelog_title_label = QLabel(self.update_changelog_widget) # Update changelog title.
        self.update_changelog_scroll = QScrollArea(self.update_changelog_widget) # Udapte changelog scroll.
        # Widget adding by script
        self.update_changelog_download_button = QPushButton(self.update_changelog_widget) # Update changelog download button, for download udapte.
        self.update_changelog_exit_button = QPushButton(self.update_changelog_widget) # Update changelog exit button, fot exit from update to main or settings.
#_______________________________________________________________________________________________________________________
        """ Notification widget """
        self.notification_background_widget = QWidget(self) # Notification background widget.
        self.notification_background_label = QLabel(self.notification_background_widget) # Notification background label, for blur effect.
        self.notification_background_label_blur = QGraphicsBlurEffect(self.notification_background_label) # Notification background label, graphics effect.
        self.notification_background_widget_layout = QGridLayout(self.notification_background_widget) # Notification background widget grid layout.
        self.notification_widget = QWidget(self.notification_background_widget) # Notification widget.
        self.notification_widget_layout = QGridLayout(self.notification_background_widget) # Notification widget grid layout.
        self.notification_text_label = QLabel(self.notification_background_widget) # Notification text label, for show message.
        self.notification_exit_button = QPushButton(self.notification_background_widget) # Notification exit button, for hide notification.
        self.notification_anim = QPropertyAnimation(self.notification_background_widget, b'pos') # Notification animation, change position.
#_______________________________________________________________________________________________________________________
        """ Alert widget """
        self.alert_background_widget = QWidget(self) # Alert background widget.
        self.alert_background_widget_layout = QGridLayout(self.alert_background_widget) # Alert background widget grid layout.
        self.alert_widget = QWidget(self.alert_background_widget) # Alert widget.
        self.alert_widget_layout = QGridLayout(self.alert_background_widget) # Alert widget grid layout.
        self.alert_text_label = QLabel(self.alert_background_widget) # Alert text label, for show message.
        self.alert_download_button = QPushButton(self.alert_widget)  # Create download button for alert
        self.alert_exit_button = QPushButton(self.alert_background_widget) # Alert exit button, for hide alert.
#_______________________________________________________________________________________________________________________
        """ Setup Main window """
        set_ObjectName(self) # Set object name, id of items.
        set_Property(self) # Set property, class of items.
        set_Layout(self) # Set layout.
        set_Size(self) # Set size.
        set_Widget(self) # Set widget.
        set_ScrollArea(self) # Set scroll area.
        set_Label(self) # Set label.
        set_ComboBox(self) # Set combobox, list.
        set_Disabled(self) # Set PushButtons disabled.
#_______________________________________________________________________________________________________________________
        """ Controllers, create controllers from main """
        self.controller_notification = controller_notification(self)  # Controller of notification.
        self.controller_settings = controller_settings(self) # Controller of settings.
        self.controller_report = controller_report(self) # Controller of report.
        self.controller_alert = controller_alert(self) # Controller of alert.
        self.controller_update = controller_update(self)  # Controller of update.
        self.controller_main = controller_main(self)  # Controller of main.
        set_Connect(self)  # Set connect buttons to functions.
#_______________________________________________________________________________________________________________________
        """ Ping """
        self.ping = controller_ping(self) # Controller ping.
        self.ping.signal.connect(self.controller_main.main_changelog_controller) # Connect main changelog.
        self.ping.start() # Start thread.
########################################################################################################################
""" Set font function"""
def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/TickerK8_updater/APP_FILES/FONTS/Montserrat-Regular.ttf') # Get font.
    font_families = QFontDatabase.applicationFontFamilies(font_id) # Set font family.
    return QFont(font_families[0]) # Return new font.
########################################################################################################################
""" Start application """
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create app.
    app.setFont(set_font()) # Set font for all application.
    window = Main_window() # Set main widnow.
    window.show() # Show main window.
    sys.exit(app.exec_()) # Exit func.
########################################################################################################################
