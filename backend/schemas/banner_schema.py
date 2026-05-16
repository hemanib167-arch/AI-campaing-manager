from pydantic import BaseModel
from typing import Optional

class BannerRequest(BaseModel):
    aspect_ratio: str = "16:9"
    resolution: str = "1024x1024"
    brief: str

class BannerResponse(BaseModel):
    dalle_prompt: str
    text_overlay_suggestion: str
    mood: str
    image_url: Optional[str] = None
