from typing import Dict, List, Tuple
from pathlib import Path

# Output rows schema: List[Tuple[file_name, doc_type, key, value]]
def parse_extracted(extracted: Dict[Path, str]) -> List[Tuple[str, str, str, str]]:
    rows: List[Tuple[str, str, str, str]] = []
    for path, text in extracted.items():
        # Stub logic: detect doc type by filename
        name = path.name
        lower = name.lower()
        if "w2" in lower:
            doc_type = "W-2"
        elif "1099" in lower:
            doc_type = "1099"
        elif "k1" in lower:
            doc_type = "K-1"
        else:
            doc_type = "GENERIC"

        # Stub: produce 2 fake fields (replace with real regex rules)
        rows.append((name, doc_type, "field_1", "value_1"))
        rows.append((name, doc_type, "field_2", "value_2"))
    return rows
