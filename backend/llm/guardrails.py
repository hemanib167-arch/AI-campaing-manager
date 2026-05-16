from typing import Dict, Any
from ..utils.errors import ValidationError

# Simple guardrails for the hackathon
FORBIDDEN_TERMS = ["cheapest flights guaranteed", "competitor"]

def apply_guardrails(text: str) -> None:
    text_lower = text.lower()
    for term in FORBIDDEN_TERMS:
        if term in text_lower:
            raise ValidationError(f"Content failed guardrails: contained forbidden term '{term}'")

def check_response_guardrails(response: Dict[str, Any]) -> None:
    """Recursively checks a JSON response for forbidden terms."""
    if isinstance(response, dict):
        for val in response.values():
            check_response_guardrails(val)
    elif isinstance(response, list):
        for item in response:
            check_response_guardrails(item)
    elif isinstance(response, str):
        apply_guardrails(response)
