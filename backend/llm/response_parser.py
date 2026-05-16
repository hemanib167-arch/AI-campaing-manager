from typing import Dict, Any
from ..utils.errors import ValidationError

def parse_social_response(response: Dict[str, Any]) -> Dict[str, Any]:
    # Support both old and new (with image_url/image_prompt)
    if "instagram" not in response:
        raise ValidationError("Social response missing 'instagram' platform.")
    return response

def parse_copy_response(response: Dict[str, Any]) -> Dict[str, Any]:
    # Support new detailed structure
    if "headline" not in response and "copy" not in response:
        raise ValidationError("Copy response missing required content (headline or copy).")
    return response

def parse_banner_response(response: Dict[str, Any]) -> Dict[str, Any]:
    if "dalle_prompt" not in response:
        raise ValidationError("Banner response missing 'dalle_prompt' field.")
    return response
