from pydantic import BaseModel
from typing import Optional

class ProjectSchema(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    status: str = "active"
