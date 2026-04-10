from PyQt5.QtWidgets import (
    QPushButton,
    QSizePolicy
)
from NewsRead.AStructure import NewsReadS

def CreateList(self):
    for i, d in enumerate(self.GetNewsListData, start=1):
        if i == 1:
            OpenNewsRead(self, d[0])
        button = QPushButton(self.ListW)
        button.setObjectName(f'ListB{i}')
        button.setProperty('class', 'ListB')
        self.ListL.addWidget(button)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setText(f'{d[1]} | {d[2]}')
        button.clicked.connect(lambda _, news_id=d[0]: OpenNewsRead(self, news_id))

def OpenNewsRead(self, i):
    if self.MainSelf.OpenedW.NewsReadS:
        self.MainSelf.OpenedW.NewsReadS.deleteLater()
        self.MainSelf.OpenedW.NewsReadS = None
    NewsReadS(self.MainSelf, self.MainSelf.GetNewsById(i, self.Language))
    self.MainSelf.UpdateNewsPopularity(i)
    