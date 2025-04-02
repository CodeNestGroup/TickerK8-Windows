def main_setConnectButton(self):
    #
    # Main page top Widget
    #

    self.main_top_button_exit.clicked.connect(self.app_off)
    self.main_top_button_window.clicked.connect(self.app_set_screen_mode)
    self.main_top_button_minimize.clicked.connect(self.app_minimize)
# ----------------------------------------------------------------------------------------------------------------------
