#
# Import
#

import os
from PyQt5.QtGui import QPixmap, QIcon, QMovie
#-----------------------------------------------------------------------------------------------------------------------

#
# set label graphic
#

def main_setGraphics(self):
    #
    # Main Widget
    #
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main page top Widget
    #

    self.main_top_button_exit.setIcon(QIcon(self.window_widget.app_path + '/TickerK8_app/app_files/ICONS/UI/exit-alt.png'))
    self.main_top_button_window.setIcon(QIcon(self.window_widget.app_path + '/TickerK8_app/app_files/ICONS/UI/expand.png'))
    self.main_top_button_minimize.setIcon(QIcon(self.window_widget.app_path + '/TickerK8_app/app_files/ICONS/UI/down-left-and-up-right-to-center.png'))
    self.main_top_button_search_button.setIcon(QIcon(self.window_widget.app_path + '/TickerK8_app/app_files/ICONS/UI/analyse-alt.png'))
    self.main_top_button_settings.setIcon(QIcon(self.window_widget.app_path + '/TickerK8_app/app_files/ICONS/UI/settings-sliders.png'))
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main panel center right Widget
    #

    self.main_center_right_deafoult_label.setPixmap(QPixmap(self.window_widget.app_path + '/TickerK8_app/app_files/ICONS/UI/newspaper.png'))
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main page down left Widget
    #

    #self.Main_down_left_button_news.setIcon(QIcon(self.app_path+'TickerK8_app/img/main_graphics/newspaper.svg"))
    #self.Main_down_left_button_chart.setIcon(QIcon("./img/main_graphics/chart-mixed-up-circle-dollar.svg"))
    #self.Main_down_left_button_stats.setIcon(QIcon("./img/main_graphics/chart-pie-alt.svg"))
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main page down center Widget
    #

    #self.Main_down_center_indi.setIcon(QIcon("./img/main_graphics/fuel-gauge.svg"))
    #self.Main_down_center_fore.setIcon(QIcon("./img/main_graphics/cloud-sun-rain.svg"))
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main page down right Widget
    #

# ----------------------------------------------------------------------------------------------------------------------
