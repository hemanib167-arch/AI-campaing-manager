import asyncio
import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.llm.azure_openai_client import generate_text as test_azure
from backend.llm.gemini_client import generate_text as test_gemini
from backend.image.image_client import generate_image as test_image
from backend.core.social_service import social_service
from backend.core.copywriting_service import copywriting_service
from backend.core.banner_service import banner_service

async def run_diagnostics():
    print("=== 6E Creative Studio AI Diagnostics ===\n")

    # 1. Test Azure OpenAI
    print("[1/5] Testing Azure OpenAI (Text Generation)...")
    try:
        res = await test_azure("You are a helpful assistant.", "Say 'Azure is working' inside a JSON object with a 'message' key.")
        print(f"  [SUCCESS] Azure Response: {res}")
    except Exception as e:
        print(f"  [FAILED] Azure Error: {e}")

    # 2. Test Gemini Fallback
    print("\n[2/5] Testing Google Gemini (Fallback)...")
    try:
        res = await test_gemini("You are a helpful assistant.", "Say 'Gemini is working'")
        print(f"  [SUCCESS] Gemini Response: {res}")
    except Exception as e:
        print(f"  [FAILED] Gemini Error: {e}")

    # 3. Test Image Generation (DALL-E 3)
    print("\n[3/5] Testing Image Generation (DALL-E 3 / Azure)...")
    try:
        url = await test_image("A futuristic IndiGo airplane flying through a digital cloud of code, blue and white theme.")
        print(f"  [SUCCESS] Image URL: {url[:60]}...")
    except Exception as e:
        print(f"  [FAILED] Image Generation Error: {e}")

    # 4. Test Social Service Pipeline
    print("\n[4/5] Testing Full Social Service Pipeline...")
    try:
        payload = {"campaign_type": "sale", "description": "Flash sale for London flights"}
        res = await social_service.generate(payload)
        print(f"  [SUCCESS] Social Pipeline Success! Platforms: {list(res.keys())}")
    except Exception as e:
        print(f"  [FAILED] Social Pipeline Error: {e}")

    # 5. Test Copywriting Pipeline
    print("\n[5/5] Testing Full Copywriting Pipeline...")
    try:
        payload = {"channel": "email", "brief": "London route promo", "tone": "professional"}
        res = await copywriting_service.generate(payload)
        print(f"  [SUCCESS] Copywriting Pipeline Success! Headline: {res.get('headline')}")
    except Exception as e:
        print(f"  [FAILED] Copywriting Pipeline Error: {e}")

    print("\n=== Diagnostics Complete ===")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
    asyncio.run(run_diagnostics())
