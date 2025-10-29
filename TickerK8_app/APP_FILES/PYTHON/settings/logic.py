""" Import packages """
import json
#______________________________________________________________________________________________________________________

def open_sub_widget(self, to_open):
    if self.opened_sub_widget != to_open: 
        if not self.opened_sub_widget:
            to_open.setHidden(False)
            self.opened_sub_widget = to_open
        else:
            self.opened_sub_widget.setHidden(True)
            to_open.setHidden(False)
        self.opened_sub_widget = to_open
    elif self.opened_sub_widget == to_open:
        to_open.setHidden(True)
        self.opened_sub_widget = None
#______________________________________________________________________________________________________________________

def change_day_night(self):
    _index = self.style_theme_themes_content_combobox.currentIndex()
    if _index%2:
        self.style_theme_themes_content_combobox.setCurrentIndex(int(_index-1)) 
    else:
        self.style_theme_themes_content_combobox.setCurrentIndex(int(_index+1))
#_______________________________________________________________________________________________________________________

def change_theme(self):
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _global_config['theme'] = int(self.style_theme_themes_content_combobox.currentIndex())
    json.dump(_global_config, open(self.main_self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    self.settings_reload_style()
#______________________________________________________________________________________________________________________

def set_sound_d_e(self, _type):
    """ get config """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _t = json.load(open(self.main_path+'/CONFIG/settings/translate.json', 'r'))
    _l = _global_config['language']
    _global_config['sound'][_type] = not _global_config['sound'][_type] 
    _new_value = _global_config['sound'][_type]
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    button = None
    if _type == '_button_':
        button = self.sound_button_content_button
    elif _type == '_alert_':
        button = self.sound_alert_content_button
    elif _type == '_notification_':
        button = self.sound_notification_content_button
    if button:
        button.setText(_t[f'sound{_type}content_button'][_l][_new_value])
#_______________________________________________________________________________________________________________________

def change_language(self):
    """ Get data """
    _global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))
    _global_config['language'] = int(self.language_langauge_content_combobox.currentIndex())  
    json.dump(_global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4)
    self.settings_retranslate()
#______________________________________________________________________________________________________________________
