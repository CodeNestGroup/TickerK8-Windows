#   --- Import ---
import datetime
import sqlite3
import json
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QScrollArea,
    QWidget,
    QGridLayout,
    QPushButton,
    QLabel,
    QSizePolicy
)

from PySide6.QtCore import (
    Qt
)


from PySide6.QtGui import (
    QLinearGradient,
    QPalette,
    QBrush,
    QColor,
    QPixmap,
    QPainter
)


from ..Object.Structure import ObjectW
from ..ObjectInfo.Structure import ObjectInfoS
from ..ObjectStats.Structure import ObjectStatsS

#   --- Dynamic Background ---
def BackgroundPainter(self):
    l = self.Language
    ColorsJson = self.BackgroundConf['background']
    Color0 = '#000000'
    Color1 = '#000000'
    Color2 = '#000000'
    Alpha1 = 'ff'
    Alpha2 = 'ff'
    X1 = 0.0
    X2 = 1.0 
#       --- Calculate index and precent ---
    Now = datetime.datetime.now()
    TodaySec = Now.hour*3600+Now.minute*60+Now.second
    if TodaySec >=86400:
        TodaySec = 86399
    Index = TodaySec//8640 
    Percent = (TodaySec/8640)-Index 
#       --- Set colors ---
    if Percent <= 0.5:
        X1 = 1-(Percent*2)
        X2 = 1.0
        Alpha1 = 'ff'
        Alpha2 = f'{int(255 *(Percent / 0.5)):02X}'
        Color0 = f'#ff{ColorsJson[Index-1]}'
    else:
        X1 = 0.0
        X2 = 1-(Percent-0.5)*2
        Alpha1 = f'{255-int(255 *(Percent - 0.5) / 0.5):02X}'
        Alpha2 = 'ff'
        Color0 = f'#ff{ColorsJson[Index]}'
    Color1 = f'#{Alpha1}{ColorsJson[Index-1]}'
    Color2 = f'#{Alpha2}{ColorsJson[Index]}'
#       --- Paint background ---
    Pixmap = QPixmap(self.size())
    Pixmap.fill(QColor(Color0))
    Painter = QPainter(Pixmap)
    Gradient = QLinearGradient(0,0,self.width(), 0)
    Gradient.setColorAt(X1, QColor(Color1))
    Gradient.setColorAt(X2, QColor(Color2))
    Painter.fillRect(self.rect(), Gradient)
    Painter.end()
    Palette = self.palette()
    Palette.setBrush(QPalette.Window, QBrush(Pixmap))
    self.setAutoFillBackground(True)
    self.setPalette(Palette)

def ReloadConfig(self):
    self.Config = json.loads(self.GetUserConfig(self.LoggedUserId)[0])
    self.Theme = self.Config['theme']
    self.Language = self.Config['language']
    self.ObjectList = self.Config['lists']

def SetupMainObject(self, d):
    if self.ObjectW:
        self.ObjectW.deleteLater()
        self.ObjectW = None
    self.ObjectW = ObjectW(self, d['type'], d['id'])
    self.OpenedL.addWidget(self.ObjectW, 0, 35, 100, 30)

def SetupObject(self, d):
    if self.ObejctInfoS:
        self.ObejctInfoS.deleteLater()
        self.ObejctInfoS = None
    if self.ObjectStatsS:
        self.ObjectStats.deleteLater()
        self.ObjectStats = None 
    self.ObejctInfoS = ObjectInfoS(self, d['type'], d['id'])
    self.ObjectStatsW = ObjectStatsS(self, d['type'], d['id'])
    self.OpenedL.addWidget(self.ObejctInfoS, 0, 16, 100, 41)
    self.OpenedL.addWidget(self.ObjectStatsW, 0, 58, 100, 41)

