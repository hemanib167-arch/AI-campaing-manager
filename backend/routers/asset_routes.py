from fastapi import APIRouter
from typing import List
from ..schemas.asset_schema import AssetSchema
from ..core.asset_service import asset_service_crud

router = APIRouter(prefix="/assets", tags=["Assets"])

@router.post("/", response_model=AssetSchema)
def create_asset(request: AssetSchema):
    return asset_service_crud.create_asset(request.dict(exclude_unset=True))

@router.get("/", response_model=List[AssetSchema])
def get_assets():
    return asset_service_crud.get_assets()
