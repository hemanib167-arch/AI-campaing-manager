from typing import List, Optional, Dict, Any
from .db import JSONDatabase

analytics_db = JSONDatabase("analytics")

class AnalyticsRepository:
    def get_by_id(self, event_id: str) -> Optional[Dict[str, Any]]:
        return analytics_db.get(event_id)

    def get_all(self) -> List[Dict[str, Any]]:
        return analytics_db.get_all()

    def create(self, event_id: str, data: Dict[str, Any]) -> None:
        analytics_db.save(event_id, data)

analytics_repository = AnalyticsRepository()
