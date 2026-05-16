import uuid
from fastapi import APIRouter, Depends
from ..schemas.main import SocialCampaignRequest, CopywritingRequest, BannerRequest, Job, JobStatus
from ..memory import jobs_db
from ..queue import add_to_queue
from ..middleware.auth import verify_token

router = APIRouter(prefix="/api/campaigns", tags=["Campaigns"])


@router.post("/social", response_model=Job)
async def create_social_campaign(
    request: SocialCampaignRequest,
    user=Depends(verify_token),
):
    job_id = str(uuid.uuid4())
    job = Job(id=job_id, type="social", status=JobStatus.PENDING)
    jobs_db[job_id] = job
    await add_to_queue("social", job_id, request.dict())
    return job


@router.post("/copy", response_model=Job)
async def create_copywriting(
    request: CopywritingRequest,
    user=Depends(verify_token),
):
    job_id = str(uuid.uuid4())
    job = Job(id=job_id, type="copy", status=JobStatus.PENDING)
    jobs_db[job_id] = job
    await add_to_queue("copy", job_id, request.dict())
    return job


@router.post("/banner", response_model=Job)
async def create_banner(
    request: BannerRequest,
    user=Depends(verify_token),
):
    job_id = str(uuid.uuid4())
    job = Job(id=job_id, type="banner", status=JobStatus.PENDING)
    jobs_db[job_id] = job
    await add_to_queue("banner", job_id, request.dict())
    return job
