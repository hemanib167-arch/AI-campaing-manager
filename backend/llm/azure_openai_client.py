import os
import json
from typing import Dict, Any
from openai import AsyncAzureOpenAI
from ..utils.errors import AIProviderError

def _get_client() -> AsyncAzureOpenAI:
    """Build Azure OpenAI async client."""
    return AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview"),
    )

async def generate_text(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    """Calls Azure OpenAI (gpt-5-mini series)."""
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5-mini1")

    try:
        client = _get_client()
        
        # Combine instructions for o-series compatibility
        combined_content = f"### SYSTEM INSTRUCTIONS\n{system_prompt}\n\n### USER REQUEST\n{user_prompt}\n\nIMPORTANT: Return valid JSON only."
        
        response = await client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "user", "content": combined_content},
            ],
            # Use max_completion_tokens for o1/mini compatibility
            max_completion_tokens=4000
        )
        
        content = response.choices[0].message.content
        if not content:
            raise AIProviderError("Azure OpenAI returned empty content.")
            
        text = content.strip()
        if "{" in text and "}" in text:
            start = text.find("{")
            end = text.rfind("}") + 1
            text = text[start:end]
            
        return json.loads(text)
    except Exception as e:
        raise AIProviderError(f"Azure OpenAI Error: {str(e)}")
