from fastapi import APIRouter, HTTPException
from ..storage.memory_store import jobs_db
from ..schemas.job_schema import JobSchema

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/{job_id}", response_model=JobSchema)
async def get_job(job_id: str):
    job = jobs_db.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
