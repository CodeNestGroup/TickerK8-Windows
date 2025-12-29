""" Import packages """
import sys
import pathlib
import socket
import time
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    )
from PyQt5.QtCore import (
    QRect,
    QThread,
    pyqtSignal
    )
from PyQt5.QtGui import (
    QFontDatabase,
    QFont
    )
""" Import application modules """
from main.structure import Main_widget
from settings.structure import Settings_widget
from changelog.structure import Changelog_widget
from report.structure import Report_widget
#______________________________________________________________________________________________________________________

class app_controller(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('window')
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.main_widget = None
        self.settings_widget = None
        self.changelog_widget = None
        self.report_widget = None 
        self.screen = QApplication.primaryScreen()
        self.geometry = self.screen.availableGeometry()
        pos_x = self.geometry.width()//4
        pos_y = self.geometry.height()//4
        width = self.geometry.width()//2
        height = self.geometry.height()//2
        self.setGeometry(pos_x, pos_y, width, height)
        self.ping_thread = self.controller_ping()
        self.ping_thread.start()
        self.main_setup()
#______________________________________________________________________________________________________________________

    def main_setup(self):
        self.main_widget = Main_widget(self)
        self.layout.addWidget(self.main_widget)
        self.ping_thread.signal.connect(self.main_widget.main_connect_handle)
        self.main_widget.changelog_widget.connection_signal.connect(self.main_changelog_connection)
        self.main_widget.settings_button.clicked.connect(self.main_to_settings)
    
    def settings_setup(self):
        self.settings_widget = Settings_widget(self)
        self.layout.addWidget(self.settings_widget)
        self.settings_widget.exit_button.clicked.connect(self.settings_to_main)
        self.settings_widget.report_created.connect(lambda: self.settings_widget.sendreport_button.clicked.connect(self.settings_to_report))
        self.settings_widget.update_created.connect(lambda: self.settings_widget.version_changelog_button.clicked.connect(lambda: self.settings_to_changelog('', 's')))
    
    def changelog_setup(self, data, f):
        self.changelog_widget = Changelog_widget(self, data)
        self.layout.addWidget(self.changelog_widget)
        if f == 'm':
            self.changelog_widget.exit_button.clicked.connect(self.changelog_to_main)
        elif f == 's':
            self.changelog_widget.exit_button.clicked.connect(self.changelog_to_settings)

    def report_setup(self):
        self.report_widget = Report_widget(self)
        self.layout.addWidget(self.report_widget)
        self.report_widget.exit_button.clicked.connect(self.report_to_settings)
#______________________________________________________________________________________________________________________

    def main_to_settings(self):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.settings_setup()

    def settings_to_main(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.main_setup()

    def main_to_changelog(self, data, f):
        self.main_widget.deleteLater()
        self.main_widget = None
        self.changelog_setup(data, f)
    
    def changelog_to_main(self):
        self.changelog_widget.deleteLater()
        self.changelog_widget = None
        self.main_setup()
    
    def settings_to_changelog(self, data, f):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.changelog_setup(data, f)
    
    def changelog_to_settings(self):
        self.changelog_widget.deleteLater()
        self.changelog_widget = None
        self.settings_setup()
    
    def settings_to_report(self):
        self.settings_widget.deleteLater()
        self.settings_widget = None
        self.report_setup()

    def report_to_settings(self):
        self.report_widget.deleteLater()
        self.report_widget = None
        self.settings_setup()
#______________________________________________________________________________________________________________________
    
    def main_changelog_connection(self):
        d = self.main_widget.changelog_widget.release_data
        b = self.main_widget.changelog_widget.releases_button_list
        for index, release in enumerate(d, start=0):
            b[index].clicked.connect(lambda _, i=release: self.main_to_changelog(i, 'm'))
#______________________________________________________________________________________________________________________

    class controller_ping(QThread):
        signal = pyqtSignal(bool)
        def __init__(self):
            super().__init__()

        def run(self):
            while True:
                self.single_ping()
                time.sleep(5)

        def single_ping(self):
            try:
                socket.setdefaulttimeout(3)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                self.signal.emit(True)
            except socket.error:
                self.signal.emit(False)
#______________________________________________________________________________________________________________________

def set_font():
    font_id = QFontDatabase.addApplicationFont(str(pathlib.Path(__file__).resolve().parents[2])+'/updater/STYLE/FONTS/NotoSerif-VariableFont_wdth,wght.ttf')
    font_families = QFontDatabase.applicationFontFamilies(font_id) 
    return QFont(font_families[0])
#______________________________________________________________________________________________________________________

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setFont(set_font())
    controller = app_controller()
    controller.setHidden(False)
    sys.exit(application.exec_())
#______________________________________________________________________________________________________________________
