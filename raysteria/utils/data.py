import json
from pathlib import Path


def load_from_json(file_path: str | Path) -> dict:
    return json.load(open(file_path, encoding="utf-8"))
