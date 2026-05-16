import os
import base64
import asyncio
from ..utils.errors import AIProviderError

async def generate_image(prompt: str, size: str = "1024x1024") -> str:
    """
    Generates images using Gemini 3.1 Flash Image Preview multimodal model.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    model_id = os.getenv("GEMINI_MODEL_NAME", "gemini-3.1-flash-image-preview")
    
    if not api_key:
        return "https://placehold.co/1024x1024/1A1AAF/FFFFFF?text=No+API+Key"

    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        loop = asyncio.get_event_loop()
        
        # Ensure prompt is clean
        clean_prompt = f"Generate a high-resolution professional marketing image for IndiGo Airlines: {prompt}"

        def _call_gemini():
            return client.models.generate_content(
                model=model_id,
                contents=clean_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE'],
                )
            )

        response = await loop.run_in_executor(None, _call_gemini)
        
        for part in response.parts:
            # The SDK returns image bytes in inline_data
            if part.inline_data:
                img_bytes = part.inline_data.data
                b64 = base64.b64encode(img_bytes).decode('utf-8')
                mime = part.inline_data.mime_type or "image/png"
                return f"data:{mime};base64,{b64}"
            
        return "https://placehold.co/1024x1024/1A1AAF/FFFFFF?text=Image+Not+Found+In+Response"

    except Exception as e:
        print(f"Gemini 3.1 Image Error: {e}")
        # Return the prompt-based placeholder as a last resort
        keywords = "+".join(prompt.split()[:5])
        return f"https://placehold.co/1024x1024/1A1AAF/FFFFFF?text=AI+Generated:+{keywords}"
