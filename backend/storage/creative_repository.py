from typing import List, Optional, Dict, Any
from .memory_store import jobs_db

class CreativeRepository:
    """Uses jobs_db for storing creative outputs."""
    def get_by_id(self, creative_id: str) -> Optional[Dict[str, Any]]:
        return jobs_db.get(creative_id)

    def get_all(self) -> List[Dict[str, Any]]:
        return jobs_db.get_all()

    def create(self, creative_id: str, data: Dict[str, Any]) -> None:
        jobs_db.save(creative_id, data)

    def delete(self, creative_id: str) -> bool:
        return jobs_db.delete(creative_id)

creative_repository = CreativeRepository()
