import sys
from pathlib import Path as SysPath

def Path() -> str:
    if hasattr(sys, "_MEIPASS"):
        b = SysPath(sys._MEIPASS)
    else:
        b = SysPath(__file__).resolve()
        for _ in range(3):
            b = b.parent
    return str(b)