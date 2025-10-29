""" Import packages """
import sys
import pathlib
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QDesktopWidget,
    QMainWindow
    )
from PyQt5.QtCore import (
    QRect
    )
from PyQt5.QtGui import (
    QFontDatabase,
    QFont
    )
""" Import application modules """
from login.structure import Login_widget
from register.structure import Register_widget
from recover_password.structure import Recover_password_widget
from main.structure import Main_widget 
from settings.structure import Settings_widget
from statistics.structure import Statistics_widget
from chart.structure import Chart_widget
#______________________________________________________________________________________________________________________

class app_controller(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('window')
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.login_widget = None
        self.register_widget = None
        self.recover_password_widget = None
        self.main_widget = None
        self.settings_widget = None
        self.statistics_widget = None
        self.chart_widget = None
        self.screen = QApplication.primaryScreen()
        self.geometry = self.screen.availableGeometry()
        self.login_setup()
#______________________________________________________________________________________________________________________

    def login_setup(self):
        self.login_widget = Login_widget(self)
        self.layout.addWidget(self.login_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//12)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//1.25)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        self.login_widget.correct_login.connect(self.login_to_main)
        self.login_widget.login_register_button.clicked.connect(self.login_to_register)
    
    def register_setup(self):
        self.register_widget = Register_widget(self)
        self.layout.addWidget(self.register_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//12)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//1.25)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        self.register_widget.register_exit_button.clicked.connect(self.register_to_login)
    
    def recover_password_setup(self):
        self.recover_password_widget = Recover_password_widget(self)
        self.layout.addWidget(self.recover_password_widget)
        pos_x = int(self.geometry.width()//4)
        pos_y = int(self.geometry.height()//12)
        width = int(self.geometry.width()//2)
        height = int(self.geometry.height()//1.25)
        self.setGeometry(QRect(pos_x, pos_y, width, height))
        self.recover_password_widget.recover_password_exit_button.clicked.connect(self.forgot_password_to_login)
    
    def main_setup(self):
        self.main_widget = Main_widget(self)
        self.layout.addWidget(self.main_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.main_widget.settings_button.clicked.connect(self.main_to_settings)
        self.main_widget.logout_button.clicked.connect(self.main_to_login)
    
    def settings_setup(self):
        self.settings_widget = Settings_widget(self)
        self.layout.addWidget(self.settings_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.settings_widget.navi_exit_button.clicked.connect(self.settings_to_main)
    
    def statistics_setup(self):
        self.statistics_widget = Statistics_widget(self)
        self.layout.addWidget(self.statistics_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.statistics_widget.main_exit_button.clicked.connect(self.statistics_to_main)
    
    def chart_setup(self):
        self.chart_widget = Chart_widget(self)
        self.layout.addWidget(self.chart_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.chart_widget.top_exit_button.clicked.connect(self.chart_to_main)
#______________________________________________________________________________________________________________________
    
    def login_to_register(self):
        self.login_widget.deleteLater()
        self.login_widget = None 
        self.register_setup()

    def register_to_login(self):
        self.register_widget.deleteLater()
        self.register_widget = None
        self.login_setup()

    def login_to_forgot_password(self):
        self.login_widget.deleteLater()
        self.login_widget = None
        self.recover_password_setup()

    def forgot_password_to_login(self):
        self.recover_password_widget.deleteLater()
        self.recover_password_widget = None
        self.login_setup()

    def login_to_main(self):
        self.login_widget.deleteLater()
        self.login_widget = None
        self.main_setup()

    def main_to_login(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.login_setup()

    def main_to_settings(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.settings_setup()

    def settings_to_main(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.main_setup()

    def main_to_statistics(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.statistics_setup()

    def statistics_to_main(self):
        self.statistics_widget.deleteLater() 
        self.statistics_widget = None
        self.main_setup()

    def main_to_chart(self):
        self.main_widget.deleteLater()
        self.main_widget = None 
        self.chart_setup()

    def chart_to_main(self):
        self.chart_widget.deleteLater()
        self.chart_widget = None 
        self.main_setup()
#______________________________________________________________________________________________________________________

def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[3])+'/TickerK8_app/APP_FILES/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])
#______________________________________________________________________________________________________________________

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False) 
    sys.exit(application.exec_())