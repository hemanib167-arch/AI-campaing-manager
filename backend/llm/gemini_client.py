import os
import json
from typing import Dict, Any
from ..utils.errors import AIProviderError

async def generate_text(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    """Gemini fallback using google-generativeai SDK."""
    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-2.5-flash")
    if not api_key:
        raise AIProviderError("GEMINI_API_KEY not set.")

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(model_name)

        full_prompt = (
            f"SYSTEM: {system_prompt}\n\n"
            f"USER: {user_prompt}\n\n"
            "Respond ONLY with valid JSON."
        )

        response = model.generate_content(full_prompt)
        text = response.text.strip()

        # Extract JSON
        if "{" in text and "}" in text:
            start = text.find("{")
            end = text.rfind("}") + 1
            text = text[start:end]

        return json.loads(text)
    except Exception as e:
        raise AIProviderError(f"Gemini Error ({model_name}): {str(e)}")
