import os
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = os.getenv("JWT_SECRET", "6e-creative-studio-secret-2025")
ALGORITHM = "HS256"

security = HTTPBearer(auto_error=False)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

async def auth_middleware(request: Request, call_next):
    # For hackathon: allow all requests but attach user info if token is present
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        user = verify_token(token)
        if user:
            request.state.user = user
        else:
            request.state.user = {"sub": "guest", "role": "reviewer"}
    else:
        request.state.user = {"sub": "guest", "role": "reviewer"}
        
    return await call_next(request)
