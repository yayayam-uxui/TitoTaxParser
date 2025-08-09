from pathlib import Path
from typing import Dict, List

# Placeholder: returns string “content” per file (later replace with AWS/Google/Tesseract)
def extract_batch(files: List[Path]) -> Dict[Path, str]:
    out: Dict[Path, str] = {}
    for f in files:
        # For now, we just store a stub; later: real OCR / Excel parsing.
        out[f] = f"EXTRACTED_TEXT_STUB from {f.name}"
    return out
