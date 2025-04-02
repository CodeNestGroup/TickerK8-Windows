""" Set connect, connect buttons to functions"""
def set_Connect(self):
    """ Self items """
#_______________________________________________________________________________________________________________________
    """ Main widget """
#_______________________________________________________________________________________________________________________
    """ Main changelog """
#_______________________________________________________________________________________________________________________
    """ Main logo """
#_______________________________________________________________________________________________________________________
    """ Main settings"""
    self.main_settings_open_button.clicked.connect(self.controller_main.main_to_settings)
    self.main_settings_social_media_instagram_button.clicked.connect(self.controller_main.open_instagram)
    self.main_settings_social_media_github_button.clicked.connect(self.controller_main.open_github)
    self.main_settings_social_media_discord_button.clicked.connect(self.controller_main.open_discord)
#_______________________________________________________________________________________________________________________
    """ Main update """
#_______________________________________________________________________________________________________________________
    """ Main start button"""
    self.main_start_button.clicked.connect(self.controller_main.open_TickerK8)
#_______________________________________________________________________________________________________________________
    """ Settings widget"""
#_______________________________________________________________________________________________________________________
    """ Settings exit button """
    self.settings_exit_button.clicked.connect(self.controller_main.settings_to_main)
#_______________________________________________________________________________________________________________________
    """ Settings menu scroll """
    self.settings_menu_theme_button.clicked.connect(lambda: self.controller_settings.open_close_sub_widgets(self.settings_theme_widget))
    self.settings_menu_sound_button.clicked.connect(lambda: self.controller_settings.open_close_sub_widgets(self.settings_sound_widget))
    self.settings_menu_update_button.clicked.connect(lambda: self.controller_settings.open_close_sub_widgets(self.settings_update_widget))
    self.settings_mneu_language_button.clicked.connect(lambda: self.controller_settings.open_close_sub_widgets(self.settings_lanquage_widget))
    self.settings_menu_report_button.clicked.connect(lambda: self.controller_settings.open_close_sub_widgets(self.settings_report_widget))
#_______________________________________________________________________________________________________________________
    """ Settings sub scroll """
#_______________________________________________________________________________________________________________________
    """ Settings sub theme widget """
    self.settings_theme_d_n_button.clicked.connect(self.controller_settings.change_day_night)
    self.settings_theme_list_combobox.currentIndexChanged.connect(self.controller_settings.change_theme)
#_______________________________________________________________________________________________________________________
    """ Settings sub sound widget"""
    self.settings_sound_button_button.clicked.connect(lambda: self.controller_settings.set_sound_d_e('__sound_button__'))
    self.settings_sound_alert_button.clicked.connect(lambda: self.controller_settings.set_sound_d_e('__sound_alert__'))
    self.settings_sound_notification_button.clicked.connect(lambda: self.controller_settings.set_sound_d_e('__sound_notification__'))
#_______________________________________________________________________________________________________________________
    """ Settings sub update widget """
    self.settings_update_version_changelog_button.clicked.connect(self.controller_main.settings_to_changlog)
    self.settings_update_option_autoupdate_button.clicked.connect(self.controller_settings.set_auto_update)
    self.settings_update_option_check_button.clicked.connect(self.controller_settings.check_updates)
    self.settings_update_advanced_capacity_combobox.currentIndexChanged.connect(self.controller_settings.set_capacity)
    self.settings_update_advanced_verification_button.clicked.connect(self.controller_update.check_compatibility)
#_______________________________________________________________________________________________________________________
    """ Settings sub language widget """
    self.settings_language_type_combobox.currentIndexChanged.connect(self.controller_settings.change_language)
#_______________________________________________________________________________________________________________________
    """ Settings sub report widget """
    self.settings_report_autoreport_button.clicked.connect(self.controller_settings.set_auto_report)
    self.settings_report_sendreport_button.clicked.connect(self.controller_main.settings_to_report)
#_______________________________________________________________________________________________________________________
    """ Report widget """
    self.report_send_button.clicked.connect(self.controller_report.send_report)
    self.report_clear_button.clicked.connect(self.controller_report.clear)
    self.report_exit_button.clicked.connect(self.controller_main.report_to_settings)
#_______________________________________________________________________________________________________________________
    """ Update widget """
    self.update_changelog_download_button.clicked.connect(self.controller_update.update)
#_______________________________________________________________________________________________________________________
    """ Notification widget """
    self.notification_exit_button.clicked.connect(self.controller_notification.close)
#_______________________________________________________________________________________________________________________
    """ Alert widget """
    self.alert_download_button.clicked.connect(self.controller_main.alert_to_changlog)  # Connect func to open udapte, changelog widget
    self.alert_exit_button.clicked.connect(self.controller_alert.close)
#_______________________________________________________________________________________________________________________
