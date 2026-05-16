from typing import List, Dict, Any
from ..storage.project_repository import project_repository
from ..utils.id_generator import generate_id

class ProjectService:
    def create_project(self, data: Dict[str, Any]) -> Dict[str, Any]:
        project_id = generate_id("proj")
        data["id"] = project_id
        project_repository.create(project_id, data)
        return data

    def get_projects(self) -> List[Dict[str, Any]]:
        return project_repository.get_all()

    def get_project(self, project_id: str) -> Dict[str, Any]:
        return project_repository.get_by_id(project_id)

project_service = ProjectService()
