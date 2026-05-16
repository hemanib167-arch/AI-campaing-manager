from typing import Dict
from .logger import get_logger

logger = get_logger(__name__)

# Very basic stub for metrics tracking
_metrics_store: Dict[str, float] = {}

def record_metric(name: str, value: float) -> None:
    _metrics_store[name] = _metrics_store.get(name, 0) + value
    logger.info(f"Metric Recorded: {name}={value}")

def get_metrics() -> Dict[str, float]:
    return _metrics_store
