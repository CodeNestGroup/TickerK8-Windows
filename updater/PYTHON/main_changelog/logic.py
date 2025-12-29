""" Import packages """
""" Import PyQT5 packages """
from PyQt5.QtCore import (
    QTimer
)
#______________________________________________________________________________________________________________________
    
def loading_thread(self):
    self.timer = QTimer(self.widget)
    self.timer.timeout.connect(lambda: update_label(self))
    self.timer.start(500)
#______________________________________________________________________________________________________________________

def update_label(self):
    t = self.dots_label.text()
    l = len(t)
    if l < 14:
        self.dots_label.setText(t+'.')
    else:
        self.dots_label.setText('.')
#______________________________________________________________________________________________________________________
