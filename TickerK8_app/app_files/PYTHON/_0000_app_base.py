#
# Import
#

import sys
import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt, QMetaObject
#-----------------------------------------------------------------------------------------------------------------------

#
# Login Widget
#

class Login_widget(QWidget):
    #
    # Init
    #

    def __init__(self, parent):
        super().__init__(parent)
        self.window_widget = parent
        self.setParent(self.window_widget)
        self.main_layout = QGridLayout(self)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Login Widget
        #

        self.login_widget = QWidget(self)
        self.login_widget_layout = QGridLayout(self.login_widget)
        self.login_title_label = QLabel(self.login_widget)
        self.login_login_lineedit = QLineEdit(self.login_widget)
        self.login_password_lineedit = QLineEdit(self.login_widget)
        self.login_login_button = QPushButton(self.login_widget)
        self.login_register_button = QPushButton(self.login_widget)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Register Widget
        #

        self.register_widget = QWidget(self)
        self.register_widget_layout = QGridLayout(self.register_widget)
        self.register_title_label = QLabel(self.register_widget)

        self.register_name_subtitle_label = QLabel(self.register_widget)
        self.register_name_lineedit = QLineEdit(self.register_widget)

        self.register_emial_subtitle_label = QLabel(self.register_widget)
        self.register_emial_lineedit = QLineEdit(self.register_widget)
        self.register_emial_confirm_lineedit = QLineEdit(self.register_widget)

        self.register_phonenumber_subtitle_label = QLabel(self.register_widget)
        self.register_phonenumber_combobox = QComboBox(self.register_widget)
        self.register_phonenumber_lineedit = QLineEdit(self.register_widget)

        self.register_country_subtitle_label = QLabel(self.register_widget)
        self.register_country_combobox = QComboBox(self.register_widget)

        self.register_password_subtitle_label = QLabel(self.register_widget)
        self.register_password_lineedit = QLineEdit(self.register_widget)
        self.register_password_confirm_lineedit = QLineEdit(self.register_widget)

        self.register_register_button = QPushButton(self.register_widget)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Setup Login Widget
    #

    def setup_login_widget(self):
        #
        # Import setup functions
        #

        from _01_login_setObjectName import login_setObjectName
        from _02_login_setProperty import login_setProperty
        from _03_login_setLayout import login_setLayout
        from _04_login_setWidget import login_setWidget
        from _05_login_setLineEdit import login_setLineEdit
        from _06_login_setLabel import login_setLabel
        from _07_login_setPushButton import login_setPushButton
        from _08_login_setRetranslate import login_setRetranslate
        from _09_login_setConnectButton import login_setConnectButton
        from _10_login_setGraphics import login_setGraphics
        from _11_login_setAnimation import login_setAnimation
        from _12_login_setSize import login_setSize
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Call setup functions
        #

        # setObjectName
        login_setObjectName(self)
        # setProperty
        login_setProperty(self)
        # setLayout
        login_setLayout(self)
        # setWidget
        login_setWidget(self)
        # setLineEdit
        login_setLineEdit(self)
        # setLabel
        login_setLabel(self)
        # setPushButton
        login_setPushButton(self)
        # setRetranslate
        login_setRetranslate(self)
        # setConnectButton
        login_setConnectButton(self)
        # setGraphics
        login_setGraphics(self)
        # setAnimation
        login_setAnimation(self)
        # setSize
        login_setSize(self)

# ----------------------------------------------------------------------------------------------------------------------

#
# Main Widget
#

class App_widget(QWidget):
    #
    # Init
    #
    def __init__(self, parent):
        super().__init__(parent)
        self.window_widget = parent
        self.setParent(self.window_widget)

        self.app_mode_fullscreen = True
#-----------------------------------------------------------------------------------------------------------------------

        #
        # App Widget
        #

        self.app_layout = QVBoxLayout(self)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Main panel
        #
        self.main_widget = QWidget(self)
        self.main_widget_layout = QGridLayout(self.main_widget)
        # Main panel Top Widget
        self.main_top_widget = QWidget(self.main_widget)
        self.main_top_widget_layout = QGridLayout(self.main_top_widget)
        self.main_top_button_exit = QPushButton(self.main_top_widget)
        self.main_top_button_window = QPushButton(self.main_top_widget)
        self.main_top_button_minimize = QPushButton(self.main_top_widget)
        self.main_top_button_search_button = QPushButton(self.main_top_widget)
        self.main_top_button_settings = QPushButton(self.main_top_widget)
        # Main panel Center Widget
        self.main_center_widget = QWidget(self.main_widget)
        self.main_center_widget_layout = QGridLayout(self.main_center_widget)
        # Main panel Center Left
        self.main_center_left_label = QLabel(self.main_center_widget)
        # Main panel Center center
        self.main_center_center_label = QLabel(self.main_center_widget)
        # Main panel Center right
        self.main_center_right_widget = QWidget(self.main_center_widget)
        self.main_center_right_widget_layout = QVBoxLayout(self.main_center_right_widget)
        self.main_center_right_deafoult_label = QLabel(self.main_center_right_widget)
        # Main panel down Widget
        self.main_down_widget = QWidget(self.main_widget)
        self.main_down_widget_layout = QGridLayout(self.main_down_widget)
        self.main_down_left_widget = QWidget(self.main_down_widget)
        self.main_down_left_widget_layout = QGridLayout(self.main_down_left_widget)
        self.main_down_left_button_news = QPushButton(self.main_down_left_widget)
        self.main_down_left_button_chart = QPushButton(self.main_down_left_widget)
        self.main_down_left_button_stats = QPushButton(self.main_down_left_widget)
        self.main_down_center_widget = QWidget(self.main_down_widget)
        self.main_down_center_widget_layout = QGridLayout(self.main_down_center_widget)
        self.main_down_center_indi = QPushButton(self.main_down_center_widget)
        self.main_down_center_fore = QPushButton(self.main_down_center_widget)
        self.main_down_right_widget = QWidget(self.main_down_widget)
        self.main_down_right_widget_layout = QGridLayout(self.main_down_right_widget)
        self.main_down_right_button_world = QPushButton(self.main_down_right_widget)
        self.main_down_right_label_world = QLabel(self.main_down_right_button_world)
        self.main_down_right_button_market = QPushButton(self.main_down_right_widget)
        self.main_down_right_label_market = QLabel(self.main_down_right_button_market)
        self.main_down_right_button_country = QPushButton(self.main_down_right_widget)
        self.main_down_right_label_country = QLabel(self.main_down_right_button_country)
