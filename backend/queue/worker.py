import asyncio
from typing import Dict, Any
from .job_queue import queues
from ..storage.memory_store import update_job
from ..core.social_service import social_service
from ..core.copywriting_service import copywriting_service
from ..core.banner_service import banner_service
from ..observability.logger import get_logger

logger = get_logger(__name__)

MAX_RETRIES = 3
CONCURRENT_SLOTS = 3

async def process_job(job_id: str, job_type: str, payload: Dict[str, Any], attempt: int = 1):
    try:
        update_job(job_id, status="processing")
        
        if job_type == "social":
            result = await social_service.generate(payload)
        elif job_type == "copy":
            result = await copywriting_service.generate(payload)
        elif job_type == "banner":
            result = await banner_service.generate(payload)
        else:
            raise ValueError(f"Unknown job type: {job_type}")

        update_job(job_id, status="completed", result=result)
        logger.info(f"[{job_type}] Job {job_id} completed on attempt {attempt}.")

    except Exception as exc:
        logger.warning(f"[{job_type}] Job {job_id} failed (attempt {attempt}): {exc}")
        if attempt < MAX_RETRIES:
            await asyncio.sleep(1.5 ** attempt)
            await process_job(job_id, job_type, payload, attempt + 1)
        else:
            update_job(job_id, status="failed", error=str(exc))
            logger.error(f"[{job_type}] Job {job_id} permanently failed after {MAX_RETRIES} attempts.")

async def worker_loop(queue_name: str, semaphore: asyncio.Semaphore):
    queue = queues[queue_name]
    while True:
        job_data = await queue.get()
        async with semaphore:
            job_id = job_data["job_id"]
            payload = job_data["payload"]
            asyncio.create_task(process_job(job_id, queue_name, payload))
        queue.task_done()
