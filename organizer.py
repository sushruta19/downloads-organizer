#!/usr/bin/env python3

from pathlib import Path
from typing import Dict, List, Optional
from utils import load_categories, categorize_file, move_file
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR:Path = Path(sys._MEIPASS)
else:
    BASE_DIR:Path = Path(__file__).resolve().parent 

CATEGORIES_FILE:Path = BASE_DIR / "categories.json"
FILE_CATEGORIES: Dict[str, List[str]] = load_categories(CATEGORIES_FILE)

def organize_downloads(target_dir: Optional[Path] = None) -> None:
    if target_dir is None:
        return
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"❌ Error: {target_dir} is not a valid directory.")
        return
    
    DOWNLOADS_FOLDER:Path = target_dir
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
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1]).expanduser().resolve()
        organize_downloads(input_path)
    else:
        print("Give Location")
        exit(1)
