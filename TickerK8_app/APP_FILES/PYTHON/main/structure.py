""" Import packages """
import pathlib 
import json
""" Import PyQt5 packages """
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt,
    QTimer
)
""" Import main modules """
from .ui import *
from .logic import *
from main_search.structure import Main_search_widget
from main_news_list.structure import Main_news_list_widget
#______________________________________________________________________________________________________________________

class Main_widget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setParent(parent)
        self.news = None
        self.news_list = None
        self.search_widget = None
        self.objects_list_widget = None
        """ Set paths, file name"""
        self.main_path = str(pathlib.Path(__file__).resolve().parents[2])
        self.main_conf = json.load(open(self.main_path+'/CONFIG/main/background_conf.json', 'r'))
        """ Create objects """
        self.layout = QGridLayout(self)
        self.search_button = QPushButton(self)
        self.objects_list_title_label = QLabel(self)
        self.objects_list_scroll = QScrollArea(self)
        self.type_list_button = QPushButton(self)
        self.data_list_button = QPushButton(self)
        self.settings_button = QPushButton(self)
        self.logout_button = QPushButton(self)
        self.object_icon_label = QLabel(self)
        self.object_ticker_label = QLabel(self)
        self.object_name_label = QLabel(self)
        self.object_time_widget = None
        self.object_chart_widget = None
        self.object_info_widget = None
        self.object_statistics_widget = None
        self.object_news_button = QPushButton(self)
        self.object_chart_button = QPushButton(self)
        self.object_stats_button = QPushButton(self)
        self.news_button_list = []
        self.news_button_index = 0
        self.news_next_left_button = QPushButton(self)
        self.news_next_right_button = QPushButton(self)
        self.news_market_button = QPushButton(self)
        self.news_country_button = QPushButton(self)
        self.news_world_button = QPushButton(self)
        self.timer = QTimer(self)
        self.news_timer = QTimer(self)
        """ Call functions """
        main_ui(self) 
        main_reload_style(self) 
        main_retranslate(self)
        self.widget_background = lambda: widget_background_painter(self)
        self.timer.timeout.connect(self.widget_background)
        self.timer.start(1)
        objects_list_open(self)
        self.object_list_open = lambda: objects_list_open(self)
        object_setup(self)
        news_creator(self)
        """ Connect  functions """
        self.search_button.clicked.connect(lambda: Main_search_widget(self))
        self.type_list_button.clicked.connect(self.objects_list_lists_open)
        self.data_list_button.clicked.connect(self.objects_list_edit_open)
        self.news_next_left_button.clicked.connect(lambda: news_next(self))
        self.news_next_right_button.clicked.connect(lambda: news_previous(self))
        self.news_market_button.clicked.connect(lambda: open_main_news_list(self, 0))
        self.news_country_button.clicked.connect(lambda: open_main_news_list(self, 1))
        self.news_world_button.clicked.connect(lambda: open_main_news_list(self, 2))
#______________________________________________________________________________________________________________________

    def objects_list_lists_open(self):
        """ Set config """
        self.objects_list_title_label.hide()
        self.objects_list_scroll.hide()
        self.type_list_button.hide()
        self.data_list_button.hide()
        """ Create objects """
        self.objects_list_lists_title_label = QLabel(self)
        self.objects_list_lists_scroll = QScrollArea(self)
        self.objects_list_lists_widget = QWidget(self.objects_list_lists_scroll)
        self.objects_list_lists_layout = QVBoxLayout(self.objects_list_lists_widget)
        self.objects_list_lists_exit_button = QPushButton(self)
        """ Call functions """
        object_list_lists_ui(self)
        object_list_lists_reload_style(self)
        object_list_lists_retranslate(self)
        object_list_lists_scroll_setup(self)
        """ Connect functions """
        self.objects_list_lists_exit_button.clicked.connect(lambda: object_list_lists_exit(self))
#______________________________________________________________________________________________________________________

    def objects_list_edit_open(self):
        """ Set config """
        self.objects_list_title_label.hide()
        self.objects_list_scroll.hide()
        self.type_list_button.hide()
        self.data_list_button.hide()
        """ Create objects """
        self.object_list_edit_title_label = QLabel(self)
        self.object_list_edit_scroll = QScrollArea(self)
        self.object_list_edit_widget = QWidget(self.object_list_edit_scroll)
        self.object_list_edit_layout = QGridLayout(self.object_list_edit_widget)
        self.object_list_edit_icon_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_ticker_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_pe_ratio_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_eps_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_dividend_yield_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_capitalization_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_capital_button = QPushButton(self.object_list_edit_widget)
        self.object_list_edit_exit_button = QPushButton(self)
        """ Call functions """
        object_list_edit_ui(self)
        object_list_edit_reload_style(self)
        object_list_edit_retranslate(self)
        object_list_edit_check_selected(self)
        """ Connect functions """
        self.object_list_edit_icon_button.clicked.connect(lambda: object_list_edit_save(self, 'icon'))
        self.object_list_edit_ticker_button.clicked.connect(lambda: object_list_edit_save(self, 'ticker'))
        self.object_list_edit_pe_ratio_button.clicked.connect(lambda: object_list_edit_save(self, 'pe_ratio'))
        self.object_list_edit_eps_button.clicked.connect(lambda: object_list_edit_save(self, 'eps'))
        self.object_list_edit_dividend_yield_button.clicked.connect(lambda: object_list_edit_save(self, 'dividend_yield'))
        self.object_list_edit_capitalization_button.clicked.connect(lambda: object_list_edit_save(self, 'capitalization'))
        self.object_list_edit_capital_button.clicked.connect(lambda: object_list_edit_save(self, 'capital'))
        self.object_list_edit_exit_button.clicked.connect(lambda: object_list_edit_exit(self))
#______________________________________________________________________________________________________________________
