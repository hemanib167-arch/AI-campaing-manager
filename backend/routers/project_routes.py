from fastapi import APIRouter
from typing import List
from ..schemas.project_schema import ProjectSchema
from ..core.project_service import project_service

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectSchema)
def create_project(request: ProjectSchema):
    return project_service.create_project(request.dict(exclude_unset=True))

@router.get("/", response_model=List[ProjectSchema])
def get_projects():
    return project_service.get_projects()
