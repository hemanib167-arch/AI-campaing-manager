from typing import List, Optional
from datetime import datetime
from ..utils.id_generator import generate_id
from ..storage.project_repository import ProjectRepository


class ProjectService:
    def __init__(self):
        self.repository = ProjectRepository()

    def list_projects(self) -> List[dict]:
        """List all projects"""
        return self.repository.get_all()

    def get_project(self, project_id: str) -> Optional[dict]:
        """Get a specific project"""
        return self.repository.get_by_id(project_id)

    def create_project(self, name: str, description: str = "") -> dict:
        """Create a new project"""
        project = {
            "id": generate_id("proj"),
            "name": name,
            "description": description,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": None,
        }
        self.repository.save(project)
        return project

    def update_project(self, project_id: str, name: str = None, description: str = None) -> Optional[dict]:
        """Update a project"""
        project = self.get_project(project_id)
        if not project:
            return None

        if name:
            project["name"] = name
        if description is not None:
            project["description"] = description
        project["updated_at"] = datetime.utcnow().isoformat()

        self.repository.save(project)
        return project

    def delete_project(self, project_id: str) -> bool:
        """Delete a project"""
        return self.repository.delete(project_id)
