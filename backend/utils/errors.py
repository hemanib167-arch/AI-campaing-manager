class CreativeStudioError(Exception):
    """Base exception for all 6E Creative Studio backend errors."""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class ValidationError(CreativeStudioError):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)

class NotFoundError(CreativeStudioError):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)

class AIProviderError(CreativeStudioError):
    def __init__(self, message: str):
        super().__init__(message, status_code=502)
