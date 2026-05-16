from typing import List, Dict, Any
from ..storage.campaign_repository import campaign_repository
from ..utils.id_generator import generate_id

class CampaignService:
    def create_campaign(self, data: Dict[str, Any]) -> Dict[str, Any]:
        campaign_id = generate_id("camp")
        data["id"] = campaign_id
        campaign_repository.create(campaign_id, data)
        return data

    def get_campaigns(self) -> List[Dict[str, Any]]:
        return campaign_repository.get_all()

    def get_campaign(self, campaign_id: str) -> Dict[str, Any]:
        return campaign_repository.get_by_id(campaign_id)

campaign_service_crud = CampaignService()
