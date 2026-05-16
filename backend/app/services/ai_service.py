import os
import json
from openai import AsyncOpenAI
from typing import Dict, Any

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY", "your-key-here"))

def load_prompt(name: str) -> str:
    path = os.path.join(os.path.dirname(__file__), "../../../shared/prompts", f"{name}.txt")
    with open(path, "r") as f:
        return f.read()

async def generate_content(prompt_name: str, variables: Dict[str, Any]) -> Dict:
    system_prompt = load_prompt("system")
    user_prompt_template = load_prompt(prompt_name)
    user_prompt = user_prompt_template.format(**variables)

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)

async def generate_image(prompt_name: str, variables: Dict[str, Any]) -> Dict:
    # First get the prompt from GPT-4o
    dalle_brief = await generate_content(prompt_name, variables)
    
    # Then call DALL-E 3
    response = await client.images.generate(
        model="dall-e-3",
        prompt=dalle_brief["dalle_prompt"],
        size=variables.get("resolution", "1024x1024"),
        quality="standard",
        n=1,
    )
    
    dalle_brief["image_url"] = response.data[0].url
    return dalle_brief
