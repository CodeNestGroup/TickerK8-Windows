""" Import """
""" Import system and operating system packages """
import json # Json package, service of json file
import os # Os package, interaction with operating system.
import time # Time package.
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Widgets """
from PyQt5.QtCore import (Qt, # Qt
                          QPropertyAnimation, # Property animation, siple animation to setup
                          QSequentialAnimationGroup, # Sequential Animation Group 
                          pyqtProperty, # pyqrProperty
                          QRect, # QRect
                          QSize, # QSize
                          QPoint, # QPoint
                          pyqtSignal, # Signal
                          QThread, # Thread
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
""" Import PyQt5 Gui """
from PyQt5.QtGui import (QColor, # Color.
                         QPixmap, # QPixmap
                         QPainter) # Painter
#_______________________________________________________________________________________________________________________
""" Import PyQt5 Svg"""
from PyQt5.QtSvg import QSvgRenderer # Svg render
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
""" Loading animation """
class main_changelog_error_widget(QWidget):
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, main_self):
        super().__init__() # Call class.
        self.main_self = main_self # Main self, main objects of application.
        self.layout = QGridLayout(self) # Main layout
        self.icon_label = QLabel(self) # Icon label
        self.loading_message_label = QLabel(self) # Message label
        self.animation = None
        self.setup() # Setup widget
#______________________________________________________________________________________________________________________
    def setup(self):
        """ Set Object Name """
        self.setObjectName('main_changelog_error_widget')
        self.icon_label.setObjectName('icon_label')
        self.loading_message_label.setObjectName('loading_message_label')
#______________________________________________________________________________________________________________________
        """ Set Layout """
        self.layout.addWidget(self.icon_label, 30, 0, 30, 100)
        self.layout.addWidget(self.loading_message_label, 62, 0, 10, 100)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        for i in range(100):
            self.layout.setRowStretch(i, 1)
            self.layout.setColumnStretch(i, 1)
        self.setLayout(self.layout)
#______________________________________________________________________________________________________________________
        """ Set Widget """
        self.loading_message_label.setHidden(True)
#______________________________________________________________________________________________________________________
        """ Set Alignemnt """
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.loading_message_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
        """ Set Size """
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.icon_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.loading_message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Controller error """
    def controller_error(self):
        try:
            self.animation.stop() # Stop loop
            self.animation.quit()
            self.animation.wait()
            self.animation.deleteLater()
        except:
            pass
        self.loading_message_label.setText(self.main_self.settings_translate_file['main_changelog_error_widget'][0][self.main_self.settings_config_file['__language__']]) # Set text of message 
        self.loading_message_label.setHidden(False) # Show loading message label
#______________________________________________________________________________________________________________________
    """ Controller loading """
    def controller_loading(self):
        try:
            self.animation.stop() # Stop loop
            self.animation.quit()
            self.animation.wait()
            self.animation.deleteLater()
        except:
            pass
        self.animation = self.animation_thread() # Create aniamtion thread
        self.animation.update_text.connect(self.setup_text) # Connect 
        self.animation.start() # Start animation
        self.loading_message_label.setHidden(False) # Show loading message label
    
    def setup_text(self, dots):
        self.loading_message_label.setText(self.main_self.settings_translate_file['main_changelog_error_widget'][1][self.main_self.settings_config_file['__language__']]+dots) # Set text
#______________________________________________________________________________________________________________________
    class animation_thread(QThread):
        update_text = pyqtSignal(str) # Signal
        stop_signal = False # Set defoult
        def run(self):
            dots = "" # Set defoult.
            while not self.stop_signal:
                dots = "." * ((len(dots) + 1) % 4)  # Loop of dots
                self.update_text.emit(dots) # Update text
                time.sleep(0.5) # Wait 500ms.
        def stop(self):
            self.stop_signal = True
#######################################################################################################################
