""" Import packages """
import pathlib 
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem,
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QRectF
)
#______________________________________________________________________________________________________________________

def main_chart_ui(self):
    """ Set object name """
    self.setObjectName('main_chart_graphic')
    self.main_scence.setObjectName('main_scence')
    """ Set graphics """
    self.setScene(self.main_scence)
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.setDragMode(QGraphicsView.NoDrag)
    """ Set size """
    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_scence.setSceneRect(QRectF(self.rect()))
#______________________________________________________________________________________________________________________

def main_chart_reload_style(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    self.setStyleSheet(open(str(self.main_path+'/STYLE/CSS/main_chart/'+_global_config['theme']+'.css')).read())
#______________________________________________________________________________________________________________________
