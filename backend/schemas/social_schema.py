from pydantic import BaseModel
from typing import List, Optional

class SocialCampaignRequest(BaseModel):
    campaign_type: str
    description: str

class SocialPlatformContent(BaseModel):
    caption: str
    hashtags: List[str]

class SocialCampaignResponse(BaseModel):
    instagram: SocialPlatformContent
    facebook: SocialPlatformContent
    linkedin: SocialPlatformContent
