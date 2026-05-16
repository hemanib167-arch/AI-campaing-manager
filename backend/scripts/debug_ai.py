import asyncio
import os
import httpx
import json
from dotenv import load_dotenv

async def debug_ai():
    load_dotenv("backend/.env")
    
    key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    
    print(f"Testing Azure: {endpoint} / {deployment}")
    
    # Try a raw REST call to Azure
    url = f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-02-15-preview"
    
    headers = {
        "api-key": key,
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [{"role": "user", "content": "Say hello"}],
        "max_tokens": 10
    }
    
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(url, headers=headers, json=payload, timeout=30.0)
            print(f"Azure Status: {resp.status_code}")
            print(f"Azure Response: {resp.text[:200]}")
        except Exception as e:
            print(f"Azure REST Error: {e}")

    # Try a raw REST call to Gemini
    gemini_key = os.getenv("GEMINI_API_KEY")
    print(f"\nTesting Gemini: {gemini_key[:10]}...")
    
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
    gemini_payload = {
        "contents": [{"parts": [{"text": "Say hello"}]}]
    }
    
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(gemini_url, json=gemini_payload, timeout=30.0)
            print(f"Gemini Status: {resp.status_code}")
            print(f"Gemini Response: {resp.text[:200]}")
        except Exception as e:
            print(f"Gemini REST Error: {e}")

if __name__ == "__main__":
    asyncio.run(debug_ai())
