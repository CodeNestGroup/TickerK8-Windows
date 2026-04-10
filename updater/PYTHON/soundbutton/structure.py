""" Import packages """
import json
import pathlib
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QPushButton
)
""" Import shadow button modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class QPushButton_sound(QPushButton):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        """" Set paths, file name """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.clicked.connect(self.click_sound) 

    def enterEvent(self, event):
        self.enter_sound() 
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.leave_sound()
        super().leaveEvent(event) 

    def enter_sound(self):
        if self.check_config():
            print('enter')

    def leave_sound(self):
        if self.check_config(): 
            print('leave') 

    def click_sound(self):
        if self.check_config():
            print('click')

    def check_config(self):
        return json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['sound']['button']
#______________________________________________________________________________________________________________________
