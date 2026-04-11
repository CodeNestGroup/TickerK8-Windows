import sys
from pathlib import Path

def ResourcePath(i:int) -> str:
    if hasattr(sys, "_MEIPASS"):
        b = Path(sys._MEIPASS)
    else:
        b = Path(__file__).resolve()
    for _ in range(i+1):
        b = b.parent
    return str(b)