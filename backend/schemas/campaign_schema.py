from pydantic import BaseModel
from typing import Optional, List

class CampaignSchema(BaseModel):
    id: Optional[str] = None
    project_id: str
    name: str
    type: str # sale, awareness, new_route
    status: str = "draft"
