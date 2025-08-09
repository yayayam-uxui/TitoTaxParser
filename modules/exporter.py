from pathlib import Path
from typing import List, Tuple
import pandas as pd

def export_rows_to_excel(rows: List[Tuple[str, str, str, str]], base_folder: Path) -> Path:
    df = pd.DataFrame(rows, columns=["file_name", "doc_type", "key", "value"])
    out_dir = Path(base_folder) / "data"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "export.xlsx"
    df.to_excel(out_path, index=False)
    return out_path
