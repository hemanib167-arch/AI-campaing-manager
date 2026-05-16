"""
Gemini Client Implementation Example for 6E Creative Studio
This is a production-ready implementation example for integrating Gemini API.
"""

import os
from typing import Dict, List, Optional, Any
import asyncio
import logging

try:
    import google.generativeai as genai
except ImportError:
    raise ImportError(
        "google-generativeai package is required. "
        "Install it with: pip install google-generativeai"
    )

logger = logging.getLogger(__name__)


class GeminiClient:
    """
    Production-ready Gemini API client for creative content generation.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gemini-1.5-pro",
        default_temperature: float = 0.7,
        max_retries: int = 3
    ):
        """
        Initialize the Gemini client.

        Args:
            api_key: Gemini API key. If None, reads from GEMINI_API_KEY env var.
            model_name: Model to use for generation.
            default_temperature: Default temperature for generation (0.0-1.0).
            max_retries: Maximum number of retry attempts for failed requests.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Gemini API key is required. "
                "Set GEMINI_API_KEY environment variable or pass it directly."
            )

        # Configure the SDK
        genai.configure(api_key=self.api_key)

        self.model_name = model_name
        self.default_temperature = default_temperature
        self.max_retries = max_retries

        # Safety settings for brand-safe content
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]

    def _create_model(
        self,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> genai.GenerativeModel:
        """
        Create a configured GenerativeModel instance.

        Args:
            temperature: Temperature for generation (overrides default).
            max_tokens: Maximum output tokens.

        Returns:
            Configured GenerativeModel instance.
        """
        generation_config = genai.types.GenerationConfig(
            temperature=temperature or self.default_temperature,
            max_output_tokens=max_tokens or 2048,
        )

        return genai.GenerativeModel(
            self.model_name,
            generation_config=generation_config,
            safety_settings=self.safety_settings
        )

    async def generate_copywriting(
        self,
        brand_name: str,
        target_audience: str,
        key_message: str,
        tone: str,
        variations: int = 3
    ) -> List[Dict[str, str]]:
        """
        Generate campaign copywriting variations.

        Args:
            brand_name: Name of the brand.
            target_audience: Description of target audience.
            key_message: Main message to convey.
            tone: Desired tone (e.g., "professional", "playful", "sophisticated").
            variations: Number of variations to generate.

        Returns:
            List of copy variations with headline, body, and CTA.
        """
        prompt = f"""Generate {variations} variations of ad copy for {brand_name}.

Target Audience: {target_audience}
Tone: {tone}
Key Message: {key_message}

For each variation, provide:
- A compelling headline (max 60 characters)
- Body copy (2-3 sentences)
- A clear call-to-action

Format as JSON array:
[
  {{"headline": "...", "body": "...", "cta": "..."}},
  ...
]"""

        model = self._create_model(temperature=0.8)

        try:
            response = model.generate_content(prompt)
            # Parse the JSON response
            import json

            text = response.text.strip()
            # Remove markdown code blocks if present
            if text.startswith("```"):
                lines = text.split("\n")
                text = "\n".join(lines[1:-1]) if len(lines) > 2 else text

            variations_data = json.loads(text)
            logger.info(f"Generated {len(variations_data)} copywriting variations")
            return variations_data

        except Exception as e:
            logger.error(f"Failed to generate copywriting: {str(e)}")
            raise

    async def generate_social_media(
        self,
        brand_voice: str,
        theme: str,
        platform: str,
        count: int = 5
    ) -> List[str]:
        """
        Generate social media captions.

        Args:
            brand_voice: Brand voice description.
            theme: Theme or topic for the posts.
            platform: Social media platform (e.g., "Instagram", "Twitter", "LinkedIn").
            count: Number of captions to generate.

        Returns:
            List of social media captions.
        """
        platform_specs = {
            "Instagram": "Include relevant hashtags and emoji. Keep under 150 characters.",
            "Twitter": "Keep under 280 characters. Use 1-2 relevant hashtags.",
            "LinkedIn": "Professional tone. 1-2 paragraphs with optional hashtags.",
            "Facebook": "Conversational and engaging. 1-3 sentences with call-to-action."
        }

        spec = platform_specs.get(platform, "Engaging and platform-appropriate.")

        prompt = f"""Create {count} {platform} captions for a brand.

Brand Voice: {brand_voice}
Theme: {theme}
Platform Requirements: {spec}

Return as a JSON array of strings:
["caption 1", "caption 2", ...]"""

        model = self._create_model(temperature=0.9)

        try:
            response = model.generate_content(prompt)

            import json
            text = response.text.strip()
            if text.startswith("```"):
                lines = text.split("\n")
                text = "\n".join(lines[1:-1]) if len(lines) > 2 else text

            captions = json.loads(text)
            logger.info(f"Generated {len(captions)} social media captions for {platform}")
            return captions

        except Exception as e:
            logger.error(f"Failed to generate social media content: {str(e)}")
            raise

    async def generate_image_prompt(
        self,
        campaign_description: str,
        scene: str,
        style: str,
        mood: str
    ) -> str:
        """
        Generate a detailed image generation prompt.

        Args:
            campaign_description: Brief description of the campaign.
            scene: Scene description.
            style: Visual style (e.g., "photography", "illustration", "3D render").
            mood: Desired mood or atmosphere.

        Returns:
            Detailed image generation prompt.
        """
        prompt = f"""Generate a detailed image generation prompt optimized for DALL-E 3.

Campaign: {campaign_description}
Scene: {scene}
Style: {style}
Mood: {mood}

Create a single, detailed prompt that includes:
- Subject and composition
- Lighting and atmosphere
- Color palette
- Technical details (camera angle, depth of field, etc.)
- Style specifications

Return only the image prompt, no explanations."""

        model = self._create_model(temperature=0.7, max_tokens=500)

        try:
            response = model.generate_content(prompt)
            image_prompt = response.text.strip()
            logger.info(f"Generated image prompt: {image_prompt[:100]}...")
            return image_prompt

        except Exception as e:
            logger.error(f"Failed to generate image prompt: {str(e)}")
            raise

    async def analyze_campaign_brief(
        self,
        brief_text: str
    ) -> Dict[str, Any]:
        """
        Extract structured information from a campaign brief.

        Args:
            brief_text: Raw campaign brief text.

        Returns:
            Structured campaign data.
        """
        prompt = f"""Analyze this campaign brief and extract key information:

{brief_text}

Return ONLY valid JSON with this structure:
{{
  "product": "product/service name",
  "target_audience": "audience description",
  "key_features": ["feature1", "feature2"],
  "budget": number or null,
  "channels": ["channel1", "channel2"],
  "timeline": "timeline description",
  "objectives": ["objective1", "objective2"],
  "tone": "desired tone/voice"
}}"""

        model = self._create_model(temperature=0.3)

        try:
            response = model.generate_content(prompt)

            import json
            text = response.text.strip()
            if text.startswith("```"):
                lines = text.split("\n")
                text = "\n".join(lines[1:-1]) if len(lines) > 2 else text

            campaign_data = json.loads(text)
            logger.info(f"Analyzed campaign brief for: {campaign_data.get('product')}")
            return campaign_data

        except Exception as e:
            logger.error(f"Failed to analyze campaign brief: {str(e)}")
            raise

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None
    ) -> str:
        """
        Multi-turn conversation with context.

        Args:
            messages: List of message dicts with 'role' and 'content' keys.
            temperature: Temperature for generation.

        Returns:
            Assistant's response.
        """
        model = self._create_model(temperature=temperature)

        # Convert messages to Gemini format
        history = []
        for msg in messages[:-1]:  # All except the last message
            role = "user" if msg["role"] == "user" else "model"
            history.append({"role": role, "parts": [msg["content"]]})

        # Start chat with history
        chat = model.start_chat(history=history)

        # Send the last message
        last_message = messages[-1]["content"]

        try:
            response = chat.send_message(last_message)
            logger.info("Generated chat response")
            return response.text

        except Exception as e:
            logger.error(f"Failed to generate chat response: {str(e)}")
            raise

    async def stream_completion(
        self,
        prompt: str,
        temperature: Optional[float] = None
    ):
        """
        Stream response tokens in real-time.

        Args:
            prompt: Input prompt.
            temperature: Temperature for generation.

        Yields:
            Response chunks as they are generated.
        """
        model = self._create_model(temperature=temperature)

        try:
            response = model.generate_content(prompt, stream=True)

            for chunk in response:
                if chunk.text:
                    yield chunk.text

            logger.info("Completed streaming response")

        except Exception as e:
            logger.error(f"Failed to stream response: {str(e)}")
            raise

    def count_tokens(self, text: str) -> int:
        """
        Count tokens in text for cost estimation.

        Args:
            text: Text to count tokens for.

        Returns:
            Token count.
        """
        model = genai.GenerativeModel(self.model_name)
        token_count = model.count_tokens(text)
        return token_count.total_tokens