# ----------------------------------------------------------------------------------------------------------------------

    def setup_main_widget(self):
        #
        # Import setup functions
        #
        from _01_main_setObjectName import main_setObjectName
        from _02_main_setProperty import main_setProperty
        from _03_main_setLayout import main_setLayout
        from _04_main_setWidget import main_setWidget
        from _05_main_setLineEdit import main_setLineEdit
        from _06_main_setLabel import main_setLabel
        from _07_setPushButton import main_setPushButton
        from _08_main_setRetranslate import main_setRetranslate
        from _09_main_ConnectButtons import main_setConnectButton
        from _10_main_setGraphics import main_setGraphics
        from _11_main_setSize import main_setSize
        from _12_main_setAnimation import main_setAnimation
        from _14_main_setScripts import app_off, app_set_screen_mode, app_minimize, news_controller


        #self.window_widget.setObjectName("Form")
        # Ustaw nowy rozmiar okna
        #self.window_widget.resize(self.new_width, self.new_height)
        #self.window_widget.setWindowFlag(Qt.FramelessWindowHint)
        #self.window_widget.setWindowTitle("STOCK BOT")
        #self.news_controller = news_controller(self.window_widget, self)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Set functions to Variables
        #

        self.app_off = lambda: app_off(self.window_widget.app)
        self.app_set_screen_mode = lambda: app_set_screen_mode(self, self.window_widget)
        self.app_minimize = lambda: app_minimize(self.window_widget)

        self.news_cotroller = news_controller(self)
#-----------------------------------------------------------------------------------------------------------------------

        #
        # Call setup functions
        #

        # setObjectName
        main_setObjectName(self)
        # setProperty
        main_setProperty(self)
        # setLayout
        main_setLayout(self)
        # setWidget
        main_setWidget(self)
        # setLineEdit
        main_setLineEdit(self)
        # setLabel
        main_setLabel(self)
        # setPushButton
        main_setPushButton(self)
        # setRetranslate
        main_setRetranslate(self)
        # setConnectButton
        main_setConnectButton(self)
        # setGraphics
        main_setGraphics(self)
        # setSize
        main_setSize(self)
        # setAnimation
        main_setAnimation(self)

        self.news_cotroller.news_main_create_widget()
# ----------------------------------------------------------------------------------------------------------------------

#
# Window
#

class Window_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_main = QApplication.primaryScreen()
        self.screen_main_size = self.screen_main.size()
        self.setGeometry(QRect(self.screen_main_size.width()//6,
                               self.screen_main_size.height()//6,
                               int(self.screen_main_size.width()//1.5),
                               int(self.screen_main_size.height()//1.5)))
        self.setObjectName('Window')

        self.window_layout = QVBoxLayout(self)
        self.window_layout.setSpacing(0)
        self.window_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.window_layout)

        self.login_widget = None
        self.app_widget = None
        self.app_path = os.getcwd()
        self.app_size = self.size()
        self.app = app

    # Login Widget
    def create_destroy_login_widget(self):
        if not self.login_widget:
            self.login_widget = Login_widget(self)
            self.login_widget.setup_login_widget()
            self.window_layout.addWidget(self.login_widget)
            self.login_widget.show()
        else:
            self.login_widget.deleteLater()

    # Main Widget
    def create_destroy_app_widget(self):
        if not self.app_widget:
            self.app_widget = App_widget(self)
            self.app_widget.setup_main_widget()
            self.window_layout.addWidget(self.app_widget)
            self.app_widget.show()
        else:
            self.app_widget.deleteLater()

    # App Css
    def set_Css(self):
        _json_file = json.load(open(self.app_path+'/TickerK8_app/app_files/JSON/CONFIG/_00_main_config.json'))
        self.setStyleSheet(open(self.app_path+_json_file['__CSS__']).read())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = Window_Widget()
    Window.create_destroy_login_widget()
    Window.set_Css()
    Window.show()
    sys.exit(app.exec_())