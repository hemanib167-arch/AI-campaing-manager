from fastapi import APIRouter
from ..schemas.copywriting_schema import CopywritingRequest
from ..schemas.job_schema import JobSchema, JobStatus
from ..queue.job_queue import add_to_queue
from ..utils.id_generator import generate_id
from ..storage.memory_store import jobs_db

router = APIRouter(prefix="/copywriting", tags=["Copywriting"])

@router.post("/", response_model=JobSchema)
async def create_copywriting(request: CopywritingRequest):
    job_id = generate_id("copy")
    job = JobSchema(id=job_id, type="copy", status=JobStatus.PENDING)
    jobs_db.save(job_id, job.dict())
    
    await add_to_queue("copy", job_id, request.dict())
    return job
