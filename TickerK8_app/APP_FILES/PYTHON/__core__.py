#   --- Import ---
import sys
import json
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
from login.structure import Login_widget
from register.structure import Register_widget
from login_config.p_structure import Login_configuration_widget
from recover_password.structure import Recover_password_widget
from Main.AStructure import MainW 
from Settings.AStructure import SettingsW
from statistics.structure import Statistics_widget
from chart.structure import Chart_widget
from db.connection import database
#______________________________________________________________________________________________________________________
from ResourcePath.Structure import ResourcePath

class app_controller(QWidget):
    def __init__(self):
        super().__init__()
        self.main_path = ResourcePath(2)
        self.setObjectName('window')
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.login_widget = None
        self.logged_user_id = None
        self.logged_user_sub = None
        self.register_widget = None
        self.login_configuration_widget = None
        self.recover_password_widget = None
        self.main_widget = None
        self.settings_widget = None
        self.statistics_widget = None
        self.chart_widget = None
        self.database = database()
        self.screen = QApplication.primaryScreen()
        self.geometry = self.screen.availableGeometry()
        self.pos_x = int(self.geometry.width()//4)
        self.pos_y = int(self.geometry.height()//12)
        self.width = int(self.geometry.width()//2)
        self.height = int(self.geometry.height()//1.25)
        self.login_setup()
#______________________________________________________________________________________________________________________

    def login_setup(self):
        self.logged_user_id = None
        self.logged_user_sub = None
        self.login_widget = Login_widget(self)
        self.layout.addWidget(self.login_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.login_widget.login_login_button.clicked.connect(self.login_controller)
        self.login_widget.login_register_button.clicked.connect(self.login_to_register)
    
    def register_setup(self):
        self.register_widget = Register_widget(self)
        self.layout.addWidget(self.register_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.register_add_country()
        self.register_add_prefix()
        self.register_widget.correct_data.connect(self.register_user)
        self.register_widget.register_exit_button.clicked.connect(self.register_to_login)
    
    def login_configuration_setup(self):
        self.login_configuration_widget = Login_configuration_widget(self)
        self.layout.addWidget(self.login_configuration_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.login_configuration_widget.accept_button.clicked.connect(self.login_configuration_controller)
        self.login_configuration_widget.exit_button.clicked.connect(self.login_configuration_to_login)
    
    def recover_password_setup(self):
        self.recover_password_widget = Recover_password_widget(self)
        self.layout.addWidget(self.recover_password_widget)
        self.setGeometry(QRect(self.pos_x, self.pos_y, self.width, self.height))
        self.recover_password_widget.recover_password_exit_button.clicked.connect(self.forgot_password_to_login)
    
    def main_setup(self):
        self.main_widget = MainW(self)
        self.layout.addWidget(self.main_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.main_widget.NavSettingsB.clicked.connect(self.main_to_settings)
        self.main_widget.NavLogoutB.clicked.connect(self.main_to_login)

    def settings_setup(self):
        self.settings_widget = SettingsW(self)
        self.layout.addWidget(self.settings_widget)
        self.setGeometry(self.geometry)
        self.showMaximized()
        self.settings_widget.NaviExitB.clicked.connect(self.settings_to_main)
    
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

    def login_to_login_configuration(self):
        self.login_widget.deleteLater()
        self.login_widget = None 
        self.login_configuration_setup()
    
    def login_configuration_to_login(self):
        self.login_configuration_widget.deleteLater()
        self.login_configuration_widget = None
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
        self.database.SaveSettings(self.logged_user_id, self.settings_widget.Config['theme'], self.settings_widget.Config['language'])
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

#   --- Modules functions  ---

    def login_controller(self):
        d = self.database.LoginByName(str(self.login_widget.login_login_lineedit.text()))
        if d[1] == self.login_widget.login_password_lineedit.text():
            if d[2]:
                pass # Dopisać kiedyś notyfikacje że ktoś inny jest już zalogowany
            else:
                self.logged_user_id = d[0]
                if not d[3]:
                    self.login_to_login_configuration()
                else:
                    self.database.UpdateLastLogin(d[0])
                    self.login_to_main()
        else:
            self.login_widget.login_login_lineedit.clear()
            self.login_widget.login_password_lineedit.clear()
            self.login_widget.login_login_lineedit.setStyleSheet('border: 2px solid red;')
            self.login_widget.login_password_lineedit.setStyleSheet('border: 2px solid red;')
    
    def register_add_country(self):
        r = self.database.GetCountries()
        self.register_widget.register_country_combobox.addItems(r)
    
    def register_add_prefix(self):
        r = self.database.GetPhonePrefix()
        self.register_widget.register_phonenumber_combobox.addItems(r)

    def register_user(self, user_data: tuple):
        try:
            err = self.database.RegisterUser(user_data)
            if not err:
                self.register_to_login()
            else:
                for e in err:
                    if e == 'USER_EXISTS':
                        self.register_widget.user_exists()
                    elif e == 'EMAIL_EXISTS':
                        self.register_widget.email_exists()
                    elif e == 'PHONE_EXISTS_IN_PREFIX':
                        self.register_widget.phone_exists()
                    else:
                        raise Exception
        except Exception as e:
            print(e) # Dopisz do logi
    
    def login_configuration_controller(self):
        self.database.LoginConfiguration(self.logged_user_id)
        self.login_configuration_to_login()
            
#______________________________________________________________________________________________________________________

def set_font():
    print(ResourcePath(3))
    font_id = QFontDatabase.addApplicationFont(str(ResourcePath(3)+'/APP_FILES/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf'))
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])
#______________________________________________________________________________________________________________________

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False) 
    sys.exit(application.exec_())
    