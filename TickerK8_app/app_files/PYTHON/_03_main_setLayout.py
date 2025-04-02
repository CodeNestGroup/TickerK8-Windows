def main_setLayout(self):
    #
    # App Widget
    #

    # Add Widget
    self.app_layout.addWidget(self.main_widget)

    # Setup Layout
    self.app_layout.setSpacing(0)
    self.app_layout.setContentsMargins(0,0,0,0)
    # Set Layout
    self.setLayout(self.app_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page
    #

    # Add Widget
    self.main_widget_layout.addWidget(self.main_top_widget, 0, 0, 8, 100)
    self.main_widget_layout.addWidget(self.main_center_widget, 8, 0, 70, 100)
    self.main_widget_layout.addWidget(self.main_down_widget, 78, 0, 22, 100)

    # Setup Layout
    self.main_widget_layout.setSpacing(0)
    self.main_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_widget_layout.setRowStretch(i, 1)
        self.main_widget_layout.setColumnStretch(i, 1)

    # Set Layout
    self.main_widget.setLayout(self.main_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page Top Widget
    #

    # Add Widget
    self.main_top_widget_layout.addWidget(self.main_top_button_exit, 35, 5, 30, 3)
    self.main_top_widget_layout.addWidget(self.main_top_button_window, 35, 9, 30, 3)
    self.main_top_widget_layout.addWidget(self.main_top_button_minimize, 35, 13, 30, 3)
    self.main_top_widget_layout.addWidget(self.main_top_button_search_button, 25, 40, 50, 20)
    self.main_top_widget_layout.addWidget(self.main_top_button_settings, 35, 93, 30, 3)

    # Setup Layout
    self.main_top_widget_layout.setSpacing(0)
    self.main_top_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_top_widget_layout.setRowStretch(i, 1)
        self.main_top_widget_layout.setColumnStretch(i, 1)

    # Set Layout
    self.main_top_widget.setLayout(self.main_top_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page Center Widget
    #

    # Add Widget
    self.main_center_widget_layout.addWidget(self.main_center_left_label, 0, 0, 100, 30)
    self.main_center_widget_layout.addWidget(self.main_center_center_label, 0, 30, 100, 40)
    self.main_center_widget_layout.addWidget(self.main_center_right_widget, 0, 70, 100, 30)

    # Setup Layout
    self.main_center_widget_layout.setSpacing(0)
    self.main_center_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_center_widget_layout.setRowStretch(i, 1)
        self.main_center_widget_layout.setColumnStretch(i, 1)

    # Set Layout
    self.main_center_widget.setLayout(self.main_center_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page Center Right Widget
    #

    # Add Widget
    self.main_center_right_widget_layout.addWidget(self.main_center_right_deafoult_label)

    # Setup Lyout
    self.main_center_right_widget_layout.setSpacing(0)
    self.main_center_right_widget_layout.setContentsMargins(0,0,0,0)

    # Set Layout
    self.main_center_right_widget.setLayout(self.main_center_right_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page Down Widget
    #

    # Add Widget
    self.main_down_widget_layout.addWidget(self.main_down_left_widget, 0, 0, 100, 30)
    self.main_down_widget_layout.addWidget(self.main_down_center_widget, 0, 30, 100, 40)
    self.main_down_widget_layout.addWidget(self.main_down_right_widget, 0, 70, 100, 30)

    # Setup Layout
    self.main_down_widget_layout.setSpacing(0)
    self.main_down_widget_layout.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.main_down_widget_layout.setRowStretch(i, 1)
        self.main_down_widget_layout.setColumnStretch(i, 1)

    # Set Layout
    self.main_down_widget.setLayout(self.main_down_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page Down Left Widget
    #

    # Add Widget
    self.main_down_left_widget_layout.addWidget(self.main_down_left_button_news, 0, 0)
    self.main_down_left_widget_layout.addWidget(self.main_down_left_button_chart, 0, 1)
    self.main_down_left_widget_layout.addWidget(self.main_down_left_button_stats, 0, 2)

    # Setup Layout
    self.main_down_left_widget_layout.setSpacing(0)
    self.main_down_left_widget_layout.setContentsMargins(0,0,0,0)

    # Set Layout
    self.main_down_left_widget.setLayout(self.main_down_left_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------

    #
    # Main Page Down Center Widget
    #

    # Add Widget
    self.main_down_center_widget_layout.addWidget(self.main_down_center_indi, 0, 0)
    self.main_down_center_widget_layout.addWidget(self.main_down_center_fore, 0, 1)

    # Setup Layout
    self.main_down_center_widget_layout.setSpacing(0)
    self.main_down_center_widget_layout.setContentsMargins(0,0,0,0)

    # Set Layout
    self.main_down_center_widget.setLayout(self.main_down_center_widget_layout)
#-----------------------------------------------------------------------------------------------------------------------
    #
    # Main Page Down Right Widget
    #

    # Add Widget
    self.main_down_right_widget_layout.addWidget(self.main_down_right_button_world, 0, 0)
    self.main_down_right_widget_layout.addWidget(self.main_down_right_button_market, 0, 1)
    self.main_down_right_widget_layout.addWidget(self.main_down_right_button_country, 0, 2)

    # Setup Layout
    self.main_down_right_widget_layout.setSpacing(0)
    self.main_down_right_widget_layout.setContentsMargins(0,0,0,0)

    # Set Layout
    self.main_down_right_widget.setLayout(self.main_down_right_widget_layout)
#----------------------------------------------------------------------------------------------------------------------
