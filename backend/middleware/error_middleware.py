from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from ..utils.errors import CreativeStudioError
from ..observability.logger import get_logger

logger = get_logger(__name__)

async def error_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except CreativeStudioError as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"error": e.message}
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"error": e.detail}
        )
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={"error": "An internal server error occurred."}
        )
