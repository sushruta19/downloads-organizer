#!/usr/bin/env python3

from pathlib import Path
from typing import Dict, List
from utils import load_categories, categorize_file, move_file
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR:Path = Path(sys._MEIPASS)
else:
    BASE_DIR:Path = Path(__file__).resolve().parent 

CATEGORIES_FILE:Path = BASE_DIR / "categories.json"
DOWNLOADS_FOLDER:Path = Path.home() / "Documents" / "Testing"

FILE_CATEGORIES: Dict[str, List[str]] = load_categories(CATEGORIES_FILE)

def organize_downloads() -> None:
    print(f"Organizing files in: {DOWNLOADS_FOLDER}\n")
    count = 0
    for item in DOWNLOADS_FOLDER.iterdir():
        if item.is_file():
            category:str = categorize_file(item, FILE_CATEGORIES)
            dest_folder:Path = DOWNLOADS_FOLDER / category
            try:    
                move_file(item, dest_folder)
                count += 1
            except Exception as e:
                print(f"Could not move {item.name}: {e}")
    print(f"Organization complete! {count} files moved.")

if __name__ == "__main__":
    organize_downloads()
