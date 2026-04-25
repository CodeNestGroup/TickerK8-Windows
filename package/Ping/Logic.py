# Ping/Logic.py

import requests
from PySide6.QtCore import QObject, QThread, Signal, Slot

class PingO(QObject):
    Status = Signal(bool)
    def __init__(self):
        super().__init__()
        self._running = True

    @Slot()
    def run(self):
        while self._running:
            try:
                requests.get("https://www.google.com", timeout=3)
                self.Status.emit(True)
            except:
                self.Status.emit(False)
            for _ in range(50):
                if not self._running:
                    return
                QThread.msleep(100)

    @Slot()
    def stop(self):
        self._running = False