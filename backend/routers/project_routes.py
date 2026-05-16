from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.project_schema import Project, ProjectCreate
from ..core.project_service import ProjectService

router = APIRouter(prefix="/api/projects", tags=["Projects"])


@router.get("/", response_model=List[Project])
async def list_projects(service: ProjectService = Depends()):
    """List all projects"""
    return service.list_projects()


@router.get("/{project_id}", response_model=Project)
async def get_project(project_id: str, service: ProjectService = Depends()):
    """Get a specific project"""
    project = service.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/", response_model=Project, status_code=201)
async def create_project(data: ProjectCreate, service: ProjectService = Depends()):
    """Create a new project"""
    return service.create_project(data.name, data.description)


@router.delete("/{project_id}", status_code=204)
async def delete_project(project_id: str, service: ProjectService = Depends()):
    """Delete a project"""
    success = service.delete_project(project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
