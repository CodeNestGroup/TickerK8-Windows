#   --- Import ---
import json
#   --- Import UpdateSettings modules ---
from .Ui import (
    UpdateSettingsRetranslate,
    UpdateSettingsReloadStyle,
    LanguageRetranslate,
    StyleRetranslate
    )

def ChangeDayNight(self):
    s = self.Theme.split('_')
    dn = s[-1]
    m = f'{s[0]}_{s[1]}'
    if dn == 'l':
        dn = 'd'
    elif dn == 'd':
        dn = 'l'
    self.ConfigOffline['theme'] = f'{m}_{dn}'
    self.Theme = self.ConfigOffline['theme']
    UpdateSettingsReloadStyle(self)
    StyleRetranslate(self)

def ChangeTheme(self):
    t = json.load(open(f'{self.Path}/assets/JSON/SettingsStyleTranslate.json', 'r', encoding='utf-8'))
    self.ConfigOffline['theme'] = t['StyleThemeThemesValueC'][self.StyleThemeThemesValueC.currentText()]
    self.Theme = self.ConfigOffline['theme']
    UpdateSettingsReloadStyle(self)
    StyleRetranslate(self)

def ChangeLanguage(self):
    self.ConfigOffline['language'] = self.LanguageValueC.currentIndex()
    self.Language = self.ConfigOffline['language']
    UpdateSettingsRetranslate(self)
    LanguageRetranslate(self)

def SaveConfig(self):
    with open(f'{self.Path}/assets/JSON/ConfigOffline.json', 'w', encoding='utf-8') as C:
        json.dump(self.ConfigOffline, C, indent=4)
    self.ReloadConfigOfflineF()
