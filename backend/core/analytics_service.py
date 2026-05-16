from typing import List, Dict, Any
from ..storage.analytics_repository import analytics_repository
from ..utils.id_generator import generate_id
from ..utils.time_utils import get_current_timestamp

class AnalyticsService:
    def track_event(self, event_type: str, metadata: Dict[str, Any]) -> None:
        event_id = generate_id("evt")
        event_data = {
            "id": event_id,
            "type": event_type,
            "timestamp": get_current_timestamp(),
            "metadata": metadata
        }
        analytics_repository.create(event_id, event_data)

    def get_all_events(self) -> List[Dict[str, Any]]:
        return analytics_repository.get_all()

analytics_service_crud = AnalyticsService()
