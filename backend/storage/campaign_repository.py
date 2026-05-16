from typing import List, Optional, Dict, Any
from .memory_store import campaigns_db

class CampaignRepository:
    def get_by_id(self, campaign_id: str) -> Optional[Dict[str, Any]]:
        return campaigns_db.get(campaign_id)

    def get_all(self) -> List[Dict[str, Any]]:
        return campaigns_db.get_all()

    def create(self, campaign_id: str, data: Dict[str, Any]) -> None:
        campaigns_db.save(campaign_id, data)

    def update(self, campaign_id: str, data: Dict[str, Any]) -> None:
        existing = campaigns_db.get(campaign_id)
        if existing:
            existing.update(data)
            campaigns_db.save(campaign_id, existing)

    def delete(self, campaign_id: str) -> bool:
        return campaigns_db.delete(campaign_id)

campaign_repository = CampaignRepository()
