

from google import genai
from google.genai import types
import sys

# 1. REPLACE WITH YOUR ACTUAL API KEY
API_KEY = "AlzaSyD-ZLqNEGB_rQXcF_DuKK931TDMEagKFa0A"

client = genai.Client(api_key=API_KEY)

print("Testing API key for image generation...")

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=["A simple green sphere on a white background"],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"]
        )
    )

    # Check if we got an image
    image_found = False
    for part in response.parts:
        if part.inline_data:
            image = part.as_image()
            image.save("test_key_result.png")
            print("✅ SUCCESS! Image generated and saved as 'test_key_result.png'.")
            image_found = True
    
    if not image_found:
        print("⚠️ Model responded but no image data was found in the response.")
        if response.text:
            print(f"Model message: {response.text}")

except Exception as e:
    print("❌ FAILED!")
    # Provide helpful feedback based on common errors
    error_msg = str(e).lower()
    if "401" in error_msg or "unauthorized" in error_msg:
        print("Reason: Invalid API Key. Check your key in AI Studio.")
    elif "403" in error_msg or "permission" in error_msg:
        print("Reason: Key is valid, but your account might not have access to this preview model yet.")
    elif "429" in error_msg:
        print("Reason: Rate limit exceeded. Wait a minute and try again.")
    else:
        print(f"Error Details: {e}")

