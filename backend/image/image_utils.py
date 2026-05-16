def sanitize_image_prompt(prompt: str) -> str:
    """Ensure prompt fits DALL-E limits and constraints."""
    return prompt[:4000]
