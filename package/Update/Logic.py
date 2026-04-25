#   --- Import ---
import json 
import sys
import os
import subprocess
import pathlib
import io
import shutil
import zipfile
import urllib.request
import requests
import hashlib
import time
from datetime import datetime
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy
)
from PySide6.QtCore import (
    QUrl,
    QThread,
    Signal
)
from PySide6.QtGui import (
    QDesktopServices
)

def UpdateCloseThreads(self):
    try:
        if self.PingT:
            self.PingO.stop()
            self.PingT.quit()
            self.PingT.wait()
            self.PingT.deleteLater()
            self.PingT = None
        if self.ChangelogDotsT:
            self.ChangelogDotsT.stop()
            self.ChangelogDotsT.wait()
            self.ChangelogDotsT.deleteLater()
            self.ChangelogDotsT = None
        if self.GetReleasesT:
            self.GetReleasesT.IsRunning = False
            self.GetReleasesT.quit()
            self.GetReleasesT.wait()
            self.GetReleasesT.deleteLater()
            self.GetReleasesT = None
    except Exception as e:
        pass

def CloseGetReleasesThread(self):
    self.GetReleasesT.quit()
    self.GetReleasesT.wait()
    self.GetReleasesT.deleteLater()
    self.GetReleasesT = None
    self.ChangelogDotsT.stop()
    self.ChangelogDotsT.deleteLater()
    self.ChangelogDotsT = None

def UpdateSettingsOpenHandler(self):
    UpdateCloseThreads(self)
    self.UpdateSettingsOpenF()

def UpdateChangelogOpenHandler(self, d):
    UpdateCloseThreads(self)
    self.UpdateChangelogOpenF(d)

def LoginOpenHandler(self):
    UpdateCloseThreads(self)
    self.LoginOpenF()

def OpenLink(u):
    try:
        QDesktopServices.openUrl(QUrl(u))
    except:
        pass

def DotsUpdate(self):
    t = self.ChaneglogDotsL.text()
    l = len(t)
    if l < 14:
        self.ChaneglogDotsL.setText(t+'.')
    else:
        self.ChaneglogDotsL.setText('.')

def ResetFuncInfo(self):
    if self.FuncB:
        self.FuncB.deleteLater()
        self.FuncB = None
    if self.InfoL:
        self.InfoL.deleteLater()
        self.InfoL = None

class GetReleasesT(QThread):
        List = Signal(list)
        Finished = Signal()
        def __init__(self):
            super().__init__()
            self.IsRunning = True
            self.start()

        def run(self):
            while self.IsRunning:
                try:
                    r = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases')
                    self.List.emit(json.loads(r.read().decode()))
                    self.stop()
                    break
                except Exception as e:
                    pass
        
        def stop(self):
            self.IsRunning = False
            self.Finished.emit()

def ChangelogConnectionSetup(self, r):
    GithubVersion = r[0]['published_at']
    LocalVersion = json.load(open(self.Path+'/assets/JSON/Changelog.json', 'r', encoding='utf-8'))['published_at']
    GithubTime = datetime.fromisoformat(GithubVersion.replace("Z", "+00:00"))
    LocalTime = datetime.fromisoformat(LocalVersion.replace("Z", "+00:00"))
    for i, c in enumerate(r, start=0):
        ChangelogB = QPushButton(self.ChangelogW)
        ChangelogB.clicked.connect(lambda _, cc=c: UpdateChangelogOpenHandler(self, cc))
        ChangelogB.setObjectName(f'ChangelogB{i}')
        ChangelogB.setProperty('class', 'ChangelogB')
        self.ChangelogL.addWidget(ChangelogB)
        ChangelogB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        ChangelogB.setText(c['name'])
    ResetFuncInfo(self)
    self.FuncB = QPushButton(self)
    self.FuncB.setObjectName('FuncB')
    self.FuncB.setProperty('class', 'Button')
    self.Layout.addWidget(self.FuncB, 91, 51, 9, 48)
    self.FuncB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/JSON/UpdateTranslate.json', 'r', encoding='utf-8'))
    if GithubTime <= LocalTime:
        self.FuncB.clicked.connect(lambda: LoginOpenHandler(self))
        self.FuncB.setText(t['FuncB'][0][l])
    elif GithubTime > LocalTime:
        self.FuncB.clicked.connect(lambda: StartUpdate(self))
        self.FuncB.setText(t['FuncB'][1][l])

def StartUpdate(self):
    ResetFuncInfo(self)
    self.ControllerDownloadT = ControllerDownload(self)
    self.ControllerDownloadT.Progress.connect(self.InfoL.setText)
    self.ControllerDownloadT.start()

#   --- ControllerDownload ---

class ControllerDownload(QThread):
    Progress = Signal(str)
    def __init__(self, Parent):
        super().__init__(Parent)
        self.Parent = Parent
        self.Path = Parent.Path
        self.Language = Parent.Language
        self.Translate = json.load(
            open(self.Path + '/assets/JSON/UpdateTranslate.json', 'r', encoding='utf-8')
        )
        self.CurrentBin = sys.executable
        self.WorkDir = os.path.join(os.path.expanduser("~"), ".ticker_update")
        os.makedirs(self.WorkDir, exist_ok=True)
        self.NewBin = os.path.join(self.WorkDir, "new_binary")
        self.BackupBin = self.CurrentBin + ".bak"

    def run(self):
        if not self.Download():
            return
        time.sleep(0.2)
        if not self.Backup():
            return
        time.sleep(0.2)
        if not self.Install():
            return
        time.sleep(0.2)
        self.Restart()

    def Download(self):
        try:
            self.Progress.emit(self.Translate['InfoL'][3][self.Language])
            Api = "https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases/latest"
            R = requests.get(Api, timeout=10)
            R.raise_for_status()
            Data = R.json()
            Url = Data["assets"][0]["browser_download_url"]

            with requests.get(Url, stream=True, timeout=15) as R:
                R.raise_for_status()

                with open(self.NewBin, "wb") as F:
                    for Chunk in R.iter_content(chunk_size=8192):
                        if Chunk:
                            F.write(Chunk)

            os.chmod(self.NewBin, 0o755)

            return True

        except Exception:
            self.Progress.emit(self.Translate['InfoL'][8][self.Language])
            return False

    def Backup(self):
        try:
            self.Progress.emit(self.Translate['InfoL'][2][self.Language])
            if os.path.exists(self.BackupBin):
                os.remove(self.BackupBin)
            shutil.copy2(self.CurrentBin, self.BackupBin)
            return True

        except Exception:
            self.Progress.emit(self.Translate['InfoL'][8][self.Language])
            return False

    def Install(self):
        try:
            self.Progress.emit(self.Translate['InfoL'][6][self.Language])
            os.replace(self.NewBin, self.CurrentBin)
            return True

        except Exception:
            self.Progress.emit(self.Translate['InfoL'][8][self.Language])
            self.Rollback()
            return False

    def Rollback(self):
        try:
            if os.path.exists(self.BackupBin):
                os.replace(self.BackupBin, self.CurrentBin)
        except:
            pass

    def Restart(self):
        try:
            self.Progress.emit(self.Translate['InfoL'][7][self.Language])
            subprocess.Popen([self.CurrentBin])
        finally:
            sys.exit(0)

    def CalculateSha256(self, File):
        Sha256 = hashlib.sha256()
        with open(File, "rb") as F:
            for Chunk in iter(lambda: F.read(4096), b""):
                Sha256.update(Chunk)
        return Sha256.hexdigest()