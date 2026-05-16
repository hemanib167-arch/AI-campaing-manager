from typing import List, Optional, Dict, Any
from .memory_store import assets_db

class AssetRepository:
    def get_by_id(self, asset_id: str) -> Optional[Dict[str, Any]]:
        return assets_db.get(asset_id)

    def get_all(self) -> List[Dict[str, Any]]:
        return assets_db.get_all()

    def create(self, asset_id: str, data: Dict[str, Any]) -> None:
        assets_db.save(asset_id, data)

    def delete(self, asset_id: str) -> bool:
        return assets_db.delete(asset_id)

asset_repository = AssetRepository()
