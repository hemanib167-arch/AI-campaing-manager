import sys
import os

# Add the parent directory to sys.path if running as a script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import social_routes, copywriting_routes, banner_routes, job_routes
from .queue.job_manager import start_workers

app = FastAPI(
    title="6E Creative Studio API",
    description="Domain-Driven Architecture Backend",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(social_routes.router, prefix="/api/campaigns")
app.include_router(copywriting_routes.router, prefix="/api/campaigns")
app.include_router(banner_routes.router, prefix="/api/campaigns")
app.include_router(job_routes.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    app.state.worker_tasks = await start_workers()

@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "service": "6E Creative Studio API v2"}
