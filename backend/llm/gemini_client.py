import os
import json
from typing import Dict, Any
from ..utils.errors import AIProviderError

async def generate_text(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    """Gemini fallback using new google-genai SDK."""
    api_key = os.getenv("GEMINI_API_KEY")
    model_id = os.getenv("GEMINI_MODEL_NAME", "gemini-3.1-flash-image-preview")
    
    if not api_key:
        raise AIProviderError("GEMINI_API_KEY not set.")

    try:
        from google import genai
        from google.genai import types
        import asyncio

        client = genai.Client(api_key=api_key)
        
        full_prompt = (
            f"SYSTEM INSTRUCTIONS: {system_prompt}\n\n"
            f"USER REQUEST: {user_prompt}\n\n"
            "IMPORTANT: Return ONLY valid JSON."
        )

        loop = asyncio.get_event_loop()
        
        def _call_gemini():
            return client.models.generate_content(
                model=model_id,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    response_mime_type='application/json',
                )
            )

        response = await loop.run_in_executor(None, _call_gemini)
        text = response.text.strip()

        # Extract JSON
        if "{" in text and "}" in text:
            start = text.find("{")
            end = text.rfind("}") + 1
            text = text[start:end]

        return json.loads(text)
    except Exception as e:
        raise AIProviderError(f"Gemini (google-genai) failed: {str(e)}")
