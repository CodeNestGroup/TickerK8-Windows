from PyQt5.QtWidgets import QSizePolicy


def login_setSize(self):
    #
    # Main Widget
    #

    self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#-----------------------------------------------------------------------------------------------------------------------

    #
    # Login Widget
    #

    self.login_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_login_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.login_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#-----------------------------------------------------------------------------------------------------------------------

    #
    # Register Widget
    #

    self.register_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_emial_confirm_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_phonenumber_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_country_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_country_combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_subtitle_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_password_confirm_lineedit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.register_register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#-----------------------------------------------------------------------------------------------------------------------