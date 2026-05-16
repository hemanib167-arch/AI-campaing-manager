from typing import Dict, Any
from ..utils.errors import ValidationError

def parse_social_response(response: Dict[str, Any]) -> Dict[str, Any]:
    if "instagram" not in response or "facebook" not in response or "linkedin" not in response:
        raise ValidationError("Social response missing required platforms.")
    return response

def parse_copy_response(response: Dict[str, Any]) -> Dict[str, Any]:
    if "copy" not in response:
        raise ValidationError("Copy response missing 'copy' field.")
    return response

def parse_banner_response(response: Dict[str, Any]) -> Dict[str, Any]:
    if "dalle_prompt" not in response:
        raise ValidationError("Banner response missing 'dalle_prompt' field.")
    return response
