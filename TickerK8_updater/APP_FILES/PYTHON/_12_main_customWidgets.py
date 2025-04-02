""" Import """
""" Import system and operating system packages """
import json # Json package, service of json file
import os # Os package, interaction with operating system.
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Widgets """
from PyQt5.QtCore import (Qt, # Qt
                          QPropertyAnimation, # Property animation, siple animation to setup
                          pyqtProperty, # pyqrProperty
                          QRect, # QRect
                          QPoint, # QPoint
                          QTimer) # QTimer
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Widgets """
from PyQt5.QtWidgets import (QWidget, # Widget, simple widget.
                             QLabel, # Label, simple label.
                             QPushButton, # Button, simple button.
                             QGraphicsDropShadowEffect, # Shadow Graphics effect.
                             QGridLayout, # Grid Layout.
                             QSizePolicy) # Size Policy.
#_______________________________________________________________________________________________________________________
"""" Import PyQt5 Gui """
from PyQt5.QtGui import QColor # Color.
########################################################################################################################
""" Shadow Button """
class ShadowButton(QPushButton):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self, parent): # Parent, get parent
        super().__init__(parent) # Call class.
        self.main_self = main_self # Main self, main objects of application.
        self.initShadow() # Call init shadow function.
        self.initAnimation() # call inir animation function.
        self.clicked.connect(self.click_sound) # Connect call click_sound function.
#_______________________________________________________________________________________________________________________
    """ Init Shadow function, setup shadow for button"""
    def initShadow(self):
        self.shadow = QGraphicsDropShadowEffect() # Create graphics effect
        self.shadow.setBlurRadius(10) # Setup graphic effect, blur radius
        self.shadow.setXOffset(0) # Setup graphic effect, x offest
        self.shadow.setYOffset(0) # Setup graphic effect, y offest
        self.shadow.setColor(QColor(0, 0, 0, 240)) # Setup graphic effect, color
        self.setGraphicsEffect(self.shadow) # Set graphic effect to button
#_______________________________________________________________________________________________________________________
    """ Init Animation, setup animation for button"""
    def initAnimation(self):
        self.anim = QPropertyAnimation(self, b"shadowColor") # Create animation
        self.anim.setDuration(400) # Setup animation, duration
#_______________________________________________________________________________________________________________________
    """ pyqt property """
    @pyqtProperty(QColor)
    def shadowColor(self):
        return self.shadow.color() # Return shadow color
#_______________________________________________________________________________________________________________________
    """ shadow color setter"""
    @shadowColor.setter
    def shadowColor(self, color):
        self.shadow.setColor(color) # Set colorto shadow
#_______________________________________________________________________________________________________________________
    """ Enter event, setup what button should do when cursor entering to the button"""
    def enterEvent(self, event):
        self.enter_sound() # Sound start
        self.anim.stop() # Stop Animation
        self.anim.setStartValue(self.shadow.color()) # Set start value
        self.anim.setEndValue(QColor(0, 0, 0, 130)) # Set end value
        self.anim.start() # Start anim
        self.shadow.setBlurRadius(50) # Set blur radius
        super().enterEvent(event) # Call enter event function
#_______________________________________________________________________________________________________________________
    """ Leave event, setup what button should do when cursor leaving to the button"""
    def leaveEvent(self, event):
        self.leave_sound() # Sound start
        self.anim.stop()  # Stop Animation
        self.anim.setStartValue(self.shadow.color()) # Set start value
        self.anim.setEndValue(QColor(0, 0, 0, 240)) # Set end value
        self.anim.start() # Start anim
        self.shadow.setBlurRadius(10)  # Set blur radius
        super().leaveEvent(event) # Call leave event function
#_______________________________________________________________________________________________________________________
    """ Enter sound"""
    def enter_sound(self):
        if self.check_config(): # Checking user config if playing sound is enebled or disabled
            print('enter') # Playing sound
#_______________________________________________________________________________________________________________________
    """ Leave sound """
    def leave_sound(self):
        if self.check_config(): # Checking user config if playing sound is enebled or disabled
            print('leave') # Playing sound
#_______________________________________________________________________________________________________________________
    """ Click sound """
    def click_sound(self):
        if self.check_config(): # Checking user config if playing sound is enebled or disabled
            print('click') # Playing sound

    """ Check user config """
    def check_config(self):
            return json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))['__sound_button__'] # Returning config
########################################################################################################################
""" QPushButton_sound """
class QPushButton_sound(QPushButton):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self, parent):
        super().__init__(parent) # Call class.
        self.main_self = main_self # Main self, main objects of application.
        self.clicked.connect(self.click_sound) # Connect call click_sound function
#_______________________________________________________________________________________________________________________
    """ Enter event, setup what button should do when cursor entering to the button"""
    def enterEvent(self, event):
        self.enter_sound() # Sound start
        super().enterEvent(event) # Call enter event function
#_______________________________________________________________________________________________________________________
    """ Leave event, setup what button should do when cursor leaving to the button"""
    def leaveEvent(self, event):
        self.leave_sound() # Sound start
        super().leaveEvent(event) # Call leave event function
#_______________________________________________________________________________________________________________________
    """ Enter sound """
    def enter_sound(self):
        if self.check_config(): # Checking user config if playing sound is enebled or disabled
            print('enter') # Playing sound
#_______________________________________________________________________________________________________________________
    """ Leave sound """
    def leave_sound(self):
        if self.check_config(): # Checking user config if playing sound is enebled or disabled
            print('leave') # Playing sound
#_______________________________________________________________________________________________________________________
    """ Click sound """
    def click_sound(self):
        if self.check_config(): # Checking user config if playing sound is enebled or disabled
            print('click')# Playing sound

    """ Check user config """

    def check_config(self):
        return json.load(open(self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_00_settings_config.json', 'r'))['__sound_button__']  # Returning config
########################################################################################################################
