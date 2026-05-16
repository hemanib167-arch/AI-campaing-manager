import uuid

def generate_id(prefix: str = "") -> str:
    """Generate a unique ID, optionally with a prefix."""
    unique_id = str(uuid.uuid4())
    if prefix:
        return f"{prefix}_{unique_id}"
    return unique_id
