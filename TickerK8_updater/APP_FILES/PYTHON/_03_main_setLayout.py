""" Set layout function, setup layout, add items to layout, setlayout for widgets, set placement"""
def set_Layout(self):
    """ Self items """
    self.layout.addWidget(self.main_widget)
    self.layout.addWidget(self.settings_widget)
    self.layout.addWidget(self.update_background_widget)
    self.layout.addWidget(self.report_widget)
    self.layout.setSpacing(0)
    self.layout.setContentsMargins(0,0,0,0)
    self.setLayout(self.layout)
#_______________________________________________________________________________________________________________________
    """ Main widget """
    self.main_widget_layout.addWidget(self.main_changelog_scroll, 0, 0, 90, 50)
    self.main_widget_layout.addLayout(self.main_logo_layout, 0, 50, 35, 50)
    self.main_widget_layout.addLayout(self.main_settings_layout, 35, 50, 40, 50)
    self.main_widget_layout.addLayout(self.main_update_layout, 90, 0, 10, 60)
    self.main_widget_layout.addWidget(self.main_start_button, 90, 50, 10, 50)
    self.main_widget_layout.setSpacing(0)
    self.main_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.main_widget_layout.setRowStretch(i, 1)
        self.main_widget_layout.setColumnStretch(i, 1)
    self.main_widget.setLayout(self.main_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Main logo """
    self.main_logo_layout.addWidget(self.main_logo_c_n_g_label,0, 0, 100, 50)
    self.main_logo_layout.addWidget(self.main_logo_ticker_label, 0, 50, 100, 50)
    self.main_logo_layout.setSpacing(0)
    self.main_logo_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.main_logo_layout.setRowStretch(i, 1)
        self.main_logo_layout.setColumnStretch(i, 1)
#_______________________________________________________________________________________________________________________
    """ Main settings """
    self.main_settings_layout.addWidget(self.main_settings_open_button, 0, 0, 50, 50)
    self.main_settings_layout.addWidget(self.main_settings_social_media_instagram_button, 0, 50, 50, 50)
    self.main_settings_layout.addWidget(self.main_settings_social_media_github_button, 50, 0, 50, 50)
    self.main_settings_layout.addWidget(self.main_settings_social_media_discord_button, 50, 50, 50, 50)
    self.main_settings_layout.setSpacing(0)
    self.main_settings_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_settings_layout.setRowStretch(i, 1)
        self.main_settings_layout.setColumnStretch(i, 1)
#_______________________________________________________________________________________________________________________
    """ Main update """
    self.main_update_layout.addWidget(self.main_update_progress, 0, 0, 100, 100)
    self.main_update_layout.addWidget(self.main_update_label, 0, 0, 100, 100)
    self.main_update_layout.setSpacing(0)
    self.main_update_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_update_layout.setRowStretch(i, 1)
        self.main_update_layout.setColumnStretch(i, 1)
#_______________________________________________________________________________________________________________________
    """ Main start button"""
#_______________________________________________________________________________________________________________________
    """ Settings widget"""
    self.settings_widget_layout.addWidget(self.settings_menu_scroll, 0, 0, 90, 30)
    self.settings_widget_layout.addWidget(self.settings_exit_button, 90, 0, 10, 30)
    self.settings_widget_layout.addWidget(self.settings_sub_scroll, 0, 30, 100, 70)
    self.settings_widget_layout.setSpacing(0)
    self.settings_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.settings_widget_layout.setRowStretch(i, 1)
        self.settings_widget_layout.setColumnStretch(i, 1)
    self.settings_widget.setLayout(self.settings_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings exit button """
#_______________________________________________________________________________________________________________________
    """ Settings menu scroll """
    self.settings_menu_scroll_widget_layout.addWidget(self.settings_menu_theme_button)
    self.settings_menu_scroll_widget_layout.addWidget(self.settings_menu_sound_button)
    self.settings_menu_scroll_widget_layout.addWidget(self.settings_menu_update_button)
    self.settings_menu_scroll_widget_layout.addWidget(self.settings_mneu_language_button)
    self.settings_menu_scroll_widget_layout.addWidget(self.settings_menu_report_button)
    self.settings_menu_scroll_widget_layout.setSpacing(0)
    self.settings_menu_scroll_widget_layout.setContentsMargins(0,0,0,0)
    self.settings_menu_scroll_widget.setLayout(self.settings_menu_scroll_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings sub scroll """
    self.settings_sub_scroll_widget_layout.addWidget(self.settings_theme_widget)
    self.settings_sub_scroll_widget_layout.addWidget(self.settings_sound_widget)
    self.settings_sub_scroll_widget_layout.addWidget(self.settings_update_widget)
    self.settings_sub_scroll_widget_layout.addWidget(self.settings_lanquage_widget)
    self.settings_sub_scroll_widget_layout.addWidget(self.settings_report_widget)
    self.settings_sub_scroll_widget_layout.setSpacing(0)
    self.settings_sub_scroll_widget_layout.setContentsMargins(0, 0, 0, 0)
    self.settings_sub_scroll_widget.setLayout(self.settings_sub_scroll_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings sub theme widget """
    self.settings_theme_widget_layout.addWidget(self.settings_theme_title_label, 0, 0, 1, 100)
    self.settings_theme_widget_layout.addWidget(self.settings_theme_d_n_label, 1, 0, 1, 50)
    self.settings_theme_widget_layout.addWidget(self.settings_theme_d_n_button, 1, 50, 1, 50)
    self.settings_theme_widget_layout.addWidget(self.settings_theme_list_label, 2, 0, 1, 50)
    self.settings_theme_widget_layout.addWidget(self.settings_theme_list_combobox, 2, 50, 1, 50)
    self.settings_theme_widget_layout.setSpacing(0)
    self.settings_theme_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.settings_theme_widget_layout.setColumnStretch(i, 1)
    self.settings_theme_widget.setLayout(self.settings_theme_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings sub sound widget"""
    self.settings_sound_widget_layout.addWidget(self.settings_sound_title_label, 0, 0, 1, 100)
    self.settings_sound_widget_layout.addWidget(self.settings_sound_button_label, 1, 0, 1, 50)
    self.settings_sound_widget_layout.addWidget(self.settings_sound_button_button, 1, 50, 1, 50)
    self.settings_sound_widget_layout.addWidget(self.settings_sound_alert_label, 2, 0, 1, 50)
    self.settings_sound_widget_layout.addWidget(self.settings_sound_alert_button, 2, 50, 1, 50)
    self.settings_sound_widget_layout.addWidget(self.settings_sound_notification_label, 3, 0, 1, 50)
    self.settings_sound_widget_layout.addWidget(self.settings_sound_notification_button, 3, 50, 1, 50)
    self.settings_sound_widget_layout.setSpacing(0)
    self.settings_sound_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.settings_sound_widget_layout.setColumnStretch(i, 1)
    self.settings_sound_widget.setLayout(self.settings_sound_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings sub update widget """
    self.settings_update_widget_layout.addWidget(self.settings_update_title_label, 0, 0, 1, 100)
    self.settings_update_widget_layout.addWidget(self.settings_update_version_subtitle_label, 1, 0, 1, 100)
    self.settings_update_widget_layout.addWidget(self.settings_update_version_desc_title_label, 2, 0, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_version_desc_label, 2, 50, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_version_changelog_title_label, 3, 0, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_version_changelog_button, 3, 50, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_option_subtitle_label, 4, 0, 1, 100)
    self.settings_update_widget_layout.addWidget(self.settings_update_option_autoupdate_title_label, 5, 0, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_option_autoupdate_button, 5, 50, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_option_check_title_label, 6, 0, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_option_check_button, 6, 50, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_advanced_subtitle_label, 7, 0, 1, 100)
    self.settings_update_widget_layout.addWidget(self.settings_update_advanced_capacity_title_label, 8, 0, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_advanced_capacity_combobox, 8, 50, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_advanced_verification_title_label, 9, 0, 1, 50)
    self.settings_update_widget_layout.addWidget(self.settings_update_advanced_verification_button, 9, 50, 1, 50)
    self.settings_update_widget_layout.setSpacing(0)
    self.settings_update_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.settings_update_widget_layout.setColumnStretch(i, 1)
    self.settings_update_widget.setLayout(self.settings_update_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings sub language widget """
    self.settings_lanquage_widget_layout.addWidget(self.settings_language_title_label, 0, 0, 1, 100)
    self.settings_lanquage_widget_layout.addWidget(self.settings_language_type_label, 1, 0, 1, 50)
    self.settings_lanquage_widget_layout.addWidget(self.settings_language_type_combobox, 1, 50, 1, 50)
    self.settings_lanquage_widget_layout.setSpacing(0)
    self.settings_lanquage_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.settings_lanquage_widget_layout.setColumnStretch(i, 1)
    self.settings_lanquage_widget.setLayout(self.settings_lanquage_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Settings sub report widget """
    self.settings_report_widget_layout.addWidget(self.settings_report_title_label, 0, 0, 1, 100)
    self.settings_report_widget_layout.addWidget(self.settings_report_autoreport_title_label, 1, 0, 1, 50)
    self.settings_report_widget_layout.addWidget(self.settings_report_autoreport_button, 1, 50, 1, 50)
    self.settings_report_widget_layout.addWidget(self.settings_report_sendreport_title_label, 2, 0, 1, 50)
    self.settings_report_widget_layout.addWidget(self.settings_report_sendreport_button, 2, 50, 1, 50)
    self.settings_report_widget_layout.setSpacing(0)
    self.settings_report_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.settings_report_widget_layout.setColumnStretch(i, 1)
    self.settings_report_widget.setLayout(self.settings_report_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Report widget """
    self.report_widget_layout.addWidget(self.report_textfield_textarea, 10, 10, 80, 80)
    self.report_widget_layout.addWidget(self.report_send_button, 94, 10, 2, 22)
    self.report_widget_layout.addWidget(self.report_clear_button, 94, 39, 2, 22)
    self.report_widget_layout.addWidget(self.report_exit_button, 94, 68, 2, 22)
    self.report_widget_layout.setSpacing(0)
    self.report_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.report_widget_layout.setRowStretch(i, 1)
        self.report_widget_layout.setColumnStretch(i, 1)
    self.report_widget.setLayout(self.report_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Update widget """
    self.update_background_widget_layout.addWidget(self.update_changelog_widget, 10, 10, 80, 80)
    self.update_background_widget_layout.setSpacing(0)
    self.update_background_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.update_background_widget_layout.setRowStretch(i, 1)
        self.update_background_widget_layout.setColumnStretch(i, 1)
    self.update_background_widget.setLayout(self.update_background_widget_layout)
    self.update_changelog_widget_layout.addWidget(self.update_changelog_title_label, 5, 5, 10, 90)
    self.update_changelog_widget_layout.addWidget(self.update_changelog_scroll, 20, 5, 60, 90)
    self.update_changelog_widget_layout.addWidget(self.update_changelog_download_button, 85, 40, 4, 20)
    self.update_changelog_widget_layout.addWidget(self.update_changelog_exit_button, 91, 40, 4, 20)
    self.update_changelog_widget_layout.setSpacing(0)
    self.update_changelog_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.update_changelog_widget_layout.setRowStretch(i, 1)
        self.update_changelog_widget_layout.setColumnStretch(i, 1)
    self.update_changelog_widget.setLayout(self.update_changelog_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Notification widget """
    self.notification_background_widget_layout.addWidget(self.notification_widget, 10, 20, 80, 60)
    self.notification_background_widget_layout.setSpacing(0)
    self.notification_background_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.notification_background_widget_layout.setRowStretch(i, 1)
        self.notification_background_widget_layout.setColumnStretch(i, 1)
    self.notification_background_widget.setLayout(self.notification_background_widget_layout)
    self.notification_widget_layout.addWidget(self.notification_text_label, 5, 5, 70, 90)
    self.notification_widget_layout.addWidget(self.notification_exit_button, 80, 40, 10, 20)
    self.notification_widget_layout.setSpacing(0)
    self.notification_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.notification_widget_layout.setRowStretch(i, 1)
        self.notification_widget_layout.setColumnStretch(i, 1)
    self.notification_widget.setLayout(self.notification_widget_layout)
#_______________________________________________________________________________________________________________________
    """ Alert widget """
    self.alert_background_widget_layout.addWidget(self.alert_widget, 15, 15, 70, 70)
    self.alert_background_widget_layout.setSpacing(0)
    self.alert_background_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.alert_background_widget_layout.setRowStretch(i, 1)
        self.alert_background_widget_layout.setColumnStretch(i, 1)
    self.alert_background_widget.setLayout(self.alert_background_widget_layout)
    self.alert_widget_layout.addWidget(self.alert_text_label, 30, 10, 20, 80)
    self.alert_widget_layout.addWidget(self.alert_download_button, 55, 40, 10, 20)
    self.alert_widget_layout.addWidget(self.alert_exit_button, 80, 40, 10, 20)
    self.alert_widget_layout.setSpacing(0)
    self.alert_widget_layout.setContentsMargins(0, 0, 0, 0)
    for i in range(100):
        self.alert_widget_layout.setRowStretch(i, 1)
        self.alert_widget_layout.setColumnStretch(i, 1)
    self.alert_widget.setLayout(self.alert_widget_layout)
#_______________________________________________________________________________________________________________________
