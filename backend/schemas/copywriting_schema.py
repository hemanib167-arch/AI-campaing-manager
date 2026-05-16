from pydantic import BaseModel

class CopywritingRequest(BaseModel):
    channel: str
    brief: str
    tone: str = "professional"

class CopywritingResponse(BaseModel):
    copy: str
    cta: str
    word_count: int
