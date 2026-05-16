import asyncio
from .job_queue import queues
from .worker import worker_loop, CONCURRENT_SLOTS

async def start_workers():
    tasks = []
    for q_name in queues:
        sem = asyncio.Semaphore(CONCURRENT_SLOTS)
        tasks.append(asyncio.create_task(worker_loop(q_name, sem)))
    return tasks
