#!/usr/bin/env python3
import os
import json
import hashlib

# Skrypt zakładamy, że jest w katalogu TICKERK8-LINUX
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "updater", "CONFIG", "GLOBAL", "app_file_list.json")

def sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

if not os.path.exists(CONFIG_PATH):
    print(f"Nie znaleziono pliku JSON: {CONFIG_PATH}")
    exit(1)

with open(CONFIG_PATH, "r") as f:
    files = json.load(f)

print("=== SPRAWDZANIE PLIKÓW ===")

for file, saved_hash in files.items():
    # Usuwamy początkowe '/' w JSON-ie i łączymy z BASE_DIR
    path = os.path.join(BASE_DIR, file.lstrip("/"))

    if not os.path.exists(path):
        print(f"[BRAK] {file}")
        continue

    if saved_hash == "config":
        continue

    real_hash = sha256(path)
    if not saved_hash:
        print(f"[PUSTE] {file} -> {real_hash}")
    elif saved_hash != real_hash:
        print(f"[NIEZGODNE] {file}")
        print(f"  zapisane: {saved_hash}")
        print(f"  aktualne: {real_hash}")

print("=== KONIEC ===")