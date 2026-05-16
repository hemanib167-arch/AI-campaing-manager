from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import campaigns, jobs
from .services.worker_service import start_workers

app = FastAPI(
    title="6E Creative Studio API",
    description="AI-powered marketing content engine for IndiGo Airlines (6E)",
    version="1.0.0",
)

# CORS — allow the Vite dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(campaigns.router)
app.include_router(jobs.router)


@app.on_event("startup")
async def startup_event():
    app.state.worker_tasks = await start_workers()


@app.get("/", tags=["Health"])
async def root():
    return {"status": "ok", "service": "6E Creative Studio API"}