# Example usage
async def main():
    """Example usage of the GeminiClient."""

    # Initialize client
    client = GeminiClient()

    # Example 1: Generate copywriting
    print("=== Copywriting Example ===")
    copies = await client.generate_copywriting(
        brand_name="EcoBottle",
        target_audience="Environmentally conscious millennials",
        key_message="Sustainable hydration for a better planet",
        tone="Inspirational and authentic",
        variations=2
    )
    print(f"Generated {len(copies)} variations")
    for i, copy in enumerate(copies, 1):
        print(f"\nVariation {i}:")
        print(f"  Headline: {copy['headline']}")
        print(f"  Body: {copy['body']}")
        print(f"  CTA: {copy['cta']}")

    # Example 2: Social media content
    print("\n=== Social Media Example ===")
    captions = await client.generate_social_media(
        brand_voice="Authentic, eco-conscious, empowering",
        theme="Spring sustainable fashion collection",
        platform="Instagram",
        count=3
    )
    for i, caption in enumerate(captions, 1):
        print(f"\nCaption {i}: {caption}")

    # Example 3: Image prompt
    print("\n=== Image Prompt Example ===")
    image_prompt = await client.generate_image_prompt(
        campaign_description="Organic coffee brand launch",
        scene="Morning coffee ritual in a sustainable home",
        style="Natural lifestyle photography",
        mood="Peaceful and inviting"
    )
    print(f"Image Prompt: {image_prompt}")


if __name__ == "__main__":
    asyncio.run(main())
