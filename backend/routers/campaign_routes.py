from fastapi import APIRouter
from typing import List
from ..schemas.campaign_schema import CampaignSchema
from ..core.campaign_service import campaign_service_crud

router = APIRouter(prefix="/campaign_entities", tags=["Campaign Entities"])

@router.post("/", response_model=CampaignSchema)
def create_campaign(request: CampaignSchema):
    return campaign_service_crud.create_campaign(request.dict(exclude_unset=True))

@router.get("/", response_model=List[CampaignSchema])
def get_campaigns():
    return campaign_service_crud.get_campaigns()
