import os
import json
from typing import Dict, Any
from openai import AsyncOpenAI
from ..utils.errors import AIProviderError

# Initialize client using standard OpenAI for hackathon purposes 
# (simulating Azure OpenAI structure)
_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY", "dummy-key"))

async def generate_text(system_prompt: str, user_prompt: str) -> Dict[str, Any]:
    try:
        response = await _client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        raise AIProviderError(f"Azure OpenAI Error: {str(e)}")
