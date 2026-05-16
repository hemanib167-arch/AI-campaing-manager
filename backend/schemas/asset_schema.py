from pydantic import BaseModel
from typing import Optional

class AssetSchema(BaseModel):
    id: Optional[str] = None
    campaign_id: Optional[str] = None
    type: str # image, copy, social_post
    content_url: Optional[str] = None
    content_text: Optional[str] = None
