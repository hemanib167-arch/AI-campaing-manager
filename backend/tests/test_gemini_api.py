"""
Gemini API Testing Script
Tests Google's Gemini API functionality for the 6E Creative Studio project.
"""

import os
import asyncio
from typing import Optional
import json


class GeminiAPITester:
    """Test suite for Gemini API integration."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini API tester.

        Args:
            api_key: Gemini API key. If not provided, reads from GEMINI_API_KEY env var.
        """
        api_key="AlzaSyDCH3BUM29CNHJH5w8Obg-BhNNGOWXeBms"
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY environment variable or pass it directly.")

        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        self.model = "gemini-3.1-flash-image-preview"

    async def test_basic_generation(self):
        """Test basic text generation with Gemini API."""
        print("\n=== Testing Basic Text Generation ===")

        try:
            import httpx

            url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

            payload = {
                "contents": [{
                    "parts": [{
                        "text": "Write a catchy tagline for an eco-friendly water bottle brand."
                    }]
                }]
            }

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    print(f"✓ Success! Generated text:\n{text}")
                    return True
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def test_copywriting_generation(self):
        """Test copywriting generation for campaigns."""
        print("\n=== Testing Copywriting Generation ===")

        try:
            import httpx

            url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

            prompt = """Generate 3 variations of ad copy for a luxury watch brand campaign.

Target Audience: Professionals aged 30-50
Tone: Sophisticated, aspirational
Key Message: Timeless elegance meets modern innovation

Format the response as JSON with this structure:
{
  "variations": [
    {"headline": "...", "body": "...", "cta": "..."},
    {"headline": "...", "body": "...", "cta": "..."},
    {"headline": "...", "body": "...", "cta": "..."}
  ]
}"""

            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.8,
                    "topK": 40,
                    "topP": 0.95,
                    "maxOutputTokens": 1024,
                }
            }

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    print(f"✓ Success! Generated copywriting:\n{text[:500]}...")
                    return True
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def test_social_media_generation(self):
        """Test social media content generation."""
        print("\n=== Testing Social Media Content Generation ===")

        try:
            import httpx

            url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

            prompt = """Create 5 Instagram captions for a sustainable fashion brand launching a new collection.

Brand Voice: Authentic, eco-conscious, empowering
Theme: Spring collection made from recycled materials
Include: relevant hashtags and emoji

Keep each caption under 150 characters."""

            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.9,
                    "maxOutputTokens": 800,
                }
            }

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    print(f"✓ Success! Generated social media content:\n{text}")
                    return True
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def test_image_prompt_generation(self):
        """Test image prompt generation for DALL-E/Midjourney."""
        print("\n=== Testing Image Prompt Generation ===")

        try:
            import httpx

            url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

            prompt = """Generate a detailed image generation prompt for an AI image model.

Campaign: Organic coffee brand launch
Scene: Morning coffee ritual in a cozy, sustainable home
Style: Natural lighting, warm tones, lifestyle photography
Mood: Peaceful, authentic, inviting

Create a detailed prompt optimized for DALL-E 3."""

            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 500,
                }
            }

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    print(f"✓ Success! Generated image prompt:\n{text}")
                    return True
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def test_structured_output(self):
        """Test structured JSON output generation."""
        print("\n=== Testing Structured Output ===")

        try:
            import httpx

            url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

            prompt = """Analyze this campaign brief and extract key information:

"We're launching a new line of smart fitness trackers targeting health-conscious millennials.
The campaign should emphasize our unique sleep tracking technology and 14-day battery life.
Budget is $50,000 for digital ads across Instagram, Facebook, and Google.
Timeline: Launch in 3 weeks."

Return ONLY valid JSON with this structure:
{
  "product": "product name",
  "target_audience": "audience description",
  "key_features": ["feature1", "feature2"],
  "budget": 50000,
  "channels": ["channel1", "channel2"],
  "timeline": "timeline description"
}"""

            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.3,
                    "maxOutputTokens": 500,
                }
            }

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

                    # Try to parse as JSON
                    try:
                        # Remove markdown code blocks if present
                        clean_text = text.strip()
                        if clean_text.startswith("```"):
                            clean_text = clean_text.split("```")[1]
                            if clean_text.startswith("json"):
                                clean_text = clean_text[4:]

                        parsed = json.loads(clean_text.strip())
                        print(f"✓ Success! Parsed structured output:")
                        print(json.dumps(parsed, indent=2))
                        return True
                    except json.JSONDecodeError:
                        print(f"✓ API call succeeded but output is not valid JSON:")
                        print(text)
                        return False
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def test_safety_settings(self):
        """Test content generation with safety settings."""
        print("\n=== Testing Safety Settings ===")

        try:
            import httpx

            url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

            payload = {
                "contents": [{
                    "parts": [{
                        "text": "Write a professional email to a potential client introducing our creative agency."
                    }]
                }],
                "safetySettings": [
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
            }

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)

                if response.status_code == 200:
                    data = response.json()
                    text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                    print(f"✓ Success! Generated text with safety settings:\n{text[:300]}...")
                    return True
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def test_model_listing(self):
        """Test listing available Gemini models."""
        print("\n=== Testing Model Listing ===")

        try:
            import httpx

            url = f"{self.base_url}/models?key={self.api_key}"

            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(url)

                if response.status_code == 200:
                    data = response.json()
                    models = data.get("models", [])
                    print(f"✓ Success! Found {len(models)} available models:")
                    for model in models[:5]:  # Show first 5
                        name = model.get("name", "")
                        display_name = model.get("displayName", "")
                        print(f"  - {display_name} ({name})")
                    return True
                else:
                    print(f"✗ Failed with status {response.status_code}")
                    print(f"Response: {response.text}")
                    return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    async def run_all_tests(self):
        """Run all test cases."""
        print("=" * 60)
        print("GEMINI API TESTING SUITE")
        print("=" * 60)

        results = {
            "Model Listing": await self.test_model_listing(),
            "Basic Generation": await self.test_basic_generation(),
            "Copywriting Generation": await self.test_copywriting_generation(),
            "Social Media Generation": await self.test_social_media_generation(),
            "Image Prompt Generation": await self.test_image_prompt_generation(),
            "Structured Output": await self.test_structured_output(),
            "Safety Settings": await self.test_safety_settings(),
        }

        print("\n" + "=" * 60)
        print("TEST RESULTS SUMMARY")
        print("=" * 60)

        passed = sum(1 for result in results.values() if result)
        total = len(results)

        for test_name, result in results.items():
            status = "✓ PASSED" if result else "✗ FAILED"
            print(f"{test_name:.<40} {status}")

        print(f"\nTotal: {passed}/{total} tests passed")
        print("=" * 60)

        return passed == total


async def main():
    """Main entry point for the testing script."""
    import sys

    # Check if API key is provided as command line argument
    api_key = sys.argv[1] if len(sys.argv) > 1 else None

    try:
        tester = GeminiAPITester(api_key=api_key)
        success = await tester.run_all_tests()
        sys.exit(0 if success else 1)
    except ValueError as e:
        print(f"\n❌ Configuration Error: {str(e)}")
        print("\nUsage:")
        print("  python test_gemini_api.py [API_KEY]")
        print("  or set GEMINI_API_KEY environment variable")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
