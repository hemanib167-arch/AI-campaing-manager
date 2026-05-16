import asyncio
import os
import httpx
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")

async def test_image():
    key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")

    print(f"Endpoint: {endpoint}")
    print(f"API Version: {api_version}")

    # Try common Azure DALL-E deployment names
    deployments_to_try = ["dall-e-3", "dalle3", "dall-e-3-prod", "image-generation"]

    headers = {
        "api-key": key,
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": "A blue IndiGo airline plane flying over clouds",
        "n": 1,
        "size": "1024x1024"
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        for dep in deployments_to_try:
            url = f"{endpoint}/openai/deployments/{dep}/images/generations?api-version={api_version}"
            print(f"\n[TRY] Deployment: {dep}")
            try:
                resp = await client.post(url, headers=headers, json=payload)
                print(f"  Status: {resp.status_code}")
                text = resp.text[:200]
                print(f"  Response: {text}")
                if resp.status_code == 200:
                    data = resp.json()
                    print(f"  IMAGE URL: {data['data'][0].get('url', 'no url')[:80]}")
                    break
            except Exception as e:
                print(f"  Error: {e}")

    # Also try Gemini Imagen as fallback
    print("\n--- Testing Gemini Imagen fallback ---")
    gemini_key = os.getenv("GEMINI_API_KEY")
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={gemini_key}"
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.get(gemini_url)
        models = resp.json().get("models", [])
        image_models = [m["name"] for m in models if "imagen" in m["name"].lower() or "image" in m.get("displayName","").lower()]
        print(f"  Available image models: {image_models}")

if __name__ == "__main__":
    asyncio.run(test_image())
