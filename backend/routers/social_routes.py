from fastapi import APIRouter, Depends
from ..schemas.social_schema import SocialCampaignRequest
from ..schemas.job_schema import JobSchema, JobStatus
from ..queue.job_queue import add_to_queue
from ..utils.id_generator import generate_id
from ..storage.memory_store import jobs_db

router = APIRouter(prefix="/social", tags=["Social Campaigns"])

@router.post("/", response_model=JobSchema)
async def create_social_campaign(request: SocialCampaignRequest):
    job_id = generate_id("social")
    job = JobSchema(id=job_id, type="social", status=JobStatus.PENDING)
    jobs_db.save(job_id, job.dict())
    
    await add_to_queue("social", job_id, request.dict())
    return job
