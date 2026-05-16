import os
from openai import AsyncOpenAI
from ..utils.errors import AIProviderError

_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY", "dummy-key"))

async def generate_image(prompt: str, size: str = "1024x1024") -> str:
    """Calls DALL-E 3 and returns the image URL."""
    try:
        response = await _client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        raise AIProviderError(f"DALL-E 3 Error: {str(e)}")
