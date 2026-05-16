import os
from ..utils.errors import CreativeStudioError

def load_prompt(name: str) -> str:
    """Loads a prompt template from shared/prompts/"""
    # Navigate from backend/llm/prompt_loader.py to shared/prompts/
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.join(base_dir, "shared", "prompts", f"{name}.txt")
    
    if not os.path.exists(path):
        raise CreativeStudioError(f"Prompt template '{name}' not found at {path}", 500)
        
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
