""" Import """
""" Import PyQT5 Core """
from PyQt5.QtCore import QRect # Import QRect.
#_______________________________________________________________________________________________________________________
""" Import PyQT5 Widgets """
from PyQt5.QtWidgets import QSizePolicy # Size Policy.
########################################################################################################################
""" Set size function, set size of objects"""
def set_Size(self):
    """ Self items """
    self.setGeometry(QRect(self.screen_size.width() // 4, self.screen_size.height() // 4, self.screen_size.width() // 2, self.screen_size.height() // 2))
#_______________________________________________________________________________________________________________________
    """ Main widget """
    self.main_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Main changelog """
    self.main_changelog_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Main logo """
    self.main_logo_c_n_g_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_logo_ticker_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Main settings"""
    self.main_settings_open_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_social_media_instagram_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_social_media_github_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_settings_social_media_discord_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Main update """
    self.main_update_progress.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.main_update_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Main start button"""
    self.main_start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings widget"""
    self.settings_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings exit button """
    self.settings_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings menu scroll """
    self.settings_menu_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_menu_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_menu_theme_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_menu_sound_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_menu_update_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_mneu_language_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_menu_report_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings sub scroll """
    self.settings_sub_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sub_scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings sub theme widget """
    self.settings_theme_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_d_n_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_d_n_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_list_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_theme_list_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings sub sound widget"""
    self.settings_sound_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_button_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_button_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_alert_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_alert_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_notification_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_sound_notification_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings sub update widget """
    self.settings_update_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_version_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_version_desc_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_version_desc_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_version_changelog_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_version_changelog_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_option_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_option_autoupdate_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_option_check_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_option_check_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_advanced_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_advanced_capacity_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_advanced_capacity_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_advanced_verification_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_update_advanced_verification_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings sub language widget """
    self.settings_lanquage_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_language_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_language_type_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_language_type_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Settings sub report widget """
    self.settings_report_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_report_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_report_autoreport_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_report_autoreport_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_report_sendreport_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.settings_report_sendreport_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Report widget """
    self.report_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.report_textfield_textarea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.report_send_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.report_clear_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.report_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Update widget """
    self.update_background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_changelog_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_changelog_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_changelog_scroll.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_changelog_download_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.update_changelog_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Notification widget """
    self.notification_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.notification_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.notification_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
    """ Alert widget """
    self.alert_background_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.alert_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.alert_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.alert_exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#_______________________________________________________________________________________________________________________
