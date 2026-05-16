import json
import os
from pathlib import Path
from typing import List, Optional


class ProjectRepository:
    def __init__(self, storage_path: str = "backend/data/projects.json"):
        self.storage_path = Path(storage_path)
        self._ensure_storage()

    def _ensure_storage(self):
        """Ensure storage directory and file exist"""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.storage_path.exists():
            self._write_data([])

    def _read_data(self) -> List[dict]:
        """Read all projects from storage"""
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _write_data(self, projects: List[dict]):
        """Write all projects to storage"""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(projects, f, indent=2, ensure_ascii=False)

    def get_all(self) -> List[dict]:
        """Get all projects"""
        return self._read_data()

    def get_by_id(self, project_id: str) -> Optional[dict]:
        """Get a project by ID"""
        projects = self._read_data()
        for project in projects:
            if project["id"] == project_id:
                return project
        return None

    def save(self, project: dict):
        """Save or update a project"""
        projects = self._read_data()

        # Update existing or add new
        for i, p in enumerate(projects):
            if p["id"] == project["id"]:
                projects[i] = project
                break
        else:
            projects.append(project)

        self._write_data(projects)

    def delete(self, project_id: str) -> bool:
        """Delete a project"""
        projects = self._read_data()
        original_len = len(projects)
        projects = [p for p in projects if p["id"] != project_id]

        if len(projects) < original_len:
            self._write_data(projects)
            return True
        return False
