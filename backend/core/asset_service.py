from typing import List, Dict, Any
from ..storage.asset_repository import asset_repository
from ..utils.id_generator import generate_id

class AssetService:
    def create_asset(self, data: Dict[str, Any]) -> Dict[str, Any]:
        asset_id = generate_id("asset")
        data["id"] = asset_id
        asset_repository.create(asset_id, data)
        return data

    def get_assets(self) -> List[Dict[str, Any]]:
        return asset_repository.get_all()

    def get_asset(self, asset_id: str) -> Dict[str, Any]:
        return asset_repository.get_by_id(asset_id)

asset_service_crud = AssetService()
