""" Import """
import pathlib # For get path to folders
import json # For json files
#______________________________________________________________________________________________________________________
""" Import from QtWidgets """
from PyQt5.QtWidgets import (
    QGraphicsView, # Widget that show's scene
    QGraphicsScene, # Scene where candles are placed
    QGraphicsItem, # Candle
    QToolTip, # Widget that show info about candle 
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import from QtGui """
from PyQt5.QtGui import (
    QPainter, # Painter, tool that create/paint item
    QBrush, # Brush 
    QPen, # Pen for single line 
    QColor # For set color 
)
#______________________________________________________________________________________________________________________
""" Import from QtCore """
from PyQt5.QtCore import (
    QRectF, # Rectengle
    Qt, # Qt
    QPointF # Point
)
#######################################################################################################################
""" Candy chart """
class Candle_chart(QGraphicsScene):
    """ __init__ """
    def __init__(self, data, parent=None):
        super().__init__(parent)
#______________________________________________________________________________________________________________________
        """ Get data """
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2]) # Set main path, path to TickerK8 folder.
        self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json')) # Get global config.
        self.data = data # Data for creating chart 
#______________________________________________________________________________________________________________________
        """ Set dafoult """
        self.max_price = None # Max price of chart
        self.min_price = None # Min price of chart
        self.resized_value = None # Flag for one resize 
        self.view_height= None # View height
#______________________________________________________________________________________________________________________
        """ Config Graphic View """
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag) # Enable drag 
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
        """ Config Graphic scene """
        self.setObjectName('main_chart_graphics_scene') # Set object name
#______________________________________________________________________________________________________________________
        """ Call get min max function """
        self.get_min_max()
#______________________________________________________________________________________________________________________
    """ get min max """
    def get_min_max(self):
        local_list = [] # Create local variable
        for s in self.data: local_list += [s['h'], s['l']]# Loop for data, serch highest and lowest price
        self.max_price, self.min_price = max(local_list), min(local_list) # Get highest, lowest price 
#______________________________________________________________________________________________________________________
    """Y position """
    def y_position(self, price):
        return (self.max_price-price)/(self.max_price-self.min_price)*self.view_height
#______________________________________________________________________________________________________________________
    """ Add Candles """
    def add_Candles(self):
        _conf = self.global_config['charts_config'][0]
        _space_between = _conf['space_between']
        for single_data in self.data:
            _date = single_data['d'] # Get candle date
            _open = [single_data['o'], self.y_position(single_data['o'])] # Get candle open price, y_pos
            _high = [single_data['h'], self.y_position(single_data['h'])] # Get candle highest price, y_pos
            _close = [single_data['c'], self.y_position(single_data['c'])] # Get candle close price, y_pos
            _low = [single_data['l'], self.y_position(single_data['l'])] # Get candle lowest price, y_pos
            _vol = single_data['v'] # Get candle volume value
            _color_wick = self.global_config['charts_config'][0]['+_border'] if _close >= _open else self.global_config['charts_config'][0]['-_border']
            _color_body = self.global_config['charts_config'][0]['+_body'] if _close >= _open else self.global_config['charts_config'][0]['-_body']
            _space_between += 4
            self.addItem(Candle(_space_between, _open, _high, _close, _low, _color_wick, _color_body)) # Add candle to scene
        self.setSceneRect(QRectF(0, self.global_config['charts_config'][0]['y_margin'], _space_between+self.global_config['charts_config'][0]['x_margin'], int(self.height()-(self.global_config['charts_config'][0]['y_margin']*2))))
        self.fitInView(QRectF(_space_between-200, self.global_config['charts_config'][0]['y_margin'], self.width(), int(self.height()-(self.global_config['charts_config'][0]['y_margin']*2))), Qt.KeepAspectRatio)
#______________________________________________________________________________________________________________________
    """ Wheel event """
    def wheelEvent(self, event):
        zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(zoom_factor, zoom_factor)
#______________________________________________________________________________________________________________________
    """ Reszie event """
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if not self.resized_value:
            self.view_height = self.height() # Set view height
            self.add_Candles() # Call add candles function
            self.resized_value = True # Enable flag
#######################################################################################################################
""" Single Candle """
class Candle(QGraphicsItem):
    """ __init__ """
    def __init__(self, x=int, o=list, h=list, c=list, l=list, c_w=str, c_b=str):
        super().__init__() # Call super init function 
        self.x = x # X axis start
        self.o = o # Open pirce
        self.h = h # High price
        self.c = c # Close price
        self.l = l # Low price
        self.color_wick = QColor(c_w) # Color of wick 
        self.color_body = QColor(c_b) # Color of body 
        self.setAcceptHoverEvents(True) # Activate hover event 
        self.setToolTip(f'Open: {self.o[0]}\nHigh: {self.h[0]}\nClose: {self.c[0]}\nLow: {self.l[0]}') # Set tool tip, tag with price
#______________________________________________________________________________________________________________________
    """ boundig rect """
    def boundingRect(self):
        return QRectF(self.x, int(self.h[1]), 4, int(self.l[1]-self.h[1]))
#______________________________________________________________________________________________________________________
    """ paint """
    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(self.color_wick, 1)) # Set pen color, size to create high, low price line
        painter.drawLine(QPointF(self.x+2, int(self.h[1])), QPointF(self.x+2, int(self.l[1]))) # Draw line
        painter.setBrush(QBrush(self.color_body)) # Set brush color to create body 
        painter.drawRect(QRectF(self.x, int(min(self.o[1], self.c[1])), 4, int(abs(self.o[1]-self.c[1])))) # Create body 
#______________________________________________________________________________________________________________________
    """ hover enter event """
    def hoverEnterEvent(self, event):
        QToolTip.showText(event.screenPos(), self.toolTip())
        super().hoverEnterEvent(event) # Call function 
#______________________________________________________________________________________________________________________
    """ hover leave event """
    def hoverLeaveEvent(self, event):
        QToolTip.hideText() 
        super().hoverLeaveEvent(event) # Call function 
#######################################################################################################################
