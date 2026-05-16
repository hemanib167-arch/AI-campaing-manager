from typing import Dict, Any

class BrandService:
    def get_brand_guidelines(self) -> Dict[str, Any]:
        """Returns IndiGo brand guidelines."""
        return {
            "name": "IndiGo",
            "code": "6E",
            "colors": {
                "primary": "#1A1AAF",
                "secondary": "#FFFFFF",
                "accent": "#FF6600"
            },
            "tone": "confident, aspirational, travel-forward, slightly playful but professional",
            "hashtags": ["#IndiGo", "#6ECreativeStudio", "#TravelWith6E"]
        }

brand_service = BrandService()
