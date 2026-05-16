from fastapi import APIRouter
from ..memory import get_job
from ..schemas.main import Job
from fastapi import HTTPException

router = APIRouter(prefix="/api/jobs", tags=["Jobs"])


@router.get("/{job_id}", response_model=Job)
async def get_job_status(job_id: str):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
