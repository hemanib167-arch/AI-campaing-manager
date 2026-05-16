from typing import Dict, Any
from ..llm.fallback_manager import generate_with_fallback
from ..llm.prompt_builder import build_system_prompt
from ..image.banner_prompt_builder import build_banner_prompt
from ..llm.response_parser import parse_banner_response
from ..llm.guardrails import check_response_guardrails
from ..image.image_client import generate_image
from .validation_service import validation_service

class BannerService:
    async def generate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        validation_service.validate_banner(payload)
        
        system_prompt = build_system_prompt()
        user_prompt = build_banner_prompt(payload)
        
        # 1. Generate text brief via LLM
        llm_response = await generate_with_fallback(system_prompt, user_prompt)
        check_response_guardrails(llm_response)
        parsed_response = llm_response # Assuming response is already JSON
        
        # 2. Map aspect ratio to DALL-E 3 sizes
        ar = payload.get("aspect_ratio", "1:1")
        size_map = {
            "16:9": "1792x1024",
            "9:16": "1024x1792",
            "1:1": "1024x1024"
        }
        dalle_size = size_map.get(ar, "1024x1024")
        
        # 3. Generate image using DALL-E 3
        dalle_prompt = parsed_response.get("dalle_prompt", payload.get("brief"))
        image_url = await generate_image(dalle_prompt, size=dalle_size)
        
        parsed_response["image_url"] = image_url
        return parsed_response

banner_service = BannerService()
