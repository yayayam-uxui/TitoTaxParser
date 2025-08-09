from pathlib import Path
from typing import List

SUPPORTED = {".pdf", ".xlsx", ".xls", ".csv", ".jpg", ".jpeg", ".png", ".tif", ".tiff"}

def list_supported_files(folder: Path) -> List[Path]:
    folder = Path(folder)
    files: List[Path] = []
    for p in folder.rglob("*"):
        if p.is_file() and p.suffix.lower() in SUPPORTED:
            files.append(p)
    return sorted(files)

def detect_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return "PDF"
    if ext in {".xlsx", ".xls"}:
        return "Excel"
    if ext == ".csv":
        return "CSV"
    if ext in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}:
        return "Image"
    return ext.upper()[1:]
