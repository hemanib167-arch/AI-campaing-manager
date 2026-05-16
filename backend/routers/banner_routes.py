from fastapi import APIRouter
from ..schemas.banner_schema import BannerRequest
from ..schemas.job_schema import JobSchema, JobStatus
from ..queue.job_queue import add_to_queue
from ..utils.id_generator import generate_id
from ..storage.memory_store import jobs_db

router = APIRouter(prefix="/banner", tags=["Banner Generation"])

@router.post("/", response_model=JobSchema)
async def create_banner(request: BannerRequest):
    job_id = generate_id("banner")
    job = JobSchema(id=job_id, type="banner", status=JobStatus.PENDING)
    jobs_db.save(job_id, job.dict())
    
    await add_to_queue("banner", job_id, request.dict())
    return job
