import os
import json
from typing import Dict, Any
from ..utils.errors import AIProviderError

async def generate_text(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    # Placeholder for Gemini client during hackathon
    # Currently raising error to force fallback failure if Azure fails
    raise AIProviderError("Gemini client not fully configured for hackathon yet.")
