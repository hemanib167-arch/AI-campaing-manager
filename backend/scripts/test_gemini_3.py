import os
import base64
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv("backend/.env")

def test_gemini_3():
    api_key = os.getenv("GEMINI_API_KEY")
    model_id = "gemini-3.1-flash-image-preview"
    
    print(f"Testing model: {model_id}")
    client = genai.Client(api_key=api_key)
    
    prompt = "A high-resolution marketing image of an IndiGo plane flying over the Himalayas, sunset."
    
    try:
        print("Sending request...")
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE'],
            )
        )
        
        print(f"Response Parts: {len(response.parts)}")
        for i, part in enumerate(response.parts):
            if part.text:
                print(f"Part {i} (TEXT): {part.text[:50]}...")
            if part.inline_data:
                print(f"Part {i} (IMAGE): Found image bytes! Length: {len(part.inline_data.data)}")
                with open(f"test_gen_{i}.png", "wb") as f:
                    f.write(part.inline_data.data)
                print(f"Saved to test_gen_{i}.png")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_gemini_3()
