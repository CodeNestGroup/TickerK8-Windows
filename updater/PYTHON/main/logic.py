""" Import packages """
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
""" Import PyQT5 packages """
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton
)
from PyQt5.QtCore import (
    QUrl,
    QThread,
    pyqtSignal
)
from PyQt5.QtGui import (
    QDesktopServices
)
""" Import main modules """
from .ui import (
    main_no_connect_ui,
    main_no_connect_retranslate,
    main_connect_ui,
    main_connect_retranslate,
    none_update_ui,
    none_update_retranslate,
    new_update_ui,
    new_update_retranslate,
    start_update_ui,
    start_update_retranslate
)
#______________________________________________________________________________________________________________________

def open_link(u):
    try:
        QDesktopServices.openUrl(QUrl(u))
    except:
        pass
#______________________________________________________________________________________________________________________

def reset(self):
    """ Reset """
    if self.info_label and not self.controller_download_thread:
        self.info_label.deleteLater()
        self.info_label = None 
    if self.download_button:
        self.download_button.deleteLater()
        self.download_button = None
    if self.open_button:
        self.open_button.deleteLater()
        self.open_button = None

def main_no_connect(self):
    reset(self)
    if not self.controller_download_thread:
        main_no_connect_ui(self)
        main_no_connect_retranslate(self)
    """ Call functions """
    self.changelog_widget.no_connection()

def main_connect(self):
    reset(self)
    self.get_releases_thread = get_releases()
    if not self.controller_download_thread:
        main_connect_ui(self)
        main_connect_retranslate(self)
        self.get_releases_thread.finished.connect(lambda release_data: check_update(self, release_data))
    """ Call functtions """
    self.changelog_widget.loading()
    """ Connect functions """
    self.get_releases_thread.finished.connect(self.changelog_widget.connection)
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.quit())
    self.get_releases_thread.finished.connect(lambda: self.get_releases_thread.deleteLater())
    self.get_releases_thread.start()
#______________________________________________________________________________________________________________________

class get_releases(QThread):
        finished = pyqtSignal(list)
        def __init__(self):
            super().__init__()
            self.start()

        def run(self):
            release = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases')
            self.finished.emit(json.loads(release.read().decode()))
#______________________________________________________________________________________________________________________

def check_update(self, release_data):
    g_v = release_data[0]['published_at']
    l_v = json.load(open(self.main_path+'/CONFIG/GLOBAL/changelog.json', 'r'))['published_at']
    g_t = datetime.fromisoformat(g_v.replace("Z", "+00:00"))
    l_t = datetime.fromisoformat(l_v.replace("Z", "+00:00"))
    if g_t <= l_t:
        none_update(self)
    elif g_t > l_t:
        new_update(self)

def none_update(self):
    reset(self)
    none_update_ui(self)
    none_update_retranslate(self)
    """ Connect functtions """
    self.open_button.clicked.connect(lambda: open_main_app(self))

def open_main_app(self):
    try:
        subprocess.Popen(["python", "__core__.py"])
        sys.exit(0)
    except:
        pass

def new_update(self):
    reset(self)
    new_update_ui(self)
    new_update_retranslate(self)
    """ Connect functtions """
    self.download_button.clicked.connect(lambda: start_update(self))

def start_update(self):
    reset(self)
    start_update_ui(self)
    start_update_retranslate(self)
    """ Call functions """
    self.controller_download_thread = controller_download()
    self.controller_download_thread.progress.connect(self.info_label.setText)
    self.controller_download_thread.start()
#______________________________________________________________________________________________________________________

