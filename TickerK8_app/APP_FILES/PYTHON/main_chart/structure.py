""" Import packages """
import pathlib
import json
import sqlite3
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsItem
)
from PyQt5.QtCore import Qt
""" Import main chart modules """
from .ui import *
from .logic import *
#______________________________________________________________________________________________________________________

class Main_chart(QGraphicsView):
    def __init__(self, parent, data):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.chart_data = data
        self.main_scence = QGraphicsScene(self)
        """ Call functions """
        main_chart_ui(self)
        main_chart_reload_style(self)
        candle_chart(self)
#______________________________________________________________________________________________________________________
