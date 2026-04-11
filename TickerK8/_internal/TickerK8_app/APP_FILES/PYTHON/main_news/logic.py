""" Import pacakges """
import json
import requests
from io import BytesIO
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QGridLayout,
    QSizePolicy,
    QVBoxLayout,
    QSizePolicy
)
from PyQt5.QtCore import (
    Qt,
    QSize
)
from PyQt5.QtGui import (
    QIcon,
    QPixmap
)
#______________________________________________________________________________________________________________________

def news_widget(self, data):
    """ Create objects """
    self.news_widget = QWidget(self.news_scroll)
    self.news_layout = QVBoxLayout(self.news_widget)
    self.news_photo_label = QLabel(self.news_widget)
    self.news_title_label = QLabel(self.news_widget)
    self.news_date_label = QLabel(self.news_widget)
    self.news_content_widget = QWidget(self.news_widget)
    self.news_content_layout = QGridLayout(self.news_content_widget)
    self.news_source_widget = QWidget(self.news_widget)
    self.news_source_layout = QGridLayout(self.news_source_widget)
    self.news_source_title_label = QLabel(self.news_source_widget)
    self.news_hash_widget = QWidget(self.news_widget)
    self.news_hash_layout = QGridLayout(self.news_hash_widget)
    self.news_hash_title_label = QLabel(self.news_hash_widget)
    """ Set object name """
    self.news_widget.setObjectName('news_widget')
    self.news_photo_label.setObjectName('news_photo_label')
    self.news_title_label.setObjectName('news_title_label')
    self.news_date_label.setObjectName('news_date_label')
    self.news_content_widget.setObjectName('news_content_widget')
    self.news_source_widget.setObjectName('news_source_widget')
    self.news_source_title_label.setObjectName('news_source_title_label')
    self.news_hash_widget.setObjectName('news_hash_widget')
    self.news_hash_title_label.setObjectName('news_hash_title_label')
    """ Set property """
    self.news_content_widget.setProperty('class', 'news_div_widget')
    self.news_source_widget.setProperty('class', 'news_div_widget')
    self.news_hash_widget.setProperty('class', 'news_div_widget')
    """ Set layout """
    self.news_layout.addWidget(self.news_photo_label)
    self.news_layout.addWidget(self.news_title_label)
    self.news_layout.addWidget(self.news_date_label)
    self.news_layout.addWidget(self.news_content_widget)
    self.news_layout.addWidget(self.news_source_widget)
    self.news_layout.addWidget(self.news_hash_widget)
    self.news_layout.setSpacing(0)
    self.news_layout.setContentsMargins(0,0,0,0)
    self.news_widget.setLayout(self.news_layout)
    self.news_content_layout.setSpacing(0)
    self.news_content_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_content_layout.setColumnStretch(enc, 1)
    self.news_content_widget.setLayout(self.news_content_layout)
    self.news_source_layout.addWidget(self.news_source_title_label, 0, 2, 1, 96)
    self.news_source_layout.setSpacing(0)
    self.news_source_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_source_layout.setColumnStretch(enc, 1)
    self.news_source_widget.setLayout(self.news_source_layout)
    self.news_hash_layout.addWidget(self.news_hash_title_label, 0, 2, 1, 96)
    self.news_hash_layout.setSpacing(0)
    self.news_hash_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_hash_layout.setColumnStretch(enc, 1)
    self.news_hash_widget.setLayout(self.news_hash_layout)
    """ Set widget """
    self.news_scroll.setWidget(self.news_widget)
    """ Set label """
    self.news_title_label.setAlignment(Qt.AlignCenter)
    self.news_title_label.setWordWrap(True)
    self.news_date_label.setAlignment(Qt.AlignLeft)
    """ Set size """
    self.news_widget.setMaximumWidth(self.news_scroll.width())
    self.news_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_photo_label.setMaximumWidth(self.news_scroll.width())
    self.news_photo_label.setFixedSize(QSize(self.panel_widget.width(), int(self.panel_widget.height()*0.4)))
    self.news_photo_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_title_label.setMaximumWidth(self.news_scroll.width())
    self.news_title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_date_label.setMaximumWidth(self.news_scroll.width())
    self.news_date_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_content_widget.setMaximumWidth(self.news_scroll.width())
    self.news_content_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_source_widget.setMaximumWidth(self.news_scroll.width())
    self.news_source_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_source_title_label.setMaximumWidth(self.news_scroll.width())
    self.news_source_title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_hash_widget.setMaximumWidth(self.news_scroll.width())
    self.news_hash_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    self.news_hash_title_label.setMaximumWidth(self.news_scroll.width())
    self.news_hash_title_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    """ Set text """
    _t = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/main_news/translate.json', 'r', encoding='utf-8'))
    _l = json.load(open(self.main_path+'/TickerK8_app/APP_FILES/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))['language']
    self.news_title_label.setText(data[0])
    self.news_date_label.setText('')
    self.news_source_title_label.setText(_t['news_source_title_label'][_l])
    self.news_hash_title_label.setText(_t['news_hash_title_label'][_l])
    """ Set photo """
    #photo = requests.get(json_file['photo']['original'])
    #photo.raise_for_status()
    ##pix = QPixmap()
    #pix.loadFromData(BytesIO(photo.content).read())
    #zoomed_pix = pix.scaled(self.news_photo_label.width(), int(self.panel_widget.height()*0.5), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    #cropped_pix = zoomed_pix.copy(
    #    (zoomed_pix.width() - self.news_photo_label.width()) // 2,
    #    (zoomed_pix.height() - int(self.panel_widget.height()*0.5)),
    #    self.news_photo_label.width(),
    #    self.news_photo_label.height()
    #)
    #self.news_photo_label.setPixmap(cropped_pix)
    """ Make content """
    for index, rows in enumerate(json.loads(data[2]), start=0):
        label = QLabel(self.news_content_widget)
        label.setObjectName(f'news_content_label_{index}')
        label.setText(rows[3])
        label.setWordWrap(True)
        label.setStyleSheet(rows[2])
        if rows[0] == 'Plain_Text':
            label.setObjectName(f"Plain_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Title_Text':
            label.setObjectName(f"Title_Text_{index}")
            label.setAlignment(Qt.AlignCenter)
        elif rows[0] == 'Heading_1_Text':
            label.setObjectName(f"Heading_1_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_2_Text':
            label.setObjectName(f"Heading_2_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_3_Text':
            label.setObjectName(f"Heading_3_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_4_Text':
            label.setObjectName(f"Heading_4_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        self.news_content_layout.addWidget(label, index, 2, 1, 96)
#______________________________________________________________________________________________________________________
