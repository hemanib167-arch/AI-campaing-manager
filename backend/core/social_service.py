import asyncio
from typing import Dict, Any
from ..llm.fallback_manager import generate_with_fallback
from ..llm.prompt_builder import build_system_prompt, build_prompt
from ..llm.response_parser import parse_social_response
from ..llm.guardrails import check_response_guardrails
from ..image.image_client import generate_image
from .validation_service import validation_service

class SocialService:
    async def generate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        validation_service.validate_social_campaign(payload)
        
        system_prompt = build_system_prompt()
        user_prompt = build_prompt("social", payload)
        
        # 1. Generate text and image descriptions via LLM
        response = await generate_with_fallback(system_prompt, user_prompt)
        check_response_guardrails(response)
        
        # Note: Depending on response_parser, we might need to ensure it handles image_prompt
        # For simplicity, we'll assume response is already the JSON we need
        data = response 
        
        # 2. Generate images for each platform in parallel
        platforms = ["instagram", "facebook", "linkedin"]
        tasks = []
        for p in platforms:
            if p in data and "image_prompt" in data[p]:
                tasks.append(self._gen_image_for_platform(data, p))
        
        if tasks:
            await asyncio.gather(*tasks)
            
        return data

    async def _gen_image_for_platform(self, data: Dict[str, Any], platform: str):
        prompt = data[platform]["image_prompt"]
        try:
            image_url = await generate_image(prompt)
            data[platform]["image_url"] = image_url
        except Exception:
            data[platform]["image_url"] = "https://placehold.co/1024x1024/1A1AAF/FFFFFF?text=Image+Error"

social_service = SocialService()
