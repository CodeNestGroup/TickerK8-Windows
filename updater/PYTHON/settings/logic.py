""" Import packages"""
import json 
import hashlib
import pathlib
import urllib.request
""" Import PyQt5 packages """
from PyQt5.QtCore import (
    QThread,
    pyqtSignal
)
""" Import settings modules"""
from .ui import (
    settings_reload_style,
    settings_retranslate,
    theme_retranslate,
    sound_retranslate,
    language_retranslate
    )
#______________________________________________________________________________________________________________________

def change_d_n(self):
    """ Change config """
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    t = g['theme'][:-1]
    i = g['theme_index']
    if i%2:
        t += 'l'
        i -= 1
    else:
        t += 'd'
        i += 1
    g['theme'] = t
    g['theme_index'] = i
    json.dump(g, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4)
    """ Reload """
    settings_reload_style(self)
    theme_retranslate(self)
    self.list_combobox.setCurrentIndex(i)
#______________________________________________________________________________________________________________________

def change_theme(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    i = int(self.list_combobox.currentIndex())
    if i == 0:
        t = 'vintage_elegance_l'
    elif i == 1:
        t = 'vintage_elegance_d'
    g['theme'] = t
    g['theme_index'] = i
    json.dump(g, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4)
    """ Reload """
    settings_reload_style(self)
    theme_retranslate(self)
#______________________________________________________________________________________________________________________

def change_sound_d_e(self, t):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    g['sound'][t] = not g['sound'][t]
    json.dump(g, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4)
    """ Reload """
    sound_retranslate(self)
#______________________________________________________________________________________________________________________

def change_capacity(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    g['capacity'] = self.advanced_capacity_combobox.currentIndex()
    json.dump(g, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4)
#______________________________________________________________________________________________________________________

def change_language(self):
    g = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r', encoding='utf-8'))
    g['language'] = self.type_combobox.currentIndex()
    json.dump(g, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w', encoding='utf-8'), indent=4)
    """ Reload """
    settings_retranslate(self)
    language_retranslate(self)
#______________________________________________________________________________________________________________________
