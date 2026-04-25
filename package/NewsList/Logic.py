#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QPushButton,
    QSizePolicy
)
from ..NewsRead.Structure import NewsReadS

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
    if self.Parent.OpenedW.NewsReadS:
        self.Parent.OpenedW.NewsReadS.deleteLater()
        self.Parent.OpenedW.NewsReadS = None
    NewsReadS(self.Parent, self.GetNewsByIdF(i, self.Language))
    self.UpdateNewsPopularityF(i)
    