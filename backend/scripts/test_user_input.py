import asyncio
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.core.social_service import social_service

async def test_user_input():
    load_dotenv(Path(__file__).parent.parent / ".env")
    
    # User's exact input from screenshot
    payload = {
        "campaign_type": "Seasonal Campaign",
        "description": "This is the diwali seasonal discount on tickets"
    }
    
    print(f"Testing with payload: {payload}")
    try:
        res = await social_service.generate(payload)
        print("SUCCESS!")
        print(res)
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    asyncio.run(test_user_input())
