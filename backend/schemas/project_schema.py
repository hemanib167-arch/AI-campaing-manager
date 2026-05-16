from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str = Field(default="", max_length=1000)


class Project(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
