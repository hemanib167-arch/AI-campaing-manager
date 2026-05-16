import asyncio
from typing import Dict

# 4 queues as per original spec: social, copy, banner, priority
queues: Dict[str, asyncio.Queue] = {
    "social": asyncio.Queue(),
    "copy": asyncio.Queue(),
    "banner": asyncio.Queue(),
    "priority": asyncio.Queue()
}

async def add_to_queue(job_type: str, job_id: str, payload: dict):
    queue_name = job_type if job_type in queues else "social"
    await queues[queue_name].put({
        "job_id": job_id,
        "payload": payload
    })
