"""
Gemini Image Generation Testing Script
Tests Google's Gemini API with image generation capabilities using the new google.genai package.
"""

import os
import sys
from typing import Optional

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("❌ google-genai package not installed.")
    print("Install it with: pip install google-genai")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("❌ PIL (Pillow) package not installed.")
    print("Install it with: pip install Pillow")
    sys.exit(1)


class GeminiImageTester:
    """Test suite for Gemini Image Generation API."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini image generation tester.

        Args:
            api_key: Gemini API key. If not provided, reads from GEMINI_API_KEY env var.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Gemini API key is required. "
                "Set GEMINI_API_KEY environment variable or pass it directly."
            )

        # Initialize the client with API key
        self.client = genai.Client(api_key=self.api_key)

    def test_text_generation(self):
        """Test basic text generation."""
        print("\n=== Testing Text Generation ===")

        try:
            prompt = "Write a catchy tagline for an eco-friendly water bottle brand."

            response = self.client.models.generate_content(
                model="gemini-2.0-flash-exp",
                contents=[prompt],
            )

            for part in response.parts:
                if part.text is not None:
                    print(f"✓ Success! Generated text:\n{part.text}")
                    return True

            print("✗ No text generated")
            return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    def test_image_generation(self):
        """Test image generation with Gemini."""
        print("\n=== Testing Image Generation ===")

        try:
            prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"

            print(f"Generating image for prompt: '{prompt}'")

            response = self.client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[prompt],
            )

            text_found = False
            image_found = False

            for part in response.parts:
                if part.text is not None:
                    print(f"Text response: {part.text}")
                    text_found = True
                elif part.inline_data is not None:
                    image = part.as_image()
                    output_path = "test_generated_image.png"
                    image.save(output_path)
                    print(f"✓ Success! Image saved to: {output_path}")
                    image_found = True

            if image_found:
                return True
            else:
                print("✗ No image generated")
                return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    def test_campaign_image_generation(self):
        """Test image generation for a marketing campaign."""
        print("\n=== Testing Campaign Image Generation ===")

        try:
            prompt = (
                "Create a professional product photography image: "
                "A sleek sustainable water bottle on a wooden table, "
                "natural morning light from a window, "
                "green plants in soft focus background, "
                "warm and inviting atmosphere, "
                "high-end lifestyle aesthetic"
            )

            print(f"Generating campaign image...")

            response = self.client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[prompt],
            )

            for part in response.parts:
                if part.text is not None:
                    print(f"Description: {part.text}")
                elif part.inline_data is not None:
                    image = part.as_image()
                    output_path = "campaign_generated_image.png"
                    image.save(output_path)
                    print(f"✓ Success! Campaign image saved to: {output_path}")
                    return True

            print("✗ No image generated")
            return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    def test_social_media_image(self):
        """Test image generation for social media."""
        print("\n=== Testing Social Media Image Generation ===")

        try:
            prompt = (
                "Create a square Instagram post image (1:1 aspect ratio): "
                "Minimalist flat lay of eco-friendly products, "
                "pastel green background, "
                "sustainable bamboo items, reusable containers, "
                "natural textures, soft shadows, "
                "clean and modern aesthetic, "
                "Instagram-worthy composition"
            )

            print(f"Generating social media image...")

            response = self.client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[prompt],
            )

            for part in response.parts:
                if part.text is not None:
                    print(f"Description: {part.text}")
                elif part.inline_data is not None:
                    image = part.as_image()
                    output_path = "social_media_generated_image.png"
                    image.save(output_path)
                    print(f"✓ Success! Social media image saved to: {output_path}")
                    return True

            print("✗ No image generated")
            return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    def test_banner_ad_generation(self):
        """Test banner ad image generation."""
        print("\n=== Testing Banner Ad Generation ===")

        try:
            prompt = (
                "Create a wide banner advertisement (16:9 aspect ratio): "
                "Luxury watch on a dark marble surface, "
                "dramatic side lighting creating highlights on metal, "
                "sleek and sophisticated, "
                "copy space on the right side, "
                "premium brand aesthetic, "
                "dark mood with golden accents"
            )

            print(f"Generating banner ad...")

            response = self.client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[prompt],
            )

            for part in response.parts:
                if part.text is not None:
                    print(f"Description: {part.text}")
                elif part.inline_data is not None:
                    image = part.as_image()
                    output_path = "banner_ad_generated_image.png"
                    image.save(output_path)
                    print(f"✓ Success! Banner ad saved to: {output_path}")
                    return True

            print("✗ No image generated")
            return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    def test_multimodal_generation(self):
        """Test multimodal generation (text + image together)."""
        print("\n=== Testing Multimodal Generation ===")

        try:
            prompt = (
                "Generate an image and description for a sustainable fashion campaign. "
                "Image: A model wearing eco-friendly clothing in a natural outdoor setting, "
                "golden hour lighting, authentic and inspiring mood. "
                "Also provide a short campaign tagline."
            )

            print(f"Generating multimodal content...")

            response = self.client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[prompt],
            )

            text_parts = []
            image_count = 0

            for part in response.parts:
                if part.text is not None:
                    text_parts.append(part.text)
                    print(f"Text: {part.text}")
                elif part.inline_data is not None:
                    image = part.as_image()
                    output_path = f"multimodal_generated_image_{image_count}.png"
                    image.save(output_path)
                    print(f"✓ Image saved to: {output_path}")
                    image_count += 1

            if text_parts and image_count > 0:
                print(f"✓ Success! Generated {len(text_parts)} text parts and {image_count} images")
                return True
            elif text_parts or image_count > 0:
                print(f"⚠ Partial success: {len(text_parts)} text parts, {image_count} images")
                return True
            else:
                print("✗ No content generated")
                return False

        except Exception as e:
            print(f"✗ Error: {str(e)}")
            return False

    def run_all_tests(self):
        """Run all test cases."""
        print("=" * 60)
        print("GEMINI IMAGE GENERATION TESTING SUITE")
        print("=" * 60)

        results = {
            "Text Generation": self.test_text_generation(),
            "Image Generation": self.test_image_generation(),
            "Campaign Image": self.test_campaign_image_generation(),
            "Social Media Image": self.test_social_media_image(),
            "Banner Ad Generation": self.test_banner_ad_generation(),
            "Multimodal Generation": self.test_multimodal_generation(),
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

        if passed > 0:
            print("\n📁 Generated files:")
            import glob
            image_files = glob.glob("*_generated_image*.png")
            for img in image_files:
                print(f"  - {img}")

        print("=" * 60)

        return passed == total


def main():
    """Main entry point for the testing script."""

    # Check if API key is provided as command line argument
    api_key = sys.argv[1] if len(sys.argv) > 1 else None

    try:
        tester = GeminiImageTester(api_key=api_key)
        success = tester.run_all_tests()
        sys.exit(0 if success else 1)
    except ValueError as e:
        print(f"\n❌ Configuration Error: {str(e)}")
        print("\nUsage:")
        print("  python test_gemini_image.py [API_KEY]")
        print("  or set GEMINI_API_KEY environment variable")
        print("\nTo get an API key:")
        print("  1. Visit https://makersuite.google.com/app/apikey")
        print("  2. Create a new API key")
        print("  3. Set it as GEMINI_API_KEY environment variable")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