class controller_download(QThread):
    progress = pyqtSignal(str)
    """
    2 - Creating backup
    3 - Downloading
    4 - Un zip 
    5 - Check update compatibility
    6 - Install 
    7 - Delete backup 
    8 - Error
    0 - No connection  

    Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self):
        super().__init__()
        self.backup_path = str(pathlib.Path(__file__).resolve().parents[4])
        self.main_path = str(pathlib.Path(__file__).resolve().parents[3])
        self.capacity = self.set_speed(json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))['capacity'])
        self.update_folder = None
        self.update_json_file_list = None
        self.zip_buffer = io.BytesIO()
        self.t = json.load(open(self.main_path+'/updater/CONFIG/main/translate.json', 'r'))
        self.l = json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))['language']

    def run(self):
        self.backup()
        time.sleep(0.2)
        self.download()
        time.sleep(0.2)
        self.un_zip()
        time.sleep(0.2)
        self.update_compatibility()
        time.sleep(0.2)
        self.install()
        time.sleep(0.2)
        self.delete_backup()
        time.sleep(0.2)
        self.restart()

    def backup(self):
        try:
            self.progress.emit(self.t['info_label'][2][self.l])
            n = self.main_path[-(len(self.main_path)-len(self.backup_path)):]
            b = self.backup_path+f'/.backup{n}'
            m = self.backup_path+n
            if os.path.exists(b):
                shutil.rmtree(b)
            shutil.copytree(m, b)
        except:
            self.progress.emit(self.t['info_label'][8][self.l])
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')

    def download(self):
        try:
            self.progress.emit(self.t['info_label'][3][self.l])
            r = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases/latest')
            u = json.loads(r.read().decode())['zipball_url']
            c = 8192
            d = 0
            h = {}
            while True:
                try:
                    if d > 0:
                        h['Range'] = f'bytes={d}-'
                    r = requests.get(u, stream=True, timeout=10, headers=h)
                    r.raise_for_status()
                    chunk_generator = r.iter_content(chunk_size=c)
                    for chunk in chunk_generator: 
                        if not chunk:
                            continue
                        self.zip_buffer.write(chunk)
                        d = len(chunk)
                        time.sleep(len(chunk) / self.capacity*1024)
                    break
                except (requests.RequestException, ConnectionError, TimeoutError):
                    self.progress.emit(self.t['info_label'][0][self.l])
                    time.sleep(3)
        except Exception:
            self.progress.emit(self.t['info_label'][8][self.l])
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')
            if self.zip_buffer:
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)

    def un_zip(self):
        try:
            self.progress.emit(self.t['info_label'][4][self.l])
            with zipfile.ZipFile(self.zip_buffer, 'r') as zip_ref:
                self.update_folder = f'/{zip_ref.namelist()[0]}'
                l = zip_ref.namelist()
                t = len(l)
                for file in l:
                    zip_ref.extract(file, self.backup_path)
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
        except:
            self.progress.emit(self.t['info_label'][8][self.l])
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')
            if self.zip_buffer:
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
            if os.path.exists(self.backup_path+self.update_folder):
                shutil.rmtree(self.backup_path+self.update_folder)

    def update_compatibility(self):
        try:
            self.progress.emit(self.t['info_label'][5][self.l])
            u = json.load(open(self.backup_path+self.update_folder+'updater/CONFIG/GLOBAL/app_file_list.json', 'r'))
            t = len(u)
            for file, check_sum in u.items():
                if os.path.exists(self.backup_path+self.update_folder+file):
                    if check_sum != 'config':
                        if check_sum != self.calculate_sha256(self.backup_path+self.update_folder+file):
                            raise
        except:
            self.progress.emit(self.t['info_label'][8][self.l])
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')
            if os.path.exists(self.backup_path+self.update_folder): 
                shutil.rmtree(self.backup_path+self.update_folder)

    def install(self):
        try:
            self.progress.emit(self.t['info_label'][6][self.l]) 
            n = self.main_path[-(len(self.main_path)-len(self.backup_path)):]
            m = self.main_path
            b = self.backup_path
            u = b+self.update_folder
            s1 = b+f'/.backup{n}/updater/CONFIG/GLOBAL/global_config.json'
            d1 = u+'updater/CONFIG/GLOBAL/global_config.json'
            shutil.copy2(s1, d1)
            for r, d, f in os.walk(u):
                rp = os.path.relpath(r, u)
                t = os.path.join(m, rp)
                os.makedirs(t, exist_ok=True)
                for file in f:
                    src_file = os.path.join(r, file)
                    dst_file = os.path.join(t, file)
                    shutil.copy2(src_file, dst_file)
        except:
            self.progress.emit(self.t['info_label'][8][self.l])
            if os.path.exists(self.backup_path+'/.backup'):
                self.restore_backup()
            if os.path.exists(self.backup_path+self.update_folder): 
                shutil.rmtree(self.backup_path+self.update_folder)

    def delete_backup(self):
        self.progress.emit(self.t['info_label'][7][self.l])
        if os.path.exists(self.backup_path+self.update_folder):
            shutil.rmtree(self.backup_path+self.update_folder)
        if os.path.exists(self.backup_path+'/.backup'):
            shutil.rmtree(self.backup_path+'/.backup')

    def restart(self):
        subprocess.Popen(['/bin/bash', self.main_path+'/Launcher.sh'])
        sys.exit(0)

    def restore_backup(self):
        n = self.main_path[-(len(self.main_path)-len(self.backup_path)):]
        b = self.backup_path+f'/.backup{n}'
        m = self.backup_path+n
        if os.path.exists(m):
            shutil.rmtree(m)
        shutil.copytree(b, m)

    def calculate_sha256(self, file):
        sha256 = hashlib.sha256()
        f = open(file, "rb")
        while chunk := f.read(4096):
            sha256.update(chunk)
        return sha256.hexdigest()

    def set_speed(self, index):
        capacity = 0 
        if index == 0:
            capacity = 500
        elif index == 1:
            capacity = 1000
        elif index == 2:
            capacity = 2000
        elif index== 3:
            capacity = 5000
        elif index == 4:
            capacity = float('inf')
        return capacity
#______________________________________________________________________________________________________________________
