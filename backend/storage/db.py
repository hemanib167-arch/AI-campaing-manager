import os
from typing import Dict, Any, List
from ..utils.file_utils import read_json_file, write_json_file
from ..observability.logger import get_logger

logger = get_logger(__name__)

# Base directory for data files
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

class JSONDatabase:
    """A simple JSON file-based database for persistence during the hackathon."""
    
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.file_path = os.path.join(DATA_DIR, f"{collection_name}.json")
        self._data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        return read_json_file(self.file_path, default={})

    def _save(self) -> None:
        write_json_file(self.file_path, self._data)

    def get(self, item_id: str) -> Any:
        return self._data.get(item_id)

    def get_all(self) -> List[Any]:
        return list(self._data.values())

    def save(self, item_id: str, item_data: Any) -> None:
        self._data[item_id] = item_data
        self._save()

    def delete(self, item_id: str) -> bool:
        if item_id in self._data:
            del self._data[item_id]
            self._save()
            return True
        return False
