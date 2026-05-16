from typing import Dict, Any
from .db import JSONDatabase

# We initialize the JSON DB collections here
jobs_db = JSONDatabase("jobs")
campaigns_db = JSONDatabase("campaigns")
projects_db = JSONDatabase("projects")
assets_db = JSONDatabase("assets")

# Global functions for backwards compatibility with the earlier simple memory store
def get_job(job_id: str) -> Any:
    return jobs_db.get(job_id)

def update_job(job_id: str, **kwargs) -> None:
    job = jobs_db.get(job_id)
    if job:
        for key, value in kwargs.items():
            job[key] = value
        jobs_db.save(job_id, job)
