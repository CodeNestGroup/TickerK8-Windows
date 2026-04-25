#   --- Import ---
import json

from .Ui import (
    LoginConfigurationReloadStyle,
    AppConfRetranslate
)

def ChangePage(self, i):
    self.StepIndex += i
    if self.StepIndex <= -1:
        self.StepIndex == 0
    elif self.StepIndex >= 6:
        self.StepIndex == 5

    if self.StepIndex in (1, 3, 5):
        self.InfoL.hide()
        if self.StepIndex == 1:
            self.AppConf()
        elif self.StepIndex == 3:
            self.SubConf()
        elif self.StepIndex == 5:
            self.AcceptSettings()
    elif self.StepIndex in (0, 2, 4):
        l = self.Language
        t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationTranslate.json', 'r', encoding='utf-8'))
        self.Reset()
        self.InfoL.show()
        self.InfoL.setText(t['InfoL'][l][self.StepIndex])

def ChangeLanguage(self):
    with open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'r', encoding='utf-8') as file:
        c = json.load(file)
        c['language'] = self.LanguageC.currentIndex()
        with open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'w', encoding='utf-8') as f:
            json.dump(c, f, indent=4)
    self.Language = c['language']
    AppConfRetranslate(self)

def ChangeTheme(self):
    t = json.load(open(f'{self.Path}/assets/JSON/LoginConfigurationAppConfTranslate.json', 'r', encoding='utf-8'))
    with open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'r', encoding='utf-8') as file:
        c = json.load(file)
        c['theme'] = t['ThemeC'][self.ThemeC.currentText()]
        with open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'w', encoding='utf-8') as f:
            json.dump(c, f, indent=4)
    self.Theme = c['theme']
    (self)
    LoginConfigurationReloadStyle(self)
    AppConfRetranslate(self)

def ChangeSub(self, i:int, button):
    with open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'r', encoding='utf-8') as file:
        c = json.load(file)
        c['subscription'] = i
        with open(self.Path+'/assets/JSON/LoginConfigurationConfig.json', 'w', encoding='utf-8') as f:
            json.dump(c, f, indent=4)
    if self.CheckedB:
        self.CheckedB.setStyleSheet('border: none;')
    self.CheckedB = button
    self.CheckedB.setStyleSheet('border: 2px solid green;')

def LoginConfigurationController(self):
    self.LoginConfigurationF()
    self.LoginOpenF()