def ListAddSetupList(self):
    conn = sqlite3.connect(f'{self.Path}/assets/DB/Tickerk8Offline.db')
    cur = conn.cursor()
    for ListName, ListItems in self.ObjectList.items():
        self.NameL.setText(ListName)
        i = 0
        for SectionName, SectionItems in ListItems.items():
            SectionNameL = QLabel(self.ListAddW)
            SectionNameL.setObjectName(f'SectionNameL{SectionName}')
            SectionNameL.setProperty('class', 'SectionNameL')
            self.ListAddL.addWidget(SectionNameL, i, 0, 1, 100)
            SectionNameL.setAlignment(Qt.AlignCenter)
            SectionNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            SectionNameL.setText(SectionName)
            i += 1
            last = 0
            for ii, ItemData in enumerate(SectionItems, 1):
                cur.execute(f'SELECT name FROM "{ItemData['type']}" WHERE id=?;', (int(ItemData['id']),))
                r = cur.fetchone()
                if r:
                    AddB = QPushButton(self.ListAddW)
                    AddB.setObjectName(f'AddB{ii}')
                    AddB.setProperty('class', 'AddB')
                    self.ListAddL.addWidget(AddB, i, 0, 1, 100)
                    AddB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    AddB.setText('+')
                    AddB.clicked.connect(lambda _, L_N=ListName, S_N=SectionName, I_I=ii: ListAddPlace(self, L_N, S_N, I_I))
                    i += 1
                    ObjectNameL = QLabel(self.ListAddW)
                    ObjectNameL.setObjectName(f'ObjectNameL{ii}')
                    ObjectNameL.setProperty('class', 'ObjectNameL')
                    self.ListAddL.addWidget(ObjectNameL, i, 0, 1, 100)
                    ObjectNameL.setAlignment(Qt.AlignCenter)
                    ObjectNameL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    ObjectNameL.setText(r[0])
                    i += 1
                    last = ii
            last += ii
            AddB = QPushButton(self.ListAddW)
            AddB.setObjectName(f'AddB{last}')
            AddB.setProperty('class', 'AddB')
            self.ListAddL.addWidget(AddB, i, 0, 1, 100)
            AddB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            AddB.setText('+')
            AddB.clicked.connect(lambda _, L_N=ListName, S_N=SectionName, I_I=last: ListAddPlace(self, L_N, S_N, I_I))
            i += 1
    conn.close()

def ListAddPlace(self, Table, Section, IdObject):
    self.AddObjectData = {}
    self.AddObjectData["UserId"] = self.LoggedUserId
    self.AddObjectData["TableName"] = Table
    self.AddObjectData["SectionName"] = Section
    self.AddObjectData["NewObjectPlace"] = IdObject
    self.ListSearchPage()

def SortTypeChange(self, t):
    self.SortType = t
    SetupResultS(self)

def SetupResultS(self):
    conn = sqlite3.connect(f'{self.Path}/assets/DB/Tickerk8Offline.db')
    cur = conn.cursor()
    cur.execute(f'SELECT id, name FROM {self.SortType} WHERE name like "%{self.SearchE.text()}%";')
    data = cur.fetchall()
    conn.close()
    if self.ResultS:
        self.ResultS.deleteLater()
        self.ResultS = None
#           --- Create objects ---
    self.ResultS = QScrollArea(self.SearchW)
    self.ResultW = QWidget(self.ResultS)
    self.ResultL = QGridLayout(self.ResultW)
    self.ResultS.setObjectName('ResultS')
    self.ResultW.setObjectName('ResultW')
    self.ResultL.setSpacing(0)
    self.ResultL.setContentsMargins(0,0,0,0)
    for i in range(100):
        self.ResultL.setColumnStretch(i,1)
    self.ResultW.setLayout(self.ResultL)
    self.SearchL.addWidget(self.ResultS, 20, 2, 80, 96)
    self.ResultS.setWidgetResizable(True)
    self.ResultS.setWidget(self.ResultW)
    self.ResultS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.ResultW.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    for ii, (ItemId, ItemName) in enumerate(data, 0):
        IndexL = QLabel(self.ResultW)
        NameB = QPushButton(self.ResultW)
        IndexL.setObjectName(f'IndexL{ii}')
        NameB.setObjectName(f'NameB{ii}')
        IndexL.setProperty('class', 'IndexL')
        NameB.setProperty('class', 'NameB')
        self.ResultL.addWidget(IndexL, ii, 0, 1, 40)
        self.ResultL.addWidget(NameB, ii, 40, 1, 60)
        IndexL.setAlignment(Qt.AlignCenter)
        IndexL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        NameB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        IndexL.setText(f'{ii+1}')
        NameB.setText(f'{ItemName}')
        NameB.clicked.connect(lambda _, dbi=ItemId: ListAddHandle(self, dbi))

def ListAddHandle(self, DBI):
    self.AddObjectData['NewObjectType'] = self.SortType
    self.AddObjectData['NewObjectId'] = DBI
    self.AddObjectToListF(self.AddObjectData)
    ReloadConfig(self)
    self.ListPage()

def ListDeleteObject(self, d):
    d['UserId'] = self.LoggedUserId
    self.DeleteObjectFromList(d)
    ReloadConfig(self)
    self.ListPage()

def GetIdByTypeInLists(lists, type_search):
    IdList = []
    for ListName, ListItems in lists.items():
        for SectionName, SectionItems in ListItems.items():
            for ObjectsItems in SectionItems:
                if ObjectsItems['type'] == type_search:
                    IdList.append(ObjectsItems['id'])
    return IdList