from typing import List, Optional, Dict, Any
from .memory_store import projects_db

class ProjectRepository:
    def get_by_id(self, project_id: str) -> Optional[Dict[str, Any]]:
        return projects_db.get(project_id)

    def get_all(self) -> List[Dict[str, Any]]:
        return projects_db.get_all()

    def create(self, project_id: str, data: Dict[str, Any]) -> None:
        projects_db.save(project_id, data)

    def update(self, project_id: str, data: Dict[str, Any]) -> None:
        existing = projects_db.get(project_id)
        if existing:
            existing.update(data)
            projects_db.save(project_id, existing)

    def delete(self, project_id: str) -> bool:
        return projects_db.delete(project_id)

project_repository = ProjectRepository()
