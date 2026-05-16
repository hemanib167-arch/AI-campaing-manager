"""
backend/app/services/worker_service.py
Thin shim — imports the real worker start function from workers/main.py
so that the FastAPI startup event and the standalone workers package
both use the same implementation.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../"))

from workers.main import start_workers  # noqa: F401

__all__ = ["start_workers"]
