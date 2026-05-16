"""
workers/main.py
Dev 3 owns this file.

4 queues × 3 concurrent slots = 12 max parallel AI calls.
Each worker retries failed jobs up to 3 times before marking them FAILED.
"""
import asyncio
import logging
import sys
import os

# Make sure the backend package is importable when workers/ runs standalone
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.app.queue import queues
from backend.app.memory import update_job, get_job
from backend.app.schemas.main import JobStatus
from backend.app.services.ai_service import generate_content, generate_image

logger = logging.getLogger(__name__)

MAX_RETRIES = 3
CONCURRENT_SLOTS = 3  # per queue


async def process_job(job_id: str, job_type: str, payload: dict, attempt: int = 1):
    try:
        update_job(job_id, status=JobStatus.PROCESSING)

        if job_type == "banner":
            result = await generate_image("banner", payload)
        else:
            result = await generate_content(job_type, payload)

        update_job(job_id, status=JobStatus.COMPLETED, result=result)
        logger.info(f"[{job_type}] Job {job_id} completed on attempt {attempt}.")

    except Exception as exc:
        logger.warning(f"[{job_type}] Job {job_id} failed (attempt {attempt}): {exc}")
        if attempt < MAX_RETRIES:
            await asyncio.sleep(1.5 ** attempt)          # back-off
            await process_job(job_id, job_type, payload, attempt + 1)
        else:
            update_job(job_id, status=JobStatus.FAILED, error=str(exc))
            logger.error(f"[{job_type}] Job {job_id} permanently failed after {MAX_RETRIES} attempts.")


async def worker_loop(queue_name: str, semaphore: asyncio.Semaphore):
    """Single worker coroutine — blocks on its queue and respects the semaphore."""
    queue = queues[queue_name]
    while True:
        job_data = await queue.get()
        async with semaphore:
            job_id = job_data["job_id"]
            payload = job_data["payload"]
            asyncio.create_task(process_job(job_id, queue_name, payload))
        queue.task_done()


async def start_workers():
    """
    Spin up 4 worker coroutines (one per queue).
    Each queue gets a semaphore limiting it to CONCURRENT_SLOTS simultaneous AI calls.
    """
    tasks = []
    for q_name in queues:
        sem = asyncio.Semaphore(CONCURRENT_SLOTS)
        tasks.append(asyncio.create_task(worker_loop(q_name, sem)))
    return tasks
