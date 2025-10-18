import shutil
from pathlib import Path
import json
import magic
from typing import Dict, List, Optional

def load_categories(json_path:Path) -> Dict[str, List[str]]:
    with open(json_path, 'r') as f:
        return json.load(f)

# MIME stands for Multipurpose Internet Mail Extensions.
def detect_file_type(file_path: Path) -> Optional[str]:
    try:
        mime_type: str = magic.from_file(str(file_path), mime=True)
        return mime_type
    except Exception as e:
        return None

def categorize_file(file_path: Path, categories: Dict[str, List[str]]) -> str:
    ext: str = file_path.suffix.lower()

    if ext:
        for category, extension in categories.items():
            if ext in extension:
                return category
    
    mime = detect_file_type(file_path)
    if mime:
        if "image" in mime:
            return "Images"
        elif "video" in mime:
            return "Videos"
        elif "audio" in mime:
            return "Music"
        elif "text" in mime:
            return "Documents"
        elif "application/x-executable" in mime:
            return "Executables"
    return "Others"


def move_file(src: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok = True)

    stem: str = src.stem #name of file without extension
    suffix: str = src.suffix #extension of file
    counter = 0

    dest_path: Path = dest / src.name

    # if file already exists
    while dest_path.exists():
        counter += 1
        new_name = f"{stem}_{counter}{suffix}" if suffix else f"{stem}_{counter}"
        dest_path: Path = dest / new_name
    shutil.move(str(src), str(dest_path))



    
