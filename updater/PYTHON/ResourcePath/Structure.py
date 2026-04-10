import sys
from pathlib import Path

def ResourcePath(i:int) -> str:
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return str(Path(__file__).resolve().parents[i])