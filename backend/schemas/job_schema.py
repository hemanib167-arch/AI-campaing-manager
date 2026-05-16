from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum

class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class JobSchema(BaseModel):
    id: str
    type: str
    status: JobStatus
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
