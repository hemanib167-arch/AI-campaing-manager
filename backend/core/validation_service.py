from typing import Dict, Any
from ..utils.errors import ValidationError

class ValidationService:
    @staticmethod
    def validate_social_campaign(data: Dict[str, Any]) -> None:
        if "campaign_type" not in data:
            raise ValidationError("Missing 'campaign_type' in social campaign data.")
        if "description" not in data or not data["description"].strip():
            raise ValidationError("Missing or empty 'description' in social campaign data.")

    @staticmethod
    def validate_copywriting(data: Dict[str, Any]) -> None:
        if "channel" not in data:
            raise ValidationError("Missing 'channel' in copywriting data.")
        if "brief" not in data:
            raise ValidationError("Missing 'brief' in copywriting data.")

    @staticmethod
    def validate_banner(data: Dict[str, Any]) -> None:
        if "brief" not in data:
            raise ValidationError("Missing 'brief' in banner data.")

validation_service = ValidationService()
