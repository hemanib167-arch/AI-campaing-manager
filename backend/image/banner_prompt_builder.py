from typing import Dict, Any
from ..llm.prompt_builder import build_prompt

def build_banner_prompt(variables: Dict[str, Any]) -> str:
    """Uses the prompt builder to format the banner brief."""
    return build_prompt("banner", variables)
