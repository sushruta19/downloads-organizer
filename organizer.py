from pathlib import Path
from typing import Dict, List
from utils import load_categories, categorize_file, move_file

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
            move_file(item, dest_folder)
            count += 1
    print(f"Organization complete! {count} files moved.")

if __name__ == "__main__":
    organize_downloads()
