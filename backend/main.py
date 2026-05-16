import sys
import os

# Add the parent directory to sys.path if running as a script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import social_routes, copywriting_routes, banner_routes, job_routes
from .routers import project_routes, campaign_routes, asset_routes, analytics_routes, health_routes
from .middleware.logging_middleware import logging_middleware
from .middleware.error_middleware import error_middleware
from .middleware.auth_middleware import auth_middleware
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

@app.middleware("http")
async def add_logging(request, call_next):
    return await logging_middleware(request, call_next)

@app.middleware("http")
async def handle_errors(request, call_next):
    return await error_middleware(request, call_next)

@app.middleware("http")
async def check_auth(request, call_next):
    return await auth_middleware(request, call_next)

app.include_router(social_routes.router, prefix="/api/campaigns")
app.include_router(copywriting_routes.router, prefix="/api/campaigns")
app.include_router(banner_routes.router, prefix="/api/campaigns")
app.include_router(job_routes.router, prefix="/api")
app.include_router(project_routes.router, prefix="/api")
app.include_router(campaign_routes.router, prefix="/api")
app.include_router(asset_routes.router, prefix="/api")
app.include_router(analytics_routes.router, prefix="/api")
app.include_router(health_routes.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    app.state.worker_tasks = await start_workers()

@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "service": "6E Creative Studio API v2"}
