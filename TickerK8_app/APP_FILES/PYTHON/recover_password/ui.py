""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QLineEdit, # Simple line edit
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" Recover password Ui """
def recover_password_ui(self):
    """ Set object name """
    self.setObjectName('recover_password_widget')
    self.recover_password_title_label.setObjectName('recover_password_title_label')
    self.recover_password_requirments_label.setObjectName('recover_password_requirments_label')
    self.recover_password_password_lineedit.setObjectName('recover_password_password_lineedit')
    self.recover_password_password_show_button.setObjectName('recover_password_password_show_button')
    self.recover_password_confirm_password_lineedit.setObjectName('recover_password_confirm_password_lineedit')
    self.recover_password_confirm_password_show_button.setObjectName('recover_password_confirm_password_show_button')
    self.recover_password_code_label.setObjectName('recover_password_code_label')
    self.recover_password_time_label.setObjectName('recover_password_time_label')
    self.recover_password_code_lineedit.setObjectName('recover_password_code_lineedit')
    self.recover_password_code_button.setObjectName('recover_password_code_button')
    self.recover_password_confirm_button.setObjectName('recover_password_confirm_button')
    self.recover_password_exit_button.setObjectName('recover_password_exit_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.recover_password_password_lineedit.setProperty('class', 'recover_password_password_line')
    self.recover_password_confirm_password_lineedit.setProperty('class', 'recover_password_password_line')
    self.recover_password_password_show_button.setProperty('class', 'recover_password_password_button')
    self.recover_password_confirm_password_show_button.setProperty('class', 'recover_password_password_button')
    self.recover_password_confirm_button.setProperty('class', 'recover_password_button')
    self.recover_password_exit_button.setProperty('class', 'recover_password_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.recover_password_layout.addWidget(self.recover_password_title_label, 5, 0, 5, 100)
    self.recover_password_layout.addWidget(self.recover_password_password_lineedit, 20, 5, 2, 40)
    self.recover_password_layout.addWidget(self.recover_password_password_show_button, 20, 77, 2, 18)
    self.recover_password_layout.addWidget(self.recover_password_requirments_label, 20, 45, 8, 32)
    self.recover_password_layout.addWidget(self.recover_password_confirm_password_lineedit, 26, 5, 2, 40)
    self.recover_password_layout.addWidget(self.recover_password_confirm_password_show_button, 26, 77, 2, 18)
    self.recover_password_layout.addWidget(self.recover_password_code_label, 35, 35, 15, 30)
    self.recover_password_layout.addWidget(self.recover_password_time_label, 55, 40, 5, 20)
    self.recover_password_layout.addWidget(self.recover_password_code_lineedit, 65, 40, 3, 20)
    self.recover_password_layout.addWidget(self.recover_password_code_button, 70, 40, 4, 20)
    self.recover_password_layout.addWidget(self.recover_password_confirm_button, 85, 28, 5, 20)
    self.recover_password_layout.addWidget(self.recover_password_exit_button, 85, 52, 5, 20)
    self.recover_password_layout.setSpacing(0)
    self.recover_password_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.recover_password_layout.setRowStretch(enc, 1)
        self.recover_password_layout.setColumnStretch(enc, 1)
    self.setLayout(self.recover_password_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.setHidden(False)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.recover_password_title_label.setAlignment(Qt.AlignCenter)
    self.recover_password_requirments_label.setAlignment(Qt.AlignCenter)
    self.recover_password_code_label.setAlignment(Qt.AlignCenter)
    self.recover_password_time_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set line edit """
    self.recover_password_password_lineedit.setEchoMode(QLineEdit.Password)
    self.recover_password_confirm_password_lineedit.setEchoMode(QLineEdit.Password)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_requirments_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_password_show_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_confirm_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_confirm_password_show_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_code_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_time_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_code_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_code_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_confirm_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.recover_password_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################
""" Recover password style """
def recover_password_style(self):
    self.setStyleSheet(open(str(self.main_path+'/TickerK8_app/APP_FILES/STYLE/CSS/RECOVER_PASSWORD/'+self.global_config['__theme__']+'.css')).read())
#######################################################################################################################
""" Recover password retranslate """
def recover_password_translate(self):
    _t = self.recover_password_translate # Translate texts 
    _l = self.global_config['__language__'] # Language 
    self.recover_password_title_label.setText(_t['recover_password_title_label'][_l])
    self.recover_password_requirments_label.setText(_t['recover_password_requirments_label'][_l])
    self.recover_password_password_lineedit.setPlaceholderText(_t['recover_password_password_lineedit'][_l])
    self.recover_password_password_show_button.setText(_t['recover_password_password_show_button'][_l][1])
    self.recover_password_confirm_password_lineedit.setPlaceholderText(_t['recover_password_confirm_password_lineedit'][_l])
    self.recover_password_confirm_password_show_button.setText(_t['recover_password_confirm_password_show_button'][_l][1])
    self.recover_password_time_label.setText(_t['recover_password_time_label'][_l])
    self.recover_password_code_lineedit.setPlaceholderText(_t['recover_password_code_lineedit'][_l])
    self.recover_password_code_button.setText(_t['recover_password_code_button'][_l])
    self.recover_password_confirm_button.setText(_t['recover_password_confirm_button'][_l])
    self.recover_password_exit_button.setText(_t['recover_password_exit_button'][_l])
#######################################################################################################################
