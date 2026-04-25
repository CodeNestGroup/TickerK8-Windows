#   --- Improt ---
import sqlite3
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy
)
from PySide6.QtCore import (
    Qt
)

def SetupData(self, MainSelf):
    conn = sqlite3.connect(f'{self.Path}/assets/DB/Tickerk8Offline.db')
    cur = conn.cursor()
    b = None
    for ListName, ListItems in self.ObjectList.items():
        self.NameL.setText(ListName)
        i = 0
        for SectionName, SectionItems in ListItems.items():
            SectionNameL = QLabel(self.DataW)
            SectionNameL.setObjectName(f'SectionNameL{SectionName}')
            SectionNameL.setProperty('class', 'SectionNameL')
            self.DataL.addWidget(SectionNameL, i, 0, 1, 100)
            SectionNameL.setAlignment(Qt.AlignCenter)
            SectionNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            SectionNameL.setText(SectionName)
            i += 1
            for ii, ItemData in enumerate(SectionItems, 1):
                cur.execute(f'SELECT icon, ticker, name FROM "{ItemData['type']}" WHERE id=?;', (int(ItemData['id']),))
                r = cur.fetchone()
                if r:
                    if self.SetData[0]:
                        ObjectIndexL = QLabel(self.DataW)
                        ObjectIndexL.setObjectName(f'ObjectIndexL{ii}')
                        ObjectIndexL.setProperty('class', 'IndexL')
                        self.DataL.addWidget(ObjectIndexL, i, 0, 1, 10)
                        ObjectIndexL.setAlignment(Qt.AlignCenter)
                        ObjectIndexL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        ObjectIndexL.setText(f'{ii}')
                    if self.SetData[1]:
                        ObjectIconL = QLabel(self.DataW)
                        ObjectIconL.setObjectName(f'ObjectIconL{ii}')
                        ObjectIconL.setProperty('class', 'IconL')
                        self.DataL.addWidget(ObjectIconL, i, 10, 1, 15)
                        ObjectIconL.setAlignment(Qt.AlignCenter)
                        ObjectIconL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        #ObjectIconL.setText(r[0])
                    if self.SetData[2]:
                        ObjectTickerB = QPushButton(self.DataW)
                        ObjectTickerB.setObjectName(f'ObjectTickerB{ii}')
                        ObjectTickerB.setProperty('class', 'TickerB')
                        self.DataL.addWidget(ObjectTickerB, i, 25, 1, 25)
                        ObjectTickerB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        ObjectTickerB.setText(r[1])
                        ObjectTickerB.clicked.connect(lambda _, ObjectData={"type":ItemData['type'], "id":ItemData['id'], "listname":ListName, "sectionname":SectionName, "objectplace":ii-1}: self.Open(MainSelf , ObjectData))
                        if ItemData['type'] == 'stock' and b == None:
                            b = ObjectTickerB
                    if self.SetData[3]:
                        ObjectNameL = QLabel(self.DataW)
                        ObjectNameL.setObjectName(f'ObjectNameL{ii}')
                        ObjectNameL.setProperty('class', 'NameL')
                        self.DataL.addWidget(ObjectNameL, i, 50, 1, 50)
                        ObjectNameL.setAlignment(Qt.AlignCenter)
                        ObjectNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        ObjectNameL.setText(r[2])
                i+= 1
    if b and self.SetData[4]:
        b.click()
    conn.close()