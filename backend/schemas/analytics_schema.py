from pydantic import BaseModel
from typing import Dict, Any, Optional

class AnalyticsEventSchema(BaseModel):
    id: Optional[str] = None
    type: str
    timestamp: Optional[str] = None
    metadata: Dict[str, Any]
