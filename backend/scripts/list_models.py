import asyncio
import os
import httpx
from dotenv import load_dotenv

async def list_gemini_models():
    load_dotenv("backend/.env")
    key = os.getenv("GEMINI_API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        print(f"Status: {resp.status_code}")
        print(f"Models: {resp.text[:1000]}")

if __name__ == "__main__":
    asyncio.run(list_gemini_models())
