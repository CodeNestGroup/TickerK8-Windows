import json

def Next(self):
    if self.widget_list_index <= len(self.widget_list)-2:
        self.widget_list_index += 1
    i = self.widget_list_index
    f = self.widget_list[i]
    if f:
        self.info_label.hide()
        self.center_widget_setup()
        f()
    elif not f:
        t = json.load(open(self.main_path+'/PYTHON/login_config/j_translate.json', 'r'))
        l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
        if self.center_widget:
            self.center_widget.deleteLater()
            self.center_widget = None 
        self.info_label.show()
        self.info_label.setText(t['info_label'][l][i])
    
def Previous(self):
    if self.widget_list_index >= 1:
        self.widget_list_index -= 1
    i = self.widget_list_index
    f = self.widget_list[i]
    if f:
        self.info_label.hide()
        self.center_widget_setup()
        f()
    elif not f:
        t = json.load(open(self.main_path+'/PYTHON/login_config/j_translate.json', 'r'))
        l = json.load(open(self.main_path+'/PYTHON/login_config/j_config.json', 'r'))['language']
        if self.center_widget:
            self.center_widget.deleteLater()
            self.center_widget = None 
        self.info_label.show()
        self.info_label.setText(t['info_label'][l][i])

def ResetConfig(self):
    with open(self.main_path+'/PYTHON/login_config/j_config.json', 'r') as file:
        c = json.load(file)
        c['language'] = 0
        c['theme'] = "vintage_elegance_dark"
        c['subscription'] = 0
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)

def ChangeLanguage(self):
    with open(self.main_path+'/PYTHON/login_config/j_config.json', 'r') as file:
        c = json.load(file)
        c['language'] = self.language_combobox.currentIndex()
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)

def ChangeTheme(self):
    with open(self.main_path+'/PYTHON/login_config/j_config.json', 'r') as file:
        c = json.load(file)
        c['theme'] = self.theme_combobox.currentText()
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)

def ChangeSub(self, i:int, button):
    with open(self.main_path+'/PYTHON/login_config/j_config.json', 'r') as file:
        c = json.load(file)
        c['subscription'] = i
        with open(self.main_path+'/PYTHON/login_config/j_config.json', 'w') as f:
            json.dump(c, f, indent=4)
    if self.checked_button:
        self.checked_button.setStyleSheet('border: none;')
    self.checked_button = button
    self.checked_button.setStyleSheet('border: 2px solid green;')
