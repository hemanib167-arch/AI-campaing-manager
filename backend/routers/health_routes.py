from fastapi import APIRouter
from ..utils.time_utils import get_current_timestamp

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "timestamp": get_current_timestamp(),
        "version": "2.0.0-hackathon"
    }
