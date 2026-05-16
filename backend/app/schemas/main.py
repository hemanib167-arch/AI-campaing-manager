from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum

class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class CampaignType(str, Enum):
    SALE = "sale"
    NEW_ROUTE = "new_route"
    BRAND_AWARENESS = "brand_awareness"
    FESTIVE = "festive"

# --- Social Media ---
class SocialCampaignRequest(BaseModel):
    campaign_type: CampaignType
    description: str

class SocialPlatformContent(BaseModel):
    caption: str
    hashtags: List[str]

class SocialCampaignResponse(BaseModel):
    instagram: SocialPlatformContent
    facebook: SocialPlatformContent
    linkedin: SocialPlatformContent

# --- Copywriting ---
class CopywritingRequest(BaseModel):
    channel: str
    brief: str
    tone: str = "professional"

class CopywritingResponse(BaseModel):
    copy: str
    cta: str
    word_count: int

# --- Banner / Image ---
class BannerRequest(BaseModel):
    aspect_ratio: str = "16:9"
    resolution: str = "1024x1024"
    brief: str

class BannerResponse(BaseModel):
    dalle_prompt: str
    text_overlay_suggestion: str
    mood: str
    image_url: Optional[str] = None

# --- Job/Task Wrapper ---
class Job(BaseModel):
    id: str
    type: str # social, copy, banner
    status: JobStatus
    result: Optional[Dict] = None
    error: Optional[str] = None
