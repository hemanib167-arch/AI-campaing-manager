import json
import os
from typing import Any, Dict

def ensure_directory_exists(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def read_json_file(path: str, default: Any = None) -> Any:
    if not os.path.exists(path):
        return default if default is not None else {}
    with open(path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default if default is not None else {}

def write_json_file(path: str, data: Any) -> None:
    ensure_directory_exists(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
