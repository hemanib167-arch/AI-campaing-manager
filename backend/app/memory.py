from typing import Dict, Any
from .schemas.main import Job

# In-memory stores
jobs_db: Dict[str, Job] = {}
users_db: Dict[str, Dict[str, Any]] = {}
sessions_db: Dict[str, Any] = {}

def get_job(job_id: str) -> Job:
    return jobs_db.get(job_id)

def update_job(job_id: str, **kwargs):
    if job_id in jobs_db:
        job = jobs_db[job_id]
        for key, value in kwargs.items():
            setattr(job, key, value)
        jobs_db[job_id] = job
