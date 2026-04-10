import json
from .AUi import (
    SettingsRetranslate,
    SettingsReloadStyle,
    LanguageRetranslate,
    StyleRetranslate
    )

def ChangeDayNight(self):
    s = self.Theme.split('_')
    dn = s[-1]
    m = f'{s[0]}_{s[1]}'
    if dn == 'light':
        dn = 'dark'
    elif dn == 'dark':
        dn = 'light'
    self.Config['theme'] = f'{m}_{dn}'
    self.Theme = self.Config['theme']
    SettingsReloadStyle(self)
    StyleRetranslate(self)

def ChangeTheme(self):
    t = json.load(open(f'{self.Path}/APP_FILES/PYTHON/Settings/CStylePageRetranslate.json', 'r', encoding='utf-8'))
    self.Config['theme'] = t['StyleThemeThemesValueC'][self.StyleThemeThemesValueC.currentText()]
    self.Theme = self.Config['theme']
    SettingsReloadStyle(self)

def ChangeLanguage(self):
    self.Config['language'] = self.LanguageValueC.currentIndex()
    self.Language = self.Config['language']
    SettingsRetranslate(self)
    LanguageRetranslate(self)

