from typing import Dict, Any
from . import azure_openai_client, gemini_client
from ..observability.logger import get_logger
from ..utils.errors import AIProviderError

logger = get_logger(__name__)

async def generate_with_fallback(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    """Tries Azure OpenAI first, falls back to Gemini."""
    errors = []
    
    # 1. Try Azure
    try:
        return await azure_openai_client.generate_text(system_prompt, user_prompt)
    except Exception as e:
        err_msg = f"Azure Error: {str(e)}"
        logger.warning(err_msg)
        errors.append(err_msg)
        
    # 2. Try Gemini
    try:
        return await gemini_client.generate_text(system_prompt, user_prompt)
    except Exception as e:
        err_msg = f"Gemini Error: {str(e)}"
        logger.error(f"Both AI providers failed. {err_msg}")
        errors.append(err_msg)
        
    # If both failed, raise combined error
    raise AIProviderError(f"AI Generation Failed. Details: {' | '.join(errors)}")
