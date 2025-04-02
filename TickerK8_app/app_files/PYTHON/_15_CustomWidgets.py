from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton, QSizePolicy, QScrollArea, QVBoxLayout, QGraphicsBlurEffect
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QSize, QRect
import requests
import json
import os
from io import BytesIO


class news_main_widget(QWidget):
    def __init__(self, parent, window_widget, database_select):
        super().__init__()
        self.setParent(parent)
        self.parent = parent
        self.window_widget = window_widget
        self.database_select = database_select
        self.button_list = []
        self.button_list_index = 0
        self.news_form_widget = None
        self.news_form_data_list = []

        self.setParent(self.parent)
        print(self.parent.size())

#
# Create Objects
#

        self.layout = QGridLayout(self)
        for data in self.database_select:
            button = QPushButton(self)
            self.layout.addWidget(button, 0, 0, 90, 100)
            button.setFixedSize(int(self.parent.width()), int(self.parent.height()*0.90))

            _json = json.loads(data[1])
            self.news_form_data_list.append(_json)

            response = requests.get(_json["photo"]["original"])
            response.raise_for_status()
            pix = QPixmap()
            pix.loadFromData(BytesIO(response.content).read())

            new_width = int(pix.height() * (button.width() / button.height()))
            scaled_pix = pix.copy((pix.width()-new_width) // 2, 0, new_width, pix.height())

            button.setIcon(QIcon(scaled_pix.scaled(button.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)))
            button.setIconSize(button.size())
            button.clicked.connect(self.open_news_form)

            button.setStyleSheet('background-color: #00000000; border: 0; padding: 0; margin: 0;')

            label = QLabel(button)
            label.setFixedSize(button.size())
            label.setText(_json['title'])
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet('color: #FDFFFC; background-color: #50000000; padding: 1em; font-size: 32px; font-weight: 600; letter-spacing: 0.5em;')

            button.setHidden(True)
            self.button_list.append(button)

        self.button_list[0].setHidden(False)

        self.next_widget = QWidget(self)
        self.next_widget_layout = QGridLayout(self.next_widget)
        self.next_left_button = QPushButton(self.next_widget)
        self.next_right_button = QPushButton(self.next_widget)

        self.timer = QTimer(self)
#----------------------------------------------------------------------------------------------------------------------

#
# ObjectName
#

        self.next_widget.setObjectName('next_widget')
        self.next_left_button.setObjectName('next_left_button')
        self.next_right_button.setObjectName('next_right_button')
#----------------------------------------------------------------------------------------------------------------------

#
# Set Layout
#

        self.layout.addWidget(self.next_widget, 90, 0, 10, 100)

        self.next_widget_layout.addWidget(self.next_left_button, 20, 20, 55, 30)
        self.next_widget_layout.addWidget(self.next_right_button, 20, 50, 55, 30)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        for i in range(100):
            self.layout.setRowStretch(i, 1)
            self.layout.setColumnStretch(i, 1)

        self.next_widget_layout.setSpacing(0)
        self.next_widget_layout.setContentsMargins(0,0,0,0)
        for i in range(100):
            self.next_widget_layout.setRowStretch(i, 1)
            self.next_widget_layout.setColumnStretch(i, 1)

        self.setLayout(self.layout)
        self.next_widget.setLayout(self.next_widget_layout)
#----------------------------------------------------------------------------------------------------------------------

#
# Set Icons
#

        self.next_left_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/arrow-circle-left.png'))
        self.next_right_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/arrow-circle-right.png'))
#----------------------------------------------------------------------------------------------------------------------

#
# Set Connect
#

        self.next_left_button.clicked.connect(self.previous_news)
        self.next_right_button.clicked.connect(self.next_news)
#----------------------------------------------------------------------------------------------------------------------

#
# Set StyleSheet
#

        self.setStyleSheet('''
            #next_widget{
                background-color: #FAF7F0;
            }
            #next_left_button{
                background-color: #D8D2C2;
                border:0;
                padding: 1em;
            }
            #next_left_button:hover{
                background-color: #4A4947;
            }
            #next_right_button{
                background-color: #D8D2C2;
                border:0;
                padding: 1em;
            }
            #next_right_button:hover{
                background-color: #4A4947;
            }
        ''')
#----------------------------------------------------------------------------------------------------------------------

#
# Set Timer
#
        self.timer.timeout.connect(self.next_news)
        self.timer.start(5000)
    # Panel z Newsem co sie bedzie zmienaić co 5s w petli plus sprawdzanie bazy
    # Panel z guzikami i labelem co czas przewijania pokazuje
    def next_news(self):
        self.button_list[self.button_list_index].setHidden(True)
        self.button_list_index = (self.button_list_index + 1) % len(self.button_list)
        self.button_list[self.button_list_index].setHidden(False)
        self.timer.start(5000)


    def previous_news(self):
        self.button_list[self.button_list_index].setHidden(True)
        self.button_list_index = (self.button_list_index - 1) % len(self.button_list)
        self.button_list[self.button_list_index].setHidden(False)
        self.timer.start(5000)

    def open_news_form(self):
        self.news_form_widget = news_form_widget(self.window_widget, self.news_form_data_list, self.button_list_index)
        self.news_form_widget.show()

#----------------------------------------------------------------------------------------------------------------------

#
# News Form Widget
#

class news_form_widget(QWidget):
    def __init__(self, parent, data, data_index):
        super().__init__(parent)
        self._json = data
        self._widget_list_index = data_index
        self._widget_list = []
        self._content_list_dict = []
        self._day_night_mode = True

        self.setParent(parent)

        self.background_widget = QWidget(self)
        self.background_layout = QGridLayout(self.background_widget)

        self.main_widget = QWidget(self.background_widget)
        self.main_widget_layout = QVBoxLayout(self.main_widget)

        self.tools_widget = QWidget(self)
        self.tools_widget_layout = QGridLayout(self.tools_widget)

        self.tools_day_night_button = QPushButton(self.tools_widget)
        self.tools_previous_button = QPushButton(self.tools_widget)
        self.tools_exit_button = QPushButton(self.tools_widget)
        self.tools_next_button = QPushButton(self.tools_widget)
#----------------------------------------------------------------------------------------------------------------------

#
# Set ObjectName
#
        self.background_widget.setObjectName('background_widget')
        self.main_widget.setObjectName('main_widget')
        self.tools_widget.setObjectName('tools_widget')
        self.tools_day_night_button.setObjectName('tools_day_night_button')
        self.tools_previous_button.setObjectName('tools_previous_button')
        self.tools_exit_button.setObjectName('tools_exit_button')
        self.tools_next_button.setObjectName('tools_next_button')

#----------------------------------------------------------------------------------------------------------------------

#
# Set Layout
#

        self.background_layout.addWidget(self.main_widget, 2, 25, 93, 50)
        self.background_layout.addWidget(self.tools_widget, 95, 25, 3, 50)
        self.background_layout.setSpacing(0)
        self.background_layout.setContentsMargins(0, 0, 0, 0)

        for i in range(100):
            self.background_layout.setRowStretch(i, 1)
            self.background_layout.setColumnStretch(i, 1)

        self.background_widget.setLayout(self.background_layout)

        self.main_widget_layout.setSpacing(0)
        self.main_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.main_widget.setLayout(self.main_widget_layout)

        self.tools_widget_layout.addWidget(self.tools_previous_button, 0, 0, 50, 50)
        self.tools_widget_layout.addWidget(self.tools_next_button, 0, 50, 50, 50)
        self.tools_widget_layout.addWidget(self.tools_day_night_button, 50, 0, 50, 50)
        self.tools_widget_layout.addWidget(self.tools_exit_button, 50, 50, 50, 50)

        self.tools_widget_layout.setSpacing(0)
        self.tools_widget_layout.setContentsMargins(0, 0, 0, 0)

        for i in range(100):
            self.tools_widget_layout.setRowStretch(i, 1)
            self.tools_widget_layout.setColumnStretch(i, 1)

        self.tools_widget.setLayout(self.tools_widget_layout)

#----------------------------------------------------------------------------------------------------------------------

#
# Set Size
#
        self.setGeometry(QRect(0, 0, parent.width(), parent.height()))
        self.background_widget.setGeometry(QRect(0, 0, self.width(), self.height()))

#
# Set Widget
#

        #self.background_widget.setGraphicsEffect(QGraphicsBlurEffect().setBlurRadius(20))

#----------------------------------------------------------------------------------------------------------------------

#
# Set Label
#

#----------------------------------------------------------------------------------------------------------------------
#
# Set Button
#


#----------------------------------------------------------------------------------------------------------------------
#
# Set Retranslte
#


#----------------------------------------------------------------------------------------------------------------------
#
# Connect Button
#

        self.tools_day_night_button.clicked.connect(self.day_night_mode)
        self.tools_next_button.clicked.connect(self.next_news)
        self.tools_previous_button.clicked.connect(self.previous_news)
        self.tools_exit_button.clicked.connect(self.exit_news)

#----------------------------------------------------------------------------------------------------------------------

#
# Set Graphics
#
        self.tools_day_night_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/sun.png'))
        self.tools_previous_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/arrow-circle-left.png'))
        self.tools_next_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/arrow-circle-right.png'))
        self.tools_exit_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/exit-alt.png'))

#----------------------------------------------------------------------------------------------------------------------

#
# Set Animation
#

#----------------------------------------------------------------------------------------------------------------------


#
# Setup News
#

        self.setup_news()
        self._widget_list[self._widget_list_index].setHidden(False)

#
# Set StyleSheet
#
        self.setStyleSheet(open(os.getcwd()+'/TickerK8_app/app_files/CSS/_main_news_form_day_css.css').read())
        self.day_content()

#----------------------------------------------------------------------------------------------------------------------
    def setup_news(self):
        for data_json in self._json:
            _scroll = QScrollArea(self.main_widget)
            _scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            _scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            _scroll.setWidgetResizable(True)

            _widget = QWidget(_scroll)

            _widget_layout = QVBoxLayout(_widget)
            _widget_layout.setSpacing(0)
            _widget_layout.setContentsMargins(0, 0, 0, 0)

            _photo = QLabel(_widget)
            _photo.setObjectName('photo')
            _photo.setFixedWidth(int(1920*0.5))
            pix = QPixmap()
            pix.loadFromData(requests.get(data_json['photo']['landscape']).content)
            _photo.setPixmap(pix.scaledToWidth(_photo.width(), Qt.SmoothTransformation))
            #_photo_dimmed = QLabel(_photo)
            #_photo_dimmed.setObjectName('photo_dimmed')
            #_photo_dimmed.setFixedSize(_photo.size())

            _date = QLabel(_widget)
            _date.setObjectName('date')
            _date.setText(f'{data_json['date']}')
            _date.setAlignment(Qt.AlignLeft)

            _title = QLabel(_widget)
            _title.setObjectName('title')
            _title.setText(f'{data_json['title']}')
            _title.setAlignment(Qt.AlignCenter)
            _title.setWordWrap(True)


            _content = QWidget(_widget)
            _content.setObjectName('content_widget')
            _content_layout = QVBoxLayout(_content)
            _content_layout.setSpacing(0)
            _content_layout.setContentsMargins(0, 0, 0, 0)

            _content_dict = {}
            for index, content in enumerate(data_json['content'], start=1):
                label = QLabel(_content)
                _content_dict[label] = [str(content[1]), str(content[2])]
                label.setText(content[3])
                label.setWordWrap(True)
                if content[0] == 'Plain_Text':
                    label.setObjectName(f"Plain_Text_{index}")
                    label.setAlignment(Qt.AlignLeft)

                elif content[0] == 'Title_Text':
                    label.setObjectName(f"Title_Text_{index}")
                    label.setAlignment(Qt.AlignCenter)

                elif content[0] == 'Heading_1_Text':
                    label.setObjectName(f"Heading_1_Text_{index}")
                    label.setAlignment(Qt.AlignLeft)

                elif content[0] == 'Heading_2_Text':
                    label.setObjectName(f"Heading_2_Text_{index}")
                    label.setAlignment(Qt.AlignLeft)

                elif content[0] == 'Heading_3_Text':
                    label.setObjectName(f"Heading_3_Text_{index}")
                    label.setAlignment(Qt.AlignLeft)

                elif content[0] == 'Heading_4_Text':
                    label.setObjectName(f"Heading_4_Text_{index}")
                    label.setAlignment(Qt.AlignLeft)

                _content_layout.addWidget(label)
            _content.setLayout(_content_layout)

            self._content_list_dict.append(_content_dict)

            # Source
            _source = QWidget(_widget)
            _source.setObjectName('source_widget')
            _source_layout = QVBoxLayout(_source)
            _source_layout.setSpacing(0)
            _source_layout.setContentsMargins(0, 0, 0, 0)

            for index, source in enumerate(data_json['source'], start=1):
                button = QPushButton(_source)
                button.setObjectName(f'Source_{index}')
                button.setText(str(source))

                _source_layout.addWidget(button)
            _source.setLayout(_source_layout)

            # Hash
            _hash = QWidget(_widget)
            _hash.setObjectName('hash_widget')
            _hash_layout = QVBoxLayout(_hash)
            _hash_layout.setSpacing(0)
            _hash_layout.setContentsMargins(0, 0, 0, 0)

            for index, hashtag in enumerate(data_json['hash'], start=1):
                button = QPushButton(_hash)
                button.setObjectName(f'Source_{index}')
                button.setText(str(hashtag))

                _hash_layout.addWidget(button)
            _hash.setLayout(_hash_layout)


            _widget_layout.addWidget(_photo)
            _widget_layout.addWidget(_date)
            _widget_layout.addWidget(_title)
            _widget_layout.addWidget(_content)
            _widget_layout.addWidget(_source)
            _widget_layout.addWidget(_hash)

            _widget.setLayout(_widget_layout)
            _scroll.setWidget(_widget)

            self.main_widget_layout.addWidget(_scroll)
            _scroll.setHidden(True)
            self._widget_list.append(_scroll)

    def day_content(self):
        for news in self._content_list_dict:
            for label, style in news.items():
                label.setStyleSheet(style[0])

    def night_content(self):
        for news in self._content_list_dict:
            for label, style in news.items():
                label.setStyleSheet(style[1])

    def day_night_mode(self):
        if self._day_night_mode:
            self.tools_day_night_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/moon.png'))
            self.setStyleSheet(open(os.getcwd()+'/TickerK8_app/app_files/CSS/_main_news_form_night_css.css').read())
            self.night_content()
            self._day_night_mode = False
        else:
            self.tools_day_night_button.setIcon(QIcon(os.getcwd()+'/TickerK8_app/app_files/ICONS/UI/sun.png'))
            self.setStyleSheet(open(os.getcwd()+'/TickerK8_app/app_files/CSS/_main_news_form_day_css.css').read())
            self.day_content()
            self._day_night_mode = True

    def next_news(self):
        self._widget_list[self._widget_list_index].setHidden(True)
        self._widget_list_index = (self._widget_list_index + 1) % len(self._widget_list)
        self._widget_list[self._widget_list_index].setHidden(False)

    def previous_news(self):
        self._widget_list[self._widget_list_index].setHidden(True)
        self._widget_list_index = (self._widget_list_index - 1) % len(self._widget_list)
        self._widget_list[self._widget_list_index].setHidden(False)

    def exit_news(self):
        self.deleteLater()



# dodaj do bazy tytyuł, mniej danych bedzie musiał ciąganć
# dodawaj liste id do głownego newsa