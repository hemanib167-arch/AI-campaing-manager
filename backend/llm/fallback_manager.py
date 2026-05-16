from typing import Dict, Any
from . import azure_openai_client, gemini_client
from ..observability.logger import get_logger
from ..utils.errors import AIProviderError

logger = get_logger(__name__)

async def generate_with_fallback(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    """Tries Azure OpenAI first, falls back to Gemini."""
    try:
        return await azure_openai_client.generate_text(system_prompt, user_prompt)
    except AIProviderError as e:
        logger.warning(f"Azure OpenAI failed ({str(e)}), falling back to Gemini...")
        try:
            return await gemini_client.generate_text(system_prompt, user_prompt)
        except AIProviderError as e2:
            logger.error(f"Both AI providers failed. Gemini Error: {str(e2)}")
            raise AIProviderError("All AI text generation providers failed.")
