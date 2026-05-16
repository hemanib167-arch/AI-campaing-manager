from typing import Dict, Any
from ..llm.fallback_manager import generate_with_fallback
from ..llm.prompt_builder import build_system_prompt, build_prompt
from ..llm.response_parser import parse_copy_response
from ..llm.guardrails import check_response_guardrails
from .validation_service import validation_service

class CopywritingService:
    async def generate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        validation_service.validate_copywriting(payload)
        
        system_prompt = build_system_prompt()
        user_prompt = build_prompt("copy", payload)
        
        response = await generate_with_fallback(system_prompt, user_prompt)
        check_response_guardrails(response)
        
        return parse_copy_response(response)

copywriting_service = CopywritingService()
