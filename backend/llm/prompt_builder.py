from typing import Dict, Any
from .prompt_loader import load_prompt

def build_prompt(prompt_name: str, variables: Dict[str, Any]) -> str:
    template = load_prompt(prompt_name)
    try:
        return template.format(**variables)
    except KeyError as e:
        # If a variable is missing, just return the raw template or handle it
        # For this hackathon, we assume variables map exactly.
        raise ValueError(f"Missing variable {e} for prompt {prompt_name}")

def build_system_prompt() -> str:
    return load_prompt("system")
