from fastapi import APIRouter
from typing import List
from ..schemas.analytics_schema import AnalyticsEventSchema
from ..core.analytics_service import analytics_service_crud

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/", response_model=List[AnalyticsEventSchema])
def get_analytics():
    return analytics_service_crud.get_all_events()
